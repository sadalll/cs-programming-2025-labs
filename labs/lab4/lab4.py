a=int(input('Введите температуру:'))
if a>=20: print('Кондиционер выключен')
if a<20: print('Кондиционер включен')


b=int(input('Введите номер месяца:'))
if b==1 or b==2 or b==12: print('зима')
elif b==3 or b==4 or b==5: print('весна')
elif b==6 or b==7 or b==8: print('лето ')
elif b==9 or b==10 or b==11: print('осень')
else:
    print('oh no...((((')


c=int(input('Введите возраст собаки (в годах) '))
d=0
if c<1:
    print('Ошибка:возраст собаки длжен быть не меньше 1')
    c=int(input())
elif c > 22:
    print("Ошибка: слишком большой возраст")
else:
    if c<= 2:
        d= c * 10.5
    else:
        d= 21 + (c-2) * 4
        print("Возраст собаки в человеческих годах:", d)


n=int(input())
if (n%10)%2==0 and sum(map(int,str(n)))%3==0: print('делиться на 6')
else: print('не делиться на 6')


a=input()
if len(a)<9:
    print('слишком мало символов')
elif not any(i.isupper() for i in a):
  print('пароль ненадежный: отсутствуют заглавные буквы латиницы')
elif not any(i.islower() for i in a):
    print('пароль ненадежный: отсутствуют строчные буквы латиницы')
elif not any(char in '0123456789' for char  in a):
    print('пароль ненадежный:отсутствуют числа')
elif not any (char in '!@#$%^&*()_-+|~' for char  in a):
    print('пароль ненадежный: отсутствуют специальные символы')
else:
    print('пароль надежный')


year=int(input('введите год: '))
if year%4==0:
    if year%100!=0 or year%400==0:
        print("високосный год")
    else:
        print("не високосный год")
else:
    print("не високосный год")


w=input('Введите три числа: ')
x,y,z=map(int,w.split())
mn=100
if x<mn and x<y and x<z: print(x)
if y<mn and y<x and y<z: print(y)
if z<mn and z<y and z<x: print(z)


s=int(input('Введите сумму покупки: '))
if s<1000:
    print('Ваша скидка: 0% ')
    print('К оплате: ',s)
if 1000<=s<5000:
    print('Ваша скидка: 5% ')
    print('К оплате: ',s-((s*5)/100))
if 5000<=s<=10000:
    print('Ваша скидка: 10% ')
    print('К оплате: ',s-((s*10)/100))
if s>10000:
    print('Ваша скидка: 15% ')
    print('К оплате: ',s-((s*15)/100))


v=int(input('Введите час (0–23): '))
if v in (0,1,2,3,4,5): print('Сейчас Ночь')
if v in (6,7,8,9,10,11): print('Сейчас Утро')
if v in (12,13,14,15,16,17): print('Сейчас День')
if v in (18,19,20,21,22,23): print('Сейчас Вечер')


h=int(input('введите число: '))
def f(n):
    d=2
    while n%d!=0:
        d+=1
    return d==n
if f(h)==True:
    print(f'{h}-простое число')
else:
    print(f'{h}-составное число')