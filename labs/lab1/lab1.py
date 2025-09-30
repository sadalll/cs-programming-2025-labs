x=12
c=1.2
v='qq'
n=True

name='Алёна'
age=17
print(name,age)

q=342
w=56.2
e='43'
r=w+int(e)+q
print(r)

a=3
b=8
m=(a+4*b)*(a-3*b)+a**2
print(m)

o=int(input())
u=int(input())
k=o*u
i=(o+u)*2
print('S=',k,'P=',i)



print("*  *  *")
print(" *****")
print("  * *  ")



f=3
j=2
print(f+j,f-j,f*j,f/j,f//j,f%j,f**j)
print(f==j,f!=j,f>j,f<j,f>=j,f<=j)
print(f'Меня зовут {name}, мне {age} лет')


s1='Съешь еще '
s2='этих мягких'
s3=' французских булок'
s4=', да'
s5=' выпей чаю'
print(s1+s2+s3+s4+s5)


print('Нет!Дa!'*4)

xxx=input('введите 3 числа через запятые')
x1,x2,x3=map(int,xxx.split(','))
itog=(x1+x3)//x2
print('Результат вычисления:',itog)

v=input('Введите слово,содержащее не менее 10 символов')
print(v[:4])
print(v[-2:])
print(v[3:8])
print(v[::-1])