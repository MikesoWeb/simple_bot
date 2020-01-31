# Бот спрашивает имя собеседника
# Бот говорит о погоде
# Бот задает вопросы
# Бот реагирует на сообщения пользователя

from random import choices
from time import sleep

rand_users = choices(['Андрей Сухов', "Васька Пупкин", 'Михаил Державин'])

print(f'{rand_users[0]}: --> Привет. Давай знакомиться')
sleep(1.5) 
print(f'{rand_users[0]}: --> Меня зовут {rand_users[0]}, я из Таллина мне 17 лет.')
sleep(2)
name = input(f'{rand_users[0]}: --> Как тебя зовут? ')
sleep(2)
city = input(f'{rand_users[0]}: --> Из какого ты города, {name}? ')
sleep(2)
print(f'{rand_users[0]}: --> В городе {city} сегодня хорошая погода? ')
pogoda = input()
if  'солнечно' in pogoda:
  sleep(3)
  print(f'{rand_users[0]}: Обожаю солнце! Я бы пошел купаться, ведь лето же.')
if 'пасмурно' in pogoda:
  sleep(3)
  print(f'{rand_users[0]}: Некоторые любят такую погоду. Тёплый плед и горячий чай...у камина...')
else:
  sleep(2)
  print(f'{rand_users[0]}: Чтож! Одни любят когда солнечно,другие когда пасмурно. Всем не угодишь =))')
sleep(1)
print(f'{rand_users[0]}: Ой, папа приехал....мне пора..')
sleep(2)
print(f'{rand_users[0]}: До встречи {name}, всего тебе доброго =)')
