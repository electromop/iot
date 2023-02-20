from dataclasses import dataclass
from typing import Any

@dataclass
class roomData:
    conds: Any
    
    def module(self, m):
        return self.globals()[m]
    def 

class rooms():
    def roomCreate(string):
        exec("%s = %d" % (string,0))
        globals()[string] = roomData
        print('Комната добавлена!')

    def moduleCreate(roomname, modulename):
        exec("%s = %d" % (roomname,0))
    
print('1. Новый класс')
print('2. Новый модуль')
print('3. Изменить состояние модуля')
print('4. Выйти')

while True:
    op = int(input())
    if op == 1:
        room_name = str(input())
        rooms.roomCreate(room_name)
    elif op == 4:
        break

print(globals())
