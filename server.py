"""Dependency-free local web/API server. Uses SQLite via Python's DB-API."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json, sqlite3, uuid, os
ROOT=Path(__file__).parent
DB=Path(os.getenv('FIELDNOTE_DB_PATH',ROOT/'fieldnote.db'))
SEED=[
('1','A city measured in puddles','After the storm, people follow the dry edges of the sidewalk. The shortcuts form a second map, visible for only an hour.','Field note','Abay Avenue','Almaty, Kazakhstan','Oct 18, 2025','#d87551',['rain','movement','informal paths'],'Walk 04 · 7:42 AM',1,31,39),
('2','“We wait for the second bus”','The first bus arrives full from the depot. At this stop, the timetable is less useful than watching the traffic light cycle.','Interview','Dostyk × Satpaev','Almaty, Kazakhstan','Oct 16, 2025','#73937c',['transit','waiting'],'Conversation with Aigerim',0,56,51),
('3','The blue repair patch','A square of newer asphalt interrupts the old surface. Three different utility marks cross its edge; the patch is already sinking.','Artifact','Panfilov Street','Almaty, Kazakhstan','Oct 12, 2025','#c6a45a',['maintenance','layers'],'Photo archive · 03',1,68,33),
('4','A pause beneath the plane trees','At noon, the shade moves across the bench faster than the queue for the kiosk. People adjust their position without speaking.','Field note','Kok Tobe foothills','Almaty, Kazakhstan','Oct 08, 2025','#8c7aa8',['shade','public space'],'Walk 03 · 12:16 PM',0,42,67),
('5','The unofficial noticeboard','A layer of small handwritten ads has grown around the official route map. New paper covers the old in a neat, local chronology.','Signal','Green Bazaar entrance','Almaty, Kazakhstan','Oct 03, 2025','#d87551',['signage','community'],'Photo archive · 01',0,75,72),
('6','“Everyone knows which door”','The building has four entrances. Residents use one, couriers another, and the caretaker keeps the side gate open for everyone.','Interview','Bostandyk district','Almaty, Kazakhstan','Sep 26, 2025','#73937c',['thresholds','access'],'Conversation with Marat',0,24,23)]
COLS=[('c1','The city after rain','Urban memory · Almaty','#d87551'),('c2','Quiet infrastructures','Hidden systems · 2025','#73937c'),('c3','Edges of the steppe','Landscape study · 2024','#c6a45a')]
def connect():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;c.execute('PRAGMA foreign_keys=ON');c.execute('CREATE TABLE IF NOT EXISTS collections(id TEXT PRIMARY KEY,title TEXT NOT NULL,subtitle TEXT NOT NULL,color TEXT NOT NULL)');c.execute('''CREATE TABLE IF NOT EXISTS observations(id TEXT PRIMARY KEY,collection_id TEXT NOT NULL REFERENCES collections(id),title TEXT NOT NULL,body TEXT NOT NULL,kind TEXT NOT NULL,place TEXT NOT NULL,region TEXT NOT NULL,date TEXT NOT NULL,color TEXT NOT NULL,tags TEXT NOT NULL,source TEXT NOT NULL,starred INTEGER NOT NULL,x REAL NOT NULL,y REAL NOT NULL)''')
 if not c.execute('SELECT 1 FROM collections LIMIT 1').fetchone():
  c.executemany('INSERT INTO collections VALUES(?,?,?,?)',COLS)
  c.executemany('INSERT INTO observations VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',[(s[0],'c1',s[1],s[2],s[3],s[4],s[5],s[6],s[7],json.dumps(s[8]),s[9],s[10],s[11],s[12]) for s in SEED])
 c.commit();return c
def atlas(c):
 cols=[dict(r) for r in c.execute('SELECT c.*,count(o.id) observationCount FROM collections c LEFT JOIN observations o ON c.id=o.collection_id GROUP BY c.id')]
 obs=[]
 for r in c.execute('SELECT * FROM observations ORDER BY rowid DESC'):
  n=dict(r);n['tags']=json.loads(n['tags']);n['starred']=bool(n['starred']);obs.append(n)
 return {'collections':cols,'observations':obs}
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(ROOT),**kwargs)
 def log_message(self,fmt,*args):print('%s - %s'%(self.address_string(),fmt%args))
 def send_json(self,status,obj):
  raw=json.dumps(obj).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(raw)));self.send_header('Access-Control-Allow-Origin','*');self.end_headers();self.wfile.write(raw)
 def do_OPTIONS(self):self.send_response(204);self.send_header('Access-Control-Allow-Origin','*');self.send_header('Access-Control-Allow-Methods','GET,POST,DELETE,OPTIONS');self.send_header('Access-Control-Allow-Headers','Content-Type');self.end_headers()
 def do_GET(self):
  if self.path=='/api/health':return self.send_json(200,{'status':'ok'})
  if self.path=='/api/atlas':
   c=connect()
   try:return self.send_json(200,atlas(c))
   finally:c.close()
  return super().do_GET()
 def do_POST(self):
  c=connect()
  try:
   parts=self.path.strip('/').split('/')
   if self.path=='/api/observations':
    try:data=json.loads(self.rfile.read(int(self.headers.get('Content-Length',0))))
    except Exception:return self.send_json(400,{'detail':'Invalid JSON'})
    title=str(data.get('title','')).strip();body=str(data.get('body','')).strip()
    if not title or len(title)>120 or not body or len(body)>1000:return self.send_json(422,{'detail':'Title (1–120 chars) and body (1–1000 chars) are required'})
    collection_id=str(data.get('collection_id','c1'))
    if not c.execute('SELECT 1 FROM collections WHERE id=?',(collection_id,)).fetchone():return self.send_json(422,{'detail':'Unknown collection'})
    ident=str(uuid.uuid4());c.execute('INSERT INTO observations VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(ident,collection_id,title,body,data.get('kind','Field note'),str(data.get('place','Almaty'))[:160],data.get('region','Almaty, Kazakhstan'),data.get('date','Today'),data.get('color','#d87551'),json.dumps(data.get('tags',[])),data.get('source','Field note'),int(bool(data.get('starred',False))),float(data.get('x',50)),float(data.get('y',50))));c.commit();return self.send_json(201,atlas(c))
   if len(parts)==4 and parts[:2]==['api','observations'] and parts[3]=='star':
    cur=c.execute('UPDATE observations SET starred=1-starred WHERE id=?',(parts[2],));c.commit()
    return self.send_json(200,atlas(c)) if cur.rowcount else self.send_json(404,{'detail':'Observation not found'})
   return self.send_json(404,{'detail':'Not found'})
  finally:c.close()
 def do_DELETE(self):
  parts=self.path.strip('/').split('/')
  if len(parts)==3 and parts[:2]==['api','observations']:
   c=connect()
   try:
    cur=c.execute('DELETE FROM observations WHERE id=?',(parts[2],));c.commit()
    return self.send_json(200,atlas(c)) if cur.rowcount else self.send_json(404,{'detail':'Observation not found'})
   finally:c.close()
  return self.send_json(404,{'detail':'Not found'})
if __name__=='__main__':
 connect().close();print(f'Fieldnote Atlas running at http://127.0.0.1:8091 (SQLite: {DB})');ThreadingHTTPServer(('127.0.0.1',8091),Handler).serve_forever()
