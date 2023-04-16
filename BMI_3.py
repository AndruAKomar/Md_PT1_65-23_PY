baza = {
     'Vasya':{'ves' : 80, 'rost': 1.85, 'pol' : 'men'}, 
      'Petra' : {'ves' : 120, 'rost': 1.65, 'pol' : 'women'}
      }

def menu(): #print menu
      print('\tМногопользовательский калькулятор БМИ: \nA.Вывести список пользователей \nВ.Посмотреть инфо о пользователе (рост, вес, шкала БМИ)\nC.Изменить данные о пользователе \nD.Удалить выбранного пользователя\nE.Добавить пользователя \nF.Выход')

def repiat_add_user(user, v = 0, r= 0, p= 'men'): # reoiat and add user
     baza[user] = {'ves' : v, 'rost': r, 'pol' : p}
     print(baza.get(user))

def delete_user(user): # delete user
     del(baza[user])
     print(f'{user} удален') 


menu() # begin 
point = input('\tВыбери пункт меню -> ',)

while point != 'F':
      if point == "A": # выбор первого пункта меню - А
          print('Список пользователей:\n', baza.keys())
          menu()
          
      if point == "B":
          user = input('\tВыбери пользователя -> ',)
          print(baza.get(user, 'Нет такого'))
          menu()
          
      if point == "C":
           user = input('\tВыбери пользователя для изменения-> ',)
           while baza.get(user) == None:
               print(f'{user} - Нет такого')
               user = input('\tВыбери пользователя для изменения-> ',)
           print(baza.get(user))
           v = input('\tВес ?-> ',)
           r = input('\tРост ?-> ',)
           p = input('\tПол (men/women) ?-> ',)
           repiat_add_user(user,v,r,p)
           menu()
      
      if point == "D":
           user = input('\tВыбери пользователя для удаления -> ',)
           while baza.get(user) == None:
               print(f'{user} - Нет такого')
               user = input('\tВыбери пользователя для удаления -> ',)
           delete_user(user)
           menu()

      if point == "E":
           user = input('\tВыбери пользователя для добавления -> ',)
           while baza.get(user) != None:
               print(f'{user} - Такой уже есть')
               user = input('\tВыбери пользователя для добавления -> ',)
           v = input('\tВес ?-> ',)
           r = input('\tРост ?-> ',)
           p = input('\tПол (men/women) ?-> ',)
           repiat_add_user(user,v,r,p)
           menu()

      point = input('\tВыбери пункт меню -> ',)
     