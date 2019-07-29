from WebApplication.Logic.DB.User.Character import *
from WebApplication.Document.Protocol.protocol import *
from WebApplication.Infra.Web import *
from application import app, buff_size

import flatbuffers, datetime

@app.route('/user/character/<int:useridx>', methods=['GET'])
def readCharacters(useridx):
    sp = sp_readCharacters(useridx)
    character_list = sp.execute()

    builder = flatbuffers.Builder(buff_size)
    
    proto_onReadCharactersStartCharactersVector(builder, len(character_list))
    for character in character_list:
        Createproto_characterInfo(builder, character['characteridx'], character['grade'], character['level'], character['exp'], character['awaken'], character['soulWeapon'], character['soulArmor'], character['soulTreasure'])
    character_offset = builder.EndVector(len(character_list))

    proto_onReadCharactersStart(builder)
    proto_onReadCharactersAddCharacters(builder, character_offset)
    root_offset = proto_onReadCharactersEnd(builder)
    builder.Finish(root_offset)

    return getResponseData(builder.Output())

@app.route('/user/character/<int:useridx>/<int:characteridx>', methods=['GET'])
def readCharacter(useridx, characteridx):
    sp = sp_readCharacter(useridx, characteridx)
    equipment_list = sp.execute()