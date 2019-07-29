from WebApplication.Infra.AlchemyDB import dbSession, dbCommander
from WebApplication.Document.Models.User import * 
from application import cache

class sp_takeEquipment(object):
    def __init__(self, useridx, characteridx, position, equipmentidx):
        self.useridx = useridx
        self.characteridx = characteridx
        self.position = position
        self.equipmentidx = equipmentidx

    def execute(self):
        with dbSession() as session:
            query = session.query(user_character, user_equipment). \
                filter(user_character.userdix == self.useridx). \
                filter(user_character.characteridx == self.characteridx). \
                filter(user_equipment.equipmentidx == self.equipmentidx). \
                all()
            
            if(self.position == 0):
                query[0].soulWeapon = query[1].equipmentidx
            elif(self.position == 1):
                query[0].soulArmor = query[1].equipmentidx
            elif(self.position == 2):
                query[0].soulTreasure = query[1].equipmentidx
            else:
                return
            
            try:
                session.commit()
            
            except Exception as error:
                print(error)
        
            return
            
class sp_reinforcementEquipment(object):
    def __init__(self, useridx, equipmentidx, materials):
        self.useridx = useridx
        self.equipmentidx = equipmentidx
        self.materials = materials

    def execute(self):
        # convert to list
        # createto -
        equipment_list = []
        with dbSession() as session:
            #해당 유저가 재료로 사용할 장비를 가지고 있는지 여부 확인
            query = session.query(user_equipment). \
                filter(user_equipment.useridx == self.useridx). \
                filter(user_equipment.equipmentidx.in_(equipment_list)). \
                all()

                #commander = dbCommander(equipment)
                #equipment_info.append(commander.parsing())
            

class sp_readEquipment(object):
    def __init__(self, useridx, characteridx):
        self.useridx = useridx
        self.characteridx = characteridx

    def execute(self):
        return
    
    def executeOnSession(self, session):
        query = session.query(user_equipment). \
            filter(user_equipment.useridx == self.useridx). \
            filter(user_equipment.characteridx == self.characteridx). \
            all()
        
        equipment_list = []
        for equipment in query:
            commander = dbCommander(equipment)
            equipment_list.append(commander.parsing())

        return equipment_list