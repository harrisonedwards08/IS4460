# here's a comment
print("hello world")





balance = 50
if balance < 150:
  money = 2000
  balance += money

print (balance)



balance = 50
if balance > 150:
  money = 2000
  balance += money
else:
  print ("balance is les than 150")

print (f"balance is {balance}")


fuel = 10
print ("fuel tank is good" if fuel >= 1 else "not enough")


fuel = 15
while fuel > 1:
  print ("We got the juice")
  fuel -=1



movies = ["BL", "Grand Budapest", "Heat"]
for movie in movies:
  print (f"movie : {movie}")



blah = 45
Blah = 12
print(blah)
print(Blah)
blah+= Blah
print(blah)

print(type(blah))


aye = 5
bye = 6
print (aye+bye)



this = "hello "
this2 = "my name is inigo montoya "
this3 = "you kill my father "

print(this + this2 + this3 + "prepare to die")



print(5==6)
print (int(5==5))



def subtract_numbers (a,b):
  output = a-b
  return output


c = 10
d = 15

print(subtract_numbers(c,d))

print(subtract_numbers(a=7,b=3))



name = "Harry"

def say_getouttahere ():
  name = "Terry"
  print("Getouttahere " + name)

say_getouttahere()



print(f"boolean A: {35>90}")
print(f"boolean B: {45==45}")



print ("one is equal to 2: ", int(1==2))

grade = 'a'

if grade == 'd' or grade == 'f':
    print("Try better")
elif grade == 'c':
    print("Close but no cigar")
elif grade == 'b':
    print("Good enough for government work")
else:
    print("You made it")
