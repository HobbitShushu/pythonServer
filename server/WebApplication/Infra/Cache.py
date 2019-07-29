import redis, random

class RedisController(object):
    def __init__(self, **kwargs):
        self.masterHost = kwargs['masterHost']

        self.password = None

        if 'password' in kwargs:
            self.password = kwargs['password']

        self.slaveHosts = list()
        for host in kwargs['slaveHosts']:
            self.slaveHosts.append(host)

        self.slavePorts = list()
        for port in kwargs['slavePorts']:
            self.slavePorts.append(port)

        self.tables = {'LoginCount':0, 'ranking':1, 'sharding':2}

        self.masterConnectionPools = {}
        self.slaveConnectionPools  = {}

        for key in self.tables.keys():
            self.masterConnectionPools[key] = redis.ConnectionPool(host = self.masterHost, port = 7000, password = self.password, db = self.tables[key], decode_responses=True)

            for i in range(0, len(self.slaveHosts)):
                if self.slaveConnectionPools.get(key) == None:
                    self.slaveConnectionPools[key] = list()

                self.slaveConnectionPools[key].append(redis.ConnectionPool(host = self.slaveHosts[i], port = self.slavePorts[i], password = self.password, db = self.tables[key], decode_responses=True))
    
    def GetConnectionPool(self, tableName = None, redisType = 'Master'):
        if redisType == 'Master':
            if self.masterConnectionPools.get(tableName) == None:
                return None

            return self.masterConnectionPools[tableName]               
        else:
            if self.slaveConnectionPools.get(tableName) == None:
                return None

            return random.choice(self.slaveConnectionPools[tableName])

    def get_pipeline(self, tableName = None, redisType = 'Master'):
        if tableName is None:
            return None
        
        connectionPool = self.GetConnectionPool(tableName, redisType)
        if connectionPool is None:
            return None

        cache = redis.StrictRedis(connection_pool=connectionPool)
        # transaction - Multi/Exec
        return cache.pipeline(transaction=False)
