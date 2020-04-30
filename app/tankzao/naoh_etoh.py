from flask_restful import Resource, request
import random
import time
import os
import requests

naetoh_tank = {
    'nome': "naoh-etoh",
    'volume_naoh': 0,
    'volume_etoh': 0
    
}

BASE_URL = "https://destrotrampo.herokuapp.com/"

class tankzao(Resource):
    def __init__(self):
        self.tank_url = BASE_URL + '/naoh-etoh'
        
    def get(self):
        return naetoh_tank, 200
    
    def post_EtOH(self):
        json_data = request.get_json(force=True)
        origem = json_data.get('origem', None)
        etoh = json_data.get('etoh', None)
        naoh = json_data.get('naoh', None)
        
        if origem is None:
            json = {
                "status_code": 400,
                "body": "Bad Request"
            }
        if origem == "etoh":
            if etoh is not None:
                naetoh_tank['volume_etoh'] += etoh
            else:
                json = {
                "status_code": 400,
                "body": "Bad Request"
            }
        
        if origem == "reator":
            if etoh is None or naoh is None:
              json = {
                "status_code": 400,
                "body": "Bad Request"
                }
              return json
            if etoh <= naetoh_tank['volume_etoh']:
                json = {"volume_etoh": etoh,
                }
                naetoh_tank['volume_etoh'] -= etoh
            if naoh <= naetoh_tank['volume_naoh']:
                json["volume_naoh"] = naoh
                naetoh_tank['volume_naoh'] -= naoh        
        # requests.post(url=REATOR_URL, json=json, headers={"Content_Type": "application/json"})
        return json
       
    def put(self):
        naetoh_tank['volume_naoh'] += 0.45
        naetoh_tank['volume_etoh'] += 1
        return 200

    def run(self):
        
        while (True):
            time.sleep(1)
            try:
                requests.put(url=self.tank_url)  
            except Exception as e:
                print(e)             
