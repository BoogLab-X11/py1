def plusone(myvar):
    myvar += 1
    return myvar
testvar=42
name=input("Name?")
test=(plusone(41))
try:
    test / 0
except:
    print('bang')
print('whatevs')