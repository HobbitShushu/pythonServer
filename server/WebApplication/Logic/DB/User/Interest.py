from WebApplication.Infra.AlchemyDB import dbSession, dbCommander
from WebApplication.Document.Models.User import * 
from application import cache

class sp_getUserInterest(object):
    def __init__(self, useridx):
        self.useridx = useridx

    def execute(self):
        with dbSession() as session:
            data = session.query(user_interest) \
                .filter(user_interest.useridx == self.useridx)
            
            commander = dbCommander(data)
            values = commander.to_list()

            result = {}
            if len(values) > 0:
                result = values[0]['interest']

            for i in result:
                print(result[i])

            return result

class sp_setUserInterest(object):
    def __init__(self, useridx, data):
        self.useridx = useridx
        self.data = data

    def execute(self):
        with dbSession() as session:
            # check user interest was already set
            data = session.query(user_interest) \
                .filter(user_interest.useridx == self.useridx) \
                
            commander = dbCommander(data)
            values = commander.to_list()

            if len(values) == 0:
                new_data = user_interest(self.useridx, self.data)
                session.add(new_data)
                
                try:
                    session.commit()
                
                except Exception as error:
                    print(error)
                return
            
            # already user interest was set
            else:
                data[0].interest = self.data
                try:
                    session.commit()
                    print(data[0].interest)
                except Exception as error:
                    print(error)

                return                                
