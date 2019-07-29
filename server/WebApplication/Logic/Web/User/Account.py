from WebApplication.Logic.DB.User.Account import *
from WebApplication.Document.Protocol.protocol import *
from WebApplication.Infra.Web import *
from application import app, buff_size

import flatbuffers, datetime

@app.route('/account', methods=['GET'])
def all_account():
    sp = sp_readAllUserAccount()
    sp.execute()
    return make_response("Index page"), 200

@app.route('/account/login', methods=['POST'])
def try_login():
    buf = getRequestData()
    proto = proto_registAccount.GetRootAsproto_registAccount(buf, 0)

    username = proto.Username()
    password = proto.Password()

    sp = sp_userLogin(username, password)
    sp.execute()
    
    return make_response('try login'), 200
    
@app.route('/account/regist', methods = ['POST'])
def regist():
    buf = getRequestData()
    proto = proto_registAccount.GetRootAsproto_registAccount(buf, 0)
    
    username = proto.Username()
    name = proto.Name()
    password = proto.Password()

    sp = sp_createUserAccount(username, password, name)
    sp.execute()
    return make_response('try_regist'), 200

@app.route('/account/<username>', methods=['GET'])
def readUserInfo(username):
    sp = sp_readUserInfo(username)
    result = sp.execute()

    builder = flatbuffers.Builder(buff_size)
    
    if len(result) > 0:
        username_offset = builder.CreateString(result['account']['username'])
        name_offset = builder.CreateString(result['account']['name'])
        date_offset = builder.CreateString(str(result['account']['login_date']))

        proto_onReadUserInfoStart(builder)
        proto_onReadUserInfoAddUsername(builder, username_offset)
        proto_onReadUserInfoAddName(builder, name_offset)
        proto_onReadUserInfoAddRegistDate(builder, date_offset)
        root_offset = proto_onReadUserInfoEnd(builder)
    
    builder.Finish(root_offset)
    
    return getResponseData(builder.Output())