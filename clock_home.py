import datetime
import time
import os
import my_modul

while True:
    time_now = list(datetime.datetime.now().strftime("%H%M%S"))
    #print(time_now)
      
    def lines_print(H_,_H,M_,_M,S_,_S):
        if int(time_now[5]) % 2 == 0: # по последней секунде определяю чет/нечет для принта переменной через 1 секунду
            point_print = '⬜'
        else:
            point_print = '  '
        print(my_modul.print_first_line[H_]+ ' '+ my_modul.print_first_line[_H]+ '      '+ my_modul.print_first_line[M_]+ ' '+ my_modul.print_first_line[_M]+ '      '+ my_modul.print_first_line[S_]+ ' '+ my_modul.print_first_line[_S])
        print(my_modul.print_second_line[H_]+ ' '+ my_modul.print_second_line[_H]+ f'  {point_print}  '+ my_modul.print_second_line[M_]+ ' '+ my_modul.print_second_line[_M]+ f'  {point_print}  '+ my_modul.print_second_line[S_]+ ' '+ my_modul.print_second_line[_S])
        print(my_modul.print_third_line[H_]+ ' '+ my_modul.print_third_line[_H]+ '      '+ my_modul.print_third_line[M_]+ ' '+ my_modul.print_third_line[_M]+ '      '+ my_modul.print_third_line[S_]+ ' '+ my_modul.print_third_line[_S])
        print(my_modul.print_fourth_line[H_]+ ' '+ my_modul.print_fourth_line[_H]+ f'  {point_print}  '+ my_modul.print_fourth_line[M_]+ ' '+ my_modul.print_fourth_line[_M]+ f'  {point_print}  '+ my_modul.print_fourth_line[S_]+ ' '+ my_modul.print_fourth_line[_S])
        print(my_modul.print_fifth_line[H_]+ ' '+ my_modul.print_fifth_line[_H]+ '      '+ my_modul.print_fifth_line[M_]+ ' '+ my_modul.print_fifth_line[_M]+ '      '+ my_modul.print_fifth_line[S_]+ ' '+ my_modul.print_fifth_line[_S])
       

    lines_print(time_now[0],time_now[1],time_now[2],time_now[3],time_now[4],time_now[5])
    time.sleep(0.2)
    os.system('CLS')
