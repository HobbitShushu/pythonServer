import requests
import flatbuffers
from flask import request, make_response
from WebApplication.Document.Protocol.protocol import *
from WebApplication.web.web import *

buff_size = 128

my_url = 'http://127.0.0.1:5000/'
login_url = my_url + 'account/login'
regist_url = my_url + 'account/regist'
user_info_url = my_url + 'account/'

my_id = input('input your id : ')

while 1:
    selected = input('1. recommend user\n2.request friend\n3. response friend request : ')
    if selected == 'url':
        url = input("enter url : ")
        if len(url) == 0:
            break
        
        req = requests.get(my_url + url)
        
        # test
        '''
        buf = bytearray(req.content)
        proto = proto_onReadFriendList.GetRootAsproto_onReadFriendList(buf, 0)
        recommend_list = proto.FregiriendList
        len = proto.FriendListLength()
        for i in range(0, len):
            friend = recommend_list(i)
            print(friend.Name())
            print(friend.RegistDate())
        '''    
    elif selected == 'regist':
        
        username = input("enter user name : ")
        name = input("enter name")
        password = input("password")
        builder = registAccount(username, name, password)
        data = builder.Output()
        req = requests.post(my_url + 'account/regist', data = data)
    
    elif selected == 'login':

        username = input("enter user name : ")
        name = ""
        password = input("password")
        builder = registAccount(username, name, password)
        data = builder.Output()
        req = requests.post(my_url + 'account/login', data = data)

    if selected == '1':    
        url = input("enter url : ")
        if len(url) == 0:
            break
            #params = input("enter params : ")
        params = ''
        print(my_url + url)
        req = requests.get(my_url + url, params=params)

        buf = bytearray(req.content)
        proto = proto_onReadFriendList.GetRootAsproto_onReadFriendList(buf, 0)
        recommend_list = proto.FriendList
        len = proto.FriendListLength()
        for i in range(0, len):
            friend = recommend_list(i)
            print(friend.Name())
            print(friend.RegistDate())

    if selected == '2':
        url = input("enter url : ")
        if len(url) == 0:
            break
            #params = input("enter params : ")
        params = ''
        print(my_url + url)
        req = requests.get(my_url + url, params=params)

        print(req.content)
    
    if selected == '3':
        url = 'user/friend'
            
        userid = input('enter userid : ')
        targetidx = input('enter targetidx : ')
        
        state = input('enter state : ')

        builder = flatbuffers.Builder(128)
        proto_headerStart(builder)
        proto_headerAddUseridx(builder, int(userid))
        header_offset = proto_headerEnd(builder)

        proto_responseFriendRequestStart(builder)
        proto_responseFriendRequestAddHeader(builder, header_offset)
        proto_responseFriendRequestAddTargetidx(builder, int(targetidx))
        proto_responseFriendRequestAddState(builder, int(state))
        root_offset = proto_responseFriendRequestEnd(builder)
        
        builder.Finish(root_offset)
        
        #res = make_response(builder.Output())
        #res.headers['Content-Type'] = 'application/octet-stream'
        data = builder.Output()
        req = requests.post(my_url + url, data = data)
    
    '''
    user_name = input("Enter user name : ")
    if len(user_name) == 0:
        break
    
    req = requests.get(user_info_url + user_name)

    buf = bytearray(req.content)
    #buf = bytearray(request.get_data())
    #buf = getRequestData()

    proto = proto_onReadUserInfo.GetRootAsproto_onReadUserInfo(buf, 0)
    username = proto.Username().decode('utf-8')
    name = proto.Name().decode('utf-8')
    date = proto.RegistDate().decode('utf-8')

    print(username)
    print(name)
    print(date)
    '''