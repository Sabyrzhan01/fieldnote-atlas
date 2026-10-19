export type Observation={id:string,collection_id?:string,title:string,body:string,kind:'Field note'|'Interview'|'Artifact'|'Signal',place:string,region:string,date:string,color:string,tags:string[],source:string,starred:boolean};
export type Collection={id:string,title:string,subtitle:string,color:string,observationCount:number};
export type AtlasData={collections:Collection[],observations:Observation[]};
