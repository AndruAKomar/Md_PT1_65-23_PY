baza = {
     'Vasya':{'ves' : 80, 'rost': 1.85, 'pol' : 'men'}, 
      'Petra' : {'ves' : 120, 'rost': 1.65, 'pol' : 'women'}
      }

def menu(): #print menu
      print('\n\tМногопользовательский калькулятор БМИ: \nA.Вывести список пользователей \nВ.Посмотреть инфо о пользователе (рост, вес, шкала БМИ)\nC.Изменить данные о пользователе \nD.Удалить выбранного пользователя\nE.Добавить пользователя \nF.Выход')

def change_add_user(user, v = 0, r= 0, p= 'men'): # change and add user
     baza[user] = {'ves' : v, 'rost': r, 'pol' : p}
     print(f'{user}:', baza.get(user))

def delete_user(user): # delete user
     del(baza[user])
     print(f'{user} удален') 

def clear_term():
     import os
     os.system('CLS')


menu() # begin 
point = input('\tВыбери пункт меню -> ',)

while point != 'F':
      
      if point == "A": # выбор первого пункта меню - А
          clear_term()
          print('Список пользователей:\n', baza.keys())
          menu()
          
      if point == "B":
          clear_term()
          user = input('\tВыбери пользователя -> ',)
          while baza.get(user) == None:
               print(f'{user} - Нет такого')
               user = input('\tВыбери пользователя -> ',)
          print(f'{user}:', baza.get(user))
          menu()
          
      if point == "C":
           clear_term()
           user = input('\tВыбери пользователя для изменения-> ',)
           while baza.get(user) == None:
               print(f'{user} - Нет такого')
               user = input('\tВыбери пользователя для изменения-> ',)
           v = input('\tВес ?-> ',)
           r = input('\tРост ?-> ',)
           p = input('\tПол (men/women) ?-> ',)
           change_add_user(user,v,r,p)
           menu()
      
      if point == "D":
           clear_term()
           user = input('\tВыбери пользователя для удаления -> ',)
           while baza.get(user) == None:
               print(f'{user} - Нет такого')
               user = input('\tВыбери пользователя для удаления -> ',)
           delete_user(user)
           menu()

      if point == "E":
           clear_term()
           user = input('\tВыбери пользователя для добавления -> ',)
           while baza.get(user) != None:
               print(f'{user} - Такой уже есть')
               user = input('\tВыбери пользователя для добавления -> ',)
           v = input('\tВес ?-> ',)
           r = input('\tРост ?-> ',)
           p = input('\tПол (men/women) ?-> ',)
           change_add_user(user,v,r,p)
           menu()

      point = input('\tВыбери пункт  меню -> ',)
     