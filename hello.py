spam = ['apples', 'bananas', 'tofu', 'cats']
spam=[1,2,3,4,5,6]
for i in range(len(spam)):
    if i == (len(spam)-1):
        print(' and ' + str(spam[i]), end='')
    elif i == (len(spam)-2):
        print(str(spam[i]), end='')
    else:
        print(str(spam[i]) + ', ', end='')

