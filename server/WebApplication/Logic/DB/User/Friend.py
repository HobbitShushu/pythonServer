from WebApplication.Infra.AlchemyDB import dbSession, dbCommander
from WebApplication.Document.Models.User import * 
from WebApplication.Document.Protocol.protocol import *
from application import cache

class sp_getFriendList(object):
    def __init__(self, useridx):
        self.useridx = useridx

    def execute(self):
        friend_list = []
        data = []

        with cache.get_pipeline('sharding', 'Slave') as pipeline:
            try:
                pipeline.hgetall(str(self.useridx) + ':FriendList')
                friends = pipeline.execute()
                
            except Exception as error:
                print(error)

        # get hash data - Dictionary type - items -> (key, value)
        for friend in friends:
            for key, value in friend.items():
                if int(value) == E_Friend_Request_State.accepted:
                    friend_list.append(int(key))

        with dbSession() as session:
            query = session.query(user_account). \
                filter(user_account.useridx.in_(friend_list)). \
                all()

            for account in query:
                commander = dbCommander(account)
                data.append(commander.parsing())
            
        return data

class sp_getFriendRecommend(object):
    def __init__(self, useridx):
        self.useridx = useridx
    
    def execute(self):
        friend_list = []
        data = []
        
        with cache.get_pipeline('sharding', 'Slave') as pipeline:
            try:
                pipeline.hgetall(str(self.useridx) + ':FriendList')
                friends = pipeline.execute()
            
            except Exception as error:
                print(error)
            
            for friend in friends:
                for key, value in friend.items():
                    if int(value) == E_Friend_Request_State.accepted:
                        friend_list.append(int(key))          
        
        with dbSession() as session:
            query = session.query(user_account). \
                filter(user_account.useridx != self.useridx). \
                filter(user_account.useridx.notin_(friend_list))[:50]. \
                all()
            
            for account in query:
                commander = dbCommander(account)
                data.append(commander.parsing())
        
        return data

class sp_requestFriend(object):
    def __init__(self, useridx, targetidx):
        self.useridx = useridx
        self.targetidx = targetidx
        self.out_result = responseResultType.unknown

    def execute(self):    
        with cache.get_pipeline('sharding') as pipeline:
            pipeline.hget(str(self.targetidx) + ':FriendList', self.useridx)
            state = pipeline.execute()
            
            if state == None or state != E_Friend_Request_State.block:
                try:
                    pipeline.hset(str(self.targetidx) + ':FriendList', self.useridx, E_Friend_Request_State.pending)
                    pipeline.execute()
                    self.out_result = responseResultType.success

                except Exception as error:
                    print(error)
            
            else:
                self.out_result = responseResultType.pool_condition
                return
            
            return self.out_result

class sp_responseFriend(object):
    def __init__(self, useridx, targetidx, state):
        self.useridx = useridx
        self.targetidx = targetidx
        self.state = state
    
    def execute(self):
        with cache.get_pipeline('sharding') as pipeline:
            try:
                pipeline.hset(str(self.useridx) + ':FriendList', self.targetidx, self.state)
                pipeline.execute()

                pipeline.hset(str(self.targetidx) + ':FriendList', self.useridx, self.state)
                pipeline.execute()
            except Exception as error:
                print(error)
                return
        
        return
            
