#Задание 1_1 Игра в конфеты Человек-Человек

from random import randint as RI
cls = lambda: print('\n'*15)
cls()
print("Игра в 28 конфет Человек-Человек")
GOAL = 28
candy = RI(58,113)
active_player = RI(1,2)
count = active_player
print (f"На столе лежит {candy} конфет(а)")
print (f"Первый ход делает  игрок №{active_player}")
while candy > GOAL:
    if count % 2 ==0:
        active_player = 2
    else:
       active_player = 1
    step = int(input(f"Игрок № {active_player} забирает: "))
    candy-=step
    print (f"На столе осталося {candy} конфет(ы)")
    count+=1
if count % 2 == 0:
    active_player = 2
else:
    active_player = 1
print (f"Все конфеты достаются игроку № {active_player}") 
print()
input("Нажмите любую кнопку для запуска следующей программы \n")
cls()
#Задание 1_2 Игра в конфеты Человек-бот

print("Игра в 28 конфет Человек- Бот")
GOAL = 28
candy = RI(58,113)
active_player = RI(1,2)
count = active_player
who_acts = {1:"Игрок",2:"Бот"} 

print (f"На столе лежит {candy} конфет(а,ы)")
print (f"Первый ход делает {who_acts [active_player]}")
while candy > GOAL:
    if count % 2 ==0:
        active_player = 2
    else:
       active_player = 1
    if active_player == 2:
        step = RI(1,28)
        print(f"Бот забирает {step} конфет(а,ы)")
    else:
        step = int(input(f"Игрок забирает: "))
    candy-=step
    print (f"На столе осталося {candy} конфет(а,ы)")
    count+=1
if count % 2 == 0:
   print (f"Все конфеты достаются Боту")
else:
    print (f"Все конфеты достаются Игроку")

print()
input("Нажмите любую кнопку для запуска следующей программы \n")
cls()

#Задание 1_3 Игра в конфеты Человек-умный бот

print("Игра в 28 конфет Человек-Умный Бот")
GOAL = 28
candy = RI(58,113)
active_player = RI(1,2)
count = active_player
who_acts = {1:"Игрок",2:"Бот"} 
print (f"На столе лежит {candy} конфет(а,ы)")
print (f"Первый ход делает {who_acts [active_player]}")
while candy > GOAL:
    if count % 2 ==0:
        active_player = 2
    else:
       active_player = 1
    if active_player == 2:
        if candy  > 2*GOAL:
            step = GOAL
        elif candy == GOAL+1:
            step = 1
        elif candy <= 2*GOAL:
            step = (candy-GOAL)-1
        print(f"Бот забирает {step} конфет(а,ы)")
    else:
        step = int(input(f"Игрок забирает: "))
    candy-=step
    print (f"На столе осталося {candy} конфет(а,ы)")
    count+=1
if count % 2 == 0:
   print (f"Все конфеты достаются Боту")
else:
    print (f"Все конфеты достаются Игроку") 

print()
input("Нажмите любую кнопку для запуска следующей программы \n")
cls()

#Задание 2 Игра в крестики-нолики

N = 8
mark = [1,2]
field = [1,2,3,4,5,6,7,8,9]
active_player = RI(1,2)
count = active_player
vacant_cells = {0,1,2,3,4,5,6,7,8}
def print_field(f):
    print ('-------------') 
    print(f"| {f[0]} | {f[1]} | {f[2]} |")
    print ('-------------')
    print(f"| {f[3]} | {f[4]} | {f[5]} |")
    print ('-------------')
    print(f"| {f[6]} | {f[7]} | {f[8]} |")
    print ('-------------')
     
def check_field(f):
    check_flag= 1
    cnt = 0
    for i in range (N+1):
        if (f[i] == 'X') or (f[i] == 'O'):
            cnt+=1
    if cnt == N+1:
       check_flag = 0 
       print('ИГРА ЗАВЕРШЕНА! Результат ничейный')
    return check_flag
def check_win (f,sym):
    check_flag = "not win"
    if ((f[0] == sym) and (f[1] == sym) and (f[2] == sym) or
        (f[3] == sym) and (f[4] == sym) and (f[5] == sym) or
        (f[6] == sym) and (f[7] == sym) and (f[8] == sym) or
        (f[0] == sym) and (f[3] == sym) and (f[6] == sym) or
        (f[1] == sym) and (f[4] == sym) and (f[7] == sym) or
        (f[2] == sym) and (f[5] == sym) and (f[8] == sym) or
        (f[0] == sym) and (f[4] == sym) and (f[8] == sym) or
        (f[6] == sym) and (f[4] == sym) and (f[2] == sym)):
        check_flag = "win"
    return check_flag

print("Игра в крестики-нолики начинается! Игровое поле:")
print_field(field)
print (f"Первый ход (крестики) делает игрок № {active_player}")
if active_player == 2:
    mark[0] = 'O'
    mark[1]= 'X'
else:
    mark[0] = 'X'
    mark[1] = 'O'
    
while (check_field(field) == 1):
    if count % 2 == 0:
       active_player = 2
    else:
       active_player = 1
    cell = int(input (f"Игрок № {active_player} делает ход на свободную клетку "))-1
    if cell in vacant_cells:
            field[cell] = mark[active_player-1]
            vacant_cells.discard(cell)
            cls()   
    else:
        print ("ИГРА ЗАВЕРШЕНА! Данная клетка занята или некорректный ввод")
        break
    print (f"Игровое поле после хода игрока № {active_player}")
    print_field(field)
    if (check_win(field,mark[active_player-1])=='win'):
        print(f"ИГРА ЗАВЕРШЕНА! Победу одержал игрок № {active_player}")
        break
    count+=1

print()
input("Нажмите любую кнопку для запуска следующей программы \n")
cls()

#Задание 3 Сжимание и расжимание данных
cls()
print ("Алгоритм сжатия и восстановления данных")
file_name = 'ToCompress.txt'
mode = int(input("Введите 1 для режима сжатия и 2 для восстановления данных:  "))
if mode == 1:
    file_name = 'ToCompress.txt'
    with open (file_name) as file_object:
             line = file_object.read()
    compr_a = ''
    compr_b = ''
    compr_c = ''
    if line.count('a') != 0:
           compr_a = str(line.count('a'))+'a'
    if line.count('b') != 0:
           compr_b = str(line.count('b'))+'b'
    if line.count('c') != 0:
           compr_c = str(line.count('c'))+'c'
    res = compr_a+compr_b+compr_c
    print (f"Результат сжатия строки {line}:{res}")
else:
    def Merge_It (count, symb):
        line1 = ""
        for i in range (count):
            line1+=symb
        return line1
    file_name = 'ToDecompress.txt'
    with open (file_name) as file_object:
             line = file_object.read()
    res = ''
    print(f'Исходная сжатая строка, которая будет восстановлена {line}')
    if 'a' in line:
        line_a = line.split('a')
        line = line_a[1]
        res += Merge_It(int(line_a[0]),'a')
    if 'b' in line:
        line_a = line.split('b')
        line = line_a[1]
        res += Merge_It(int(line_a[0]),'b')
    if 'c' in line:
        line_a = line.split('c')
        line = line_a[1]
        res += Merge_It(int(line_a[0]) ,'c')
    print (f"Результат восстановления строки: {res}")
print()



