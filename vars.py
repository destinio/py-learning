# x = 1

# name, age = ('destin', 37)

# s = 2 + 2

# print(s)
# print(type(name))
# print(type(s))

# cast = str(4)
# print(cast)
# print(type(cast))

name = 'Destin'
age = 36

# print('hello my name is ' + name)

# print('hello my name is {name} and I am {age}'.format(name=name, age=age))

print(f'hello my name is {name} and I am {age}')

# string methods

message = 'This is a message'

print(message.capitalize())
print(message.upper())
print(len(message))
print(message.split())

def sayHello(name):
  print(f'Hello, {name}')
  
sayHello('destin')

# LOOPS

people = ['destin', 'stacy']

for p in people:
  print(f'current person {p}')
  
for i in range(len(people)):
  print(f'current i {i}')
  
it = 5

if it < 10:
  print("Hey it works")
elif it is 11:
  print("it's 11")
else:
  print("you good")
  
x = lambda num : num * 2

print(x(2))


import json

# converting json string

dataString = '{ "name": "destin" }'

j = json.loads(dataString)

print(j)

# python object

po = {
  "name": "destin"
}

j2 = json.dumps(po)

print(j2)
