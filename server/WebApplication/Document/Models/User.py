from sqlalchemy import Column, Integer, String, SMALLINT, DATETIME, JSON
from WebApplication.Infra.AlchemyDB import Base

from datetime import datetime
import json

class user_account(Base):
    __tablename__ = 'user_account'
    #__table_args__ = {'mysql_collate': 'utf8_general_ci'}
    useridx = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(45), unique=True)
    password = Column(String(45))
    name = Column(String(10), unique=True)
    regist_date = Column(DATETIME)
    login_date = Column(DATETIME)

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name
        self.regist_date = datetime.now()
        self.login_date = datetime.now()
        
class user_interest(Base):
    __tablename__ = 'user_interest'
    useridx = Column(Integer, primary_key=True)
    interest = Column(JSON)

    def __init__(self, useridx, interest):
        self.useridx = useridx
        self.interest = interest

class user_character(Base):
    __tablename__ = 'user_character'
    useridx = Column(Integer, primary_key=True)
    characteridx = Column(Integer, primary_key=True)
    grade = Column(SMALLINT)
    level = Column(SMALLINT)
    exp = Column(Integer)
    awaken = Column(SMALLINT)

    soulWeapon = Column(Integer)
    soulArmor = Column(Integer)
    soulTreasure = Column(Integer)
    
    def __init__(self, useridx, characteridx, grade, level, exp, awaken, soulWeapon, soulArmor, soulTreasure):
        self.useridx = useridx
        self.characteridx = characteridx
        self.grade = grade
        self.level = level
        self.exp = exp
        self.awaken = awaken
        
        self.soulWeapon = soulWeapon
        self.soulArmor = soulArmor
        self.soulTreasure = soulTreasure

class user_equipment(Base):
    __tablename__ = 'user_equipment'
    useridx = Column(Integer, primary_key=True)
    characteridx = Column(Integer, primary_key=True)
    equipmentidx = Column(Integer, primary_key=True)
    level = Column(SMALLINT)
    exp = Column(Integer)

    def __init__(self, useridx, characteridx, equipmentidx, level, exp):
        self.useridx = useridx
        self.characteridx = characteridx
        self.equipmentidx = equipmentidx
        self.level = level
        self.exp = exp