import flatbuffers
from flask import request, make_response
from WebApplication.Document.Protocol.protocol import *

buff_size = 128

def registAccount(username, name, password):
    builder = flatbuffers.Builder(buff_size)
    
    username_offset = builder.CreateString(username)
    name_offset = builder.CreateString(name)
    password_offset = builder.CreateString(password)

    proto_registAccountStart(builder)
    proto_registAccountAddUsername(builder, username_offset)
    proto_registAccountAddName(builder, name_offset)
    proto_registAccountAddPassword(builder, password_offset)
    
    root_offset = proto_registAccountEnd(builder)

    builder.Finish(root_offset)

    return builder
    