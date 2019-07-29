from WebApplication.Infra.AlchemyDB import dbSession, dbCommander
from WebApplication.Document.Models.User import * 
from application import cache

class sp_readCharacters(object):
    def __init__(self, useridx):
        self.useridx = useridx
    
    def execute(self):
        with dbSession() as session:
            query = session.query(user_character). \
                filter(user_character.useridx == self.useridx). \
                all()
            
            result = []
            for character in query:
                commander = dbCommander(character)
                result.append(commander.parsing())

            return result

# character idx -> 고유 값 가져야 합니다
class sp_readCharacter(object):
    def __init__(self, useridx, characteridx):
        self.useridx = useridx
        self.characteridx = characteridx
    
    def execute(self):
        with dbSession() as session:
            query = session.query(user_character). \
                filter(user_character.useridx == self.useridx). \
                filter(user_character == self.characteridx). \
                all()

            result = []
            for character in query:
                commander = dbCommander(character)
                result.append(commander.parsing())
            
            from WebApplication.Logic.DB.User.Equipment import sp_readEquipment
            sp = sp_readEquipment(self.useridx, self.characteridx)
            equipment_list = sp.executeOnSession(session)

            return result, equipment_list