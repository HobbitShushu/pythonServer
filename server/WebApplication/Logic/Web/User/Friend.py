from WebApplication.Logic.DB.User.Friend import *
from WebApplication.Document.Protocol.protocol import *
from WebApplication.Infra.Web import *
from application import app, buff_size

import flatbuffers, datetime

@app.route('/user/friend/<int:useridx>', methods=['GET'])
def getFriendList(useridx):
    sp = sp_getFriendList(useridx)
    friend_list = sp.execute()

    builder = flatbuffers.Builder(buff_size)
    userInfoOffset_list = []
    for friend in friend_list:
        name_offset = builder.CreateString(friend['name'])
        date_offset = builder.CreateString(str(friend['regist_date']))

        proto_userInfoStart(builder)
        proto_userInfoAddName(builder, name_offset)
        proto_userInfoAddRegistDate(builder, date_offset)
        userInfo_offset = proto_userInfoEnd(builder)
  
        userInfoOffset_list.append(userInfo_offset)

    proto_onReadFriendListStartFriendListVector(builder, len(userInfoOffset_list))
    for friendList_offset in userInfoOffset_list:
        builder.PrependUOffsetTRelative(friendList_offset)
    friendList_offset = builder.EndVector(len(userInfoOffset_list))

    proto_onReadFriendListStart(builder)
    proto_onReadFriendListAddFriendList(builder, friendList_offset)
    
    root_offset = proto_onReadFriendListEnd(builder)
    builder.Finish(root_offset)

    return getResponseData(builder.Output())

@app.route('/user/friend/recommend/<int:useridx>', methods=['GET'])
def getFriendRecommend(useridx): 
    sp = sp_getFriendRecommend(useridx)
    result = sp.execute()
    
    builder = flatbuffers.Builder(buff_size)
    if len(result) > 0:
        recommendOffset_list = []
        for row in result:
            name_offset = builder.CreateString(row['name'])
            date_offset = builder.CreateString(str(row['regist_date']))

            proto_userInfoStart(builder)
            proto_userInfoAddName(builder, name_offset)
            proto_userInfoAddRegistDate(builder, date_offset)
            recommend_offset = proto_userInfoEnd(builder)
            recommendOffset_list.append(recommend_offset)

        proto_onReadFriendListStartFriendListVector(builder, len(result))
        for list_offset in recommendOffset_list:
            builder.PrependUOffsetTRelative(list_offset)
        recommendList_offset = builder.EndVector(len(result))

        proto_onReadFriendListStart(builder)
        proto_onReadFriendListAddFriendList(builder, recommendList_offset)
        root_offset = proto_onReadFriendListEnd(builder)
        
        builder.Finish(root_offset)

    return getResponseData(builder.Output())

@app.route('/user/friend/<int:useridx>/<int:targetidx>', methods=['GET'])
def requestFriend(useridx, targetidx):
    sp = sp_requestFriend(useridx, targetidx)
    sp.execute()
    
    return make_response('request friend'), 200

@app.route('/user/friend', methods=['POST'])
def responseFriend():
    buf = getRequestData()
    proto = proto_responseFriendRequest.GetRootAsproto_responseFriendRequest(buf, 0)
    header = proto.Header()
    
    useridx = header.Useridx()
    targetidx = proto.Targetidx()
    state = proto.State()

    sp = sp_responseFriend(useridx, targetidx, state)
    sp.execute()

    return make_response('response friend request'), 200

