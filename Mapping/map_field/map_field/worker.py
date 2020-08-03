import pandas as pd
from fuzzywuzzy import fuzz
import json

class MapingFields():
        def __init__(self,source,target):
                self.source=source
                self.target=target
                
        def Map_Fields(self,Flag):
                try:
                        source_df = pd.DataFrame(self.source)
                        target_df = pd.DataFrame(self.target)
                        source_df = source_df.rename(columns={'formatName':'SourceformatName','formatFields':'SourceformatFields'})
                        target_df = target_df.rename(columns={'formatName':'targetformatName','formatFields':'targetformatFields'})
                        data = pd.concat((source_df,target_df),axis=1)
                        l1 = []
                        if Flag == 'match':
                                for i in range(len(data)):
                                        l1.append(fuzz.partial_ratio(data['SourceformatFields'][i].lower(),data['targetformatFields'][i].lower()))
                        else :
                                for i in range(len(data)):
                                        l1.append(fuzz.token_set_ratio(data['SourceformatFields'][i].lower(),data['targetformatFields'][i].lower()))
                        data['confidence']=l1
                        data=data[['SourceformatFields','targetformatFields','confidence']]
                        overallConfidence=(data["confidence"].sum()/len(data))

                        if Flag =='match':
                                final_result={"sourceformatName":self.source["formatName"],"targetformatName":self.target["formatName"],
                                      "overallConfidence":overallConfidence,"mappings":data.to_json(orient='records')}
                        else :

                                final_result={"sourceformatName":self.source["formatName"],"targetformatName":self.target["formatName"],
                                      "overallConfidence":overallConfidence,"mappings":data.to_dict(orient='records')}
                        

                        json_object = json.dumps(final_result) 
                        with open("sample_db.json", "w") as outfile: 
                             outfile.write(json_object) 

                        return final_result
                except:
                        return None
        def Map_Learn(self,Mapping):
                
                        final_result={"sourceformatName":self.source["formatName"],"targetformatName":self.target["formatName"],"mappings":Mapping}
                        json_object = json.dumps(final_result) 
                        with open("sample_db.json", "w") as outfile: 
                             outfile.write(json_object) 
                        res={"sourceformatName":self.source["formatName"],"targetformatName":self.target["formatName"],"Message" :"Learned the mappings"}
                        return res
                
                        
