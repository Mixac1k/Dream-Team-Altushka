all_podezd = int(input('all_podezd >>> '))
floors = int(input('floors >>> '))
kv_on_floor = int(input('kv_on_floor >>> '))
num_kv = int(input('num_kv >>> '))


kv_v_podezde = floors * kv_on_floor      #Ищем количество квартир в одном подъезде
nice_podezd = num_kv // kv_v_podezde + 1 #Деление нацело номера искомой квартиры на кол-во квартир в подъезде и прибавление единицы помогает найти нужный подъезд

nice_floor = (num_kv - 1) // kv_on_floor #Делаем сдвиг номера квартиры на -1, дабы исключить проблему на чётных значениях, присваиваем порядковый номер этажа
nice_floor %= floors                     #Остаток от деления на кол-во этажей (ограничение одного подъезда) вычисляет необходимый этаж в подъезде
nice_floor += 1                          #Выравниваем значение нужного этажа

print('Квартира', num_kv, 'находится в', nice_podezd, 'подъезде на', nice_floor, 'этаже')
