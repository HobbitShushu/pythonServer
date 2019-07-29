from WebApplication.Logic.DB.User.Equipment import *
from WebApplication.Document.Protocol.protocol import *
from WebApplication.Infra.Web import *
from application import app, buff_size

import flatbuffers, datetime

# 장비 소환
@app.route('/user/equipment/summonEquipments', methods=['POST'])
def summonEquipment():
    return make_response('summon equipment'), 200

# 장비 장착
@app.route('/user/equipment/takeEquipment', methods=['POST'])
def takeEquipment():
    #sp = sp_takeEquipment()
    return make_response('take equipment'), 200

@app.route('/user/equipment/reinforcement', methods=['POST'])
def reinforcementEquipment():
    
    return make_response('reinforcement equipment'), 200