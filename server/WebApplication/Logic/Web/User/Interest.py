from WebApplication.Logic.DB.User.Interest import *
from application import app
from flask import request, make_response

@app.route('/interest/<int:useridx>', methods=['GET'])
def getUserInterest(useridx):
    sp = sp_getUserInterest(useridx)
    result = sp.execute()

    return make_response('log in page'), 200

@app.route('/interest', methods=['POST'])
def setUserInterest():
    useridx = request.headers['Useridx']
    interest = request.get_json()
    sp = sp_setUserInterest(useridx, interest)
    sp.execute()
    return make_response('try login'), 200
