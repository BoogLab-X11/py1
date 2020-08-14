def plusone(myvar):
    myvar += 1
    return myvar
test=(plusone(41))
try:
    test / 0
except:
    print('bang')
print('whatevs')