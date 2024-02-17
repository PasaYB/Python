print(1 + 3)    
print("yogaaaaaaaaaa") 
print('hello', 4646)
print('Hello' * 7)

""" Program ini bertujuan untuk
      menampilkan angka 5 
      dengan menggunakan fungsi print """

print(5) # Menampilkan angka 5

print('Yoga' * 7) # Perkalian String (huruf)
print(69 * 7) # Perkalian Numerik (angka)

print(int('10') / 2)
print('I Like ' + str(69))

print(type('100'))

print('Halo nama saya ' + str(20) * 3)
print("hello"[-1])
print("hello"[-5])

teks = "halo, nama saya, budi, yoga"
x = teks.split(", ")
print(x)

a = "HaLo"
b = "halo"

print(a.islower())
print(b.islower())

teks = "Halo yoga, disini yoga bersama dengan yoga semuanya"
x = teks.count("yoga")
print(x)

y = "3"
print(type(y))

print(str(3))

myVar = "John"

MYVAR = "John"
myvar2 = "John"
_my_var = "John"
my_var = "John"
myvar = "John"
myVar = "John"

z = int(3)
print(z)


z = float(3)
print(z)

a = 5 + 2 * 3
print(a)

print( 30 * 2 + 10 - (21  // 5) )

x = ('3' + '5')
print(x)

_y = (3 + 5)
print(_y)

x = pow(3, 3) # 3 pangkat 3
y = pow(3, -3) # 3 pangkat -3

print(x)
print(y)

a = 10
a += 200
a -= 100
a = a * 2

print(a)

# berat = float(input("Masukkan berat anda dalam kg: "))
# tinggi = float(input("Masukkan tinggi anda dalam m: "))

# bmi = (berat/(tinggi ** 2))
# print("BMI Anda =",bmi)

# a = 200
# b = 300
# d = 0

# e = b // a
# c = e ** b * d
# print(c)

# x = int(input("Masukkan integer pertama:" ))
# y = int(input("Masukkan integer kedua:" ))
# s = x + y
# print("Total dari",x,"dan",y,"adalah",s)

# print(8 != 10)

# a = 5
# b = 5.0
# print(a == b)

# a = 'abc'
# b = 'ABC'
# c = 'abC-abc-aBc'

# print( a is b )
# print( a in c )

x = False
y = False
print(x or y)

X = False
Y = True
Z = True

print( X or Y and Z or X )

age = 118 # diberikan kondisi bahwa age = 18

if age < 20: # result dari age < 20 adalah True
    print('youth discount')

a = 4
b = 3

if a < b:
  print("Hello")

elif a > b:
  print("World")

else:
  print("!")

a = "ABC"
b = "abc"
c = "ABC"
d = "CBA"

if a == b:
    print("123")
elif a == c:
    print("456")

if a == b:
    print("1234")
else:
    print("789")

a = "Hello"
b = "Hey"

if a == b:
    print("ABC")
else:
    print("DEF")

a = "ABC"
b = "abc"
c = "ABC"
d = "CBA"

if a == b:
    print("123")
if c == d:
    print("456")
else:
    print("789")

num = -100
if num < 0:
    print(num, 'adalah bilangan negatif. ')
else:
    print(num, 'adalah bukan bilangan negatif ')
    if num % 2 == 0:
        print(num, 'adalah bilangan genap')
    else:
        print(num, 'adalah bilangan ganjil')

a = 50
b = 30

if a > b:
  if a > 40:
    print("WOW")
  else:
    print("HAI")
else:
  print("BYE")

# for i in range(5):
#     print('Welcome to everyone!!')

# for x in range(1,5):
#   print(x)

y = 10

for x in range(1,y):
    if x % 2 == 0:
        if x >= 4:
            print(x)

numbers = [11, 22, 33, 44, 55, 66]
for n in numbers:
    print('n =',n)

#output
n = 11
n = 22
n = 33
n = 44
n = 55
n = 66

numbers = [2,4,6,8,10]
for n in numbers:
    if n < 8:
        print("Hello")
    else:
        print('n =',n)

i = 0 # initial value
while i < 5: # kode didalam block akan dieksekusi selama kondisi True
    print('Wlecome to everyone!!')
    i += 1

i = 3
while i < 5:
    print(i)
    i += 1

# i = 10
# while i > 4:
#      if i == 5:
#           i = 10
#      i -= 1
#      print(i)

a = ['apple','banana','orange']
print(id(a))

a.append('grapes')
print(id(a))
print(a)

e = 'Halo, semua!'
print(id(e))
e = 'Halo, Apa kabar?'
print(id(e))
print(e)

List4 = list(range(1,10))
print(List4)

n_list = [11,22,33,44,55,66]
print(n_list)
print(len(n_list))

a = [1,2,3,4,5]

print(a[0])

a = (1,2,3,4,5)
a[1] = 100
print(a)