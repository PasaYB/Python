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

# berat = float(input("Masukkan berat anda dalam kg: "))
# tinggi = float(input("Masukkan tinggi anda dalam m: "))

# bmi = (berat/(tinggi ** 2))
# print("BMI Anda =",bmi)

# x = ("apple", "banana", "cherry")
# print(type(x))

# x = 20.5 
# print(type(x))

# x = {"name" : "John", "age" : 36} 
# print(type(x))

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def fungsiHitung (x):
    y = int(input("Masukin angka bulet : "))
    return x * y 
print (fungsiHitung(10))

for i in range(1,41):
     if i % 4 == 0:
          print(i)


          x = 5
y = float(x)
z = str(x)
print("float : ", y)
print("string : ", z)

x = "rasyi@d"
y = "anjau"
print(x + y)

b = "Hello, World!"
print(b[7:13])

txt = "Hello\nWorld!"
print(txt)

txt = "Hello my friends"
x = txt.upper()
print(x)

nama = "Nama saya doni"
print(nama.replace("i", "o"))

x = 5
w = 5
y = 6
z = 6
if x == w and y == z:
    print("Hello World!")