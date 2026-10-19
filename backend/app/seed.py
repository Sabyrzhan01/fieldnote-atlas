from uuid import uuid4

COLLECTIONS = [
    {"id":"c1","title":"The city after rain","subtitle":"Urban memory · Almaty","color":"#d87551"},
    {"id":"c2","title":"Quiet infrastructures","subtitle":"Hidden systems · 2025","color":"#73937c"},
    {"id":"c3","title":"Edges of the steppe","subtitle":"Landscape study · 2024","color":"#c6a45a"},
]
OBSERVATIONS = [
    {"id":"1","title":"A city measured in puddles","body":"After the storm, people follow the dry edges of the sidewalk. The shortcuts form a second map, visible for only an hour.","kind":"Field note","place":"Abay Avenue","region":"Almaty, Kazakhstan","date":"Oct 18, 2025","color":"#d87551","tags":["rain","movement","informal paths"],"source":"Walk 04 · 7:42 AM","starred":True},
    {"id":"2","title":"“We wait for the second bus”","body":"The first bus arrives full from the depot. At this stop, the timetable is less useful than watching the traffic light cycle.","kind":"Interview","place":"Dostyk × Satpaev","region":"Almaty, Kazakhstan","date":"Oct 16, 2025","color":"#73937c","tags":["transit","waiting"],"source":"Conversation with Aigerim","starred":False},
    {"id":"3","title":"The blue repair patch","body":"A square of newer asphalt interrupts the old surface. Three different utility marks cross its edge; the patch is already sinking.","kind":"Artifact","place":"Panfilov Street","region":"Almaty, Kazakhstan","date":"Oct 12, 2025","color":"#c6a45a","tags":["maintenance","layers"],"source":"Photo archive · 03","starred":True},
    {"id":"4","title":"A pause beneath the plane trees","body":"At noon, the shade moves across the bench faster than the queue for the kiosk. People adjust their position without speaking.","kind":"Field note","place":"Kok Tobe foothills","region":"Almaty, Kazakhstan","date":"Oct 08, 2025","color":"#8c7aa8","tags":["shade","public space"],"source":"Walk 03 · 12:16 PM","starred":False},
    {"id":"5","title":"The unofficial noticeboard","body":"A layer of small handwritten ads has grown around the official route map. New paper covers the old in a neat, local chronology.","kind":"Signal","place":"Green Bazaar entrance","region":"Almaty, Kazakhstan","date":"Oct 03, 2025","color":"#d87551","tags":["signage","community"],"source":"Photo archive · 01","starred":False},
    {"id":"6","title":"“Everyone knows which door”","body":"The building has four entrances. Residents use one, couriers another, and the caretaker keeps the side gate open for everyone.","kind":"Interview","place":"Bostandyk district","region":"Almaty, Kazakhstan","date":"Sep 26, 2025","color":"#73937c","tags":["thresholds","access"],"source":"Conversation with Marat","starred":False},
]
def seeded():
    items=[]
    for source in OBSERVATIONS:
        item=dict(source); item["id"]=str(uuid4()); item["collection_id"]="c1"; items.append(item)
    return items
