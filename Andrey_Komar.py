text='Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!'
print('Шаг1 - Количество символов - ', len(text))

print('Шаг2 - Развернуть строку - ',text[::-1])

print('Шаг3 - Kаждое слово с большой буквы -',text.title())

print('Шаг4 - Весь текст прописными буквами -',text.upper())

print('Шаг5 - Число вхождений "нд", "ам", "о" в строку -', text.count('нд'), text.count('ам'), text.count('о'), ' раз')

print('Шаг6 - Собственное упражнение.Собака - ',text.replace("собака",chr(64),1))
print('Шаг6 - Собственное упражнение. Количество слов в строке - ',len(text.split()))

sp_text=text.split()
print('Шаг7 - Развернуть предложение -', ' '.join(sp_text[::-1]))

print('Шаг8 - В консоль исходную строку- ', text)
print ('test')

New Branch Hello


