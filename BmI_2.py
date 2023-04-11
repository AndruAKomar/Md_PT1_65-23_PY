while True:
    l = input('Vvedite rost v metrah: ',)
    m = input('Vvedite ves v kg: ',)
    p = input('Vvedite vash pol - (M/W): ',)
    v = input('Vvedite vash vozrost: ',)
    if  not l or not m or not p or not v: # выход из цикла в случае нулевого значения любого из параметров 
        print('exit')
        break
    else:
        bmi = round(float(m)/float(l)**2)
        if bmi >=50 or bmi <=20:
            print('\nVash BMI za predelami diapozona \n20==============================50\n')
        else:
            print(f'\nIndex massi tela: {bmi} \nVosrost: {int(v)} \nPol: {p}')
            print(''.join(['20','='*(bmi-21),'|','='*(49-bmi),'50\n'])) 
            if bmi > 20 and bmi < 25:
                if int(v) > 40:
                    if p == 'm':
                        print('Normal ves, men\n')
                    else:
                        print('Normal ves, women\n')
                else:
                    if p == 'm':
                        print('Normal ves, men. Good job!\n')
                    else:
                        print('Normal ves, baby. Good job!\n')
            elif  bmi >= 25 and bmi <35:
                if int(v) > 40:
                    if p == 'm':
                        print('Izbytochni ves, men. Noting hotdog\n')
                    else:
                        print('Izbytochni ves, women. Noting hotdog\n')
                else:
                    if p == 'm':
                        print('Izbytochni ves, men. Zadumaisa\n')
                    else:
                        print('Izbytochni ves, baby. Zadumaisa\n') 
            elif  bmi >= 35 and bmi < 50:
                if int(v) > 40:
                    if p == 'm':
                        print('Ogirenie , men. Allarm!!\n')
                    else:
                        print('Ogirenie , women.  Allarm!!\n')
                else:
                    if p == 'm':
                        print('Ogirenie , men. Go run!\n')
                    else:
                        print('Ogirenie , baby. Go run!') 
          
        
   
