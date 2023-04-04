l=float(input('Vvedite rost v metrah: ',))
m=float(input('Vvedite ves v kg: ',))
bmi=round(m/l**2)
list=['20','='*(bmi-21),'|','='*(49-bmi),'50']
print('Index massi tela: ', bmi)
print(''.join(list))
