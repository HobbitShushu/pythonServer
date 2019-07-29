from flask import request, make_response
import requests

def getResponseData(buf):
    res = make_response(buf)
    res.headers['Content-Type'] = 'application/octet-stream'
    
    return res

def getRequestData():
    buf = bytearray(request.get_data())
    
    return buf
