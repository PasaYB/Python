list_array = [[1,2,3],[4,5,6],[7,8,9]]
for item in list_array:
  if item == [1,2,3]:
    print("Hello!")
    continue
  print('item =',item)

dic = {'a':10,'b':20,'c':30,'d':40}
b = dic.get('f',100)
print(b)

dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.pop('c')) 

dic = {'w': 10,'x': 20,'y': 30}

for str,elemens in dic.items():
    if elemens > 10:
        print("Hello!")

a = {'abc': 100, 'cde': 200}
b = a.copy()

print(a is b) 

a = {"orang": 
        {
        "nama": "Budi",
        "umur": "20",
        "alamat": "Jalan"
        }
}

print(a["orang"]["nama"])

keys = ('100','500','300')
y = dict.fromkeys(keys,20)
print(y)

numbers = {10,11,12,15}
if 13 in numbers:
  print("HAI")
elif 14 in numbers:
  print("WHOO")
else:
  print("HELLO")