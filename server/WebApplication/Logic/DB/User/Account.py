from WebApplication.Infra.AlchemyDB import dbSession, dbCommander
from WebApplication.Document.Models.User import * 
from application import cache

class sp_readAllUserAccount(object):
    def __init__(self):
        self.all_account = []
    
    def execute(self):
        with dbSession() as session:
            query = session.query(user_account). \
                all()

            userAccount_list = []
            for account in query:
                commander = dbCommander(account)
                userAccount_list.append(commander.parsing())
            
            for account in userAccount_list:
                print(account)

class sp_createUserAccount(object):
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    def execute(self):
        with dbSession() as session:
            query = user_account(self.username, self.password, self.name)
           
            session.add(query)

            try:
                session.commit()
                
            except Exception as error:
                print('Commit Error')
                print(error)

class sp_userLogin(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.out_result = False
    
    def execute(self):
        with dbSession() as session:
            query = session.query(user_account). \
                filter(user_account.username == self.username, user_account.password == self.password)

            commander = dbCommander(query)
            values = commander.to_list()
            
            if len(values) == 0:
                return 0

            else:
                # update login date
                query[0].login_date = datetime.now()
                try:
                    session.commit()
                except Exception as error:
                    print(error)
                    return 0
                
                with cache.get_pipeline('LoginCount') as pipeline:
                    try:
                        pipeline.set('Login', 1)
                        pipeline.execute()

                    except Exception as error:
                        print(error)

                # Testing
                with cache.get_pipeline('ranking') as pipeline:
                    try:
                        pipeline.zincrby('ranking:arena', 1, str(self.username))
                        pipeline.execute()
                    
                    except Exception as error:
                        print(error)

                return 1
            
class sp_readUserInfo(object):
    def __init__(self, username):
        self.username = username

    def execute(self):
        with dbSession() as session:
            query = session.query(user_account, user_interest) \
                .filter(user_account.username == self.username) \
                .filter(user_account.useridx == user_interest.useridx) \
                .all()
            
            result = {}
            for account, interest in query:
                
                commander = dbCommander(account)
                account_values = commander.parsing()
                commander = dbCommander(interest)
                interest_values = commander.parsing()
                
                result['account'] = account_values
                result['interest'] = interest_values['interest']

            return result
            

