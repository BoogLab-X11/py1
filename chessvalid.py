game={'3c': 'bking', '6c': 'wqueen', '2g': 'bbishop' , '3g': 'bbishop', '4g': 'bbishop' , '5h': 'bqueen',
'3e': 'wking', '9h': 'bqueen', '4c': 'bqueen', '3c': 'pinkbishop'}

pieces={'wking':1,'wqueen':1,'wrook':2,'wbishop':2,'wknight':2,'wpawn':8,'bking':1,'bqueen':1,
'brook':2,'bbishop':2,'bknight':2,'bpawn':8}

#create board
board=[]
col=['h','g','f','e','d','c','b','a']
for row in range(1,9):
    for column in col:
        board.append(str(row)+str(column))

#check squares
for square in game:
    if square not in board:
        print(str(square) + ' is not a legal square')

#check pieces
for piece in game.values():
    if piece not in pieces:
        print(str(piece) + ' is not a legal piece')

#count pieces
count = 0
countDict={}
for piece in game.values():
    if piece in countDict:
        countDict[piece] += 1
        count += 1
    else:
        countDict.setdefault(piece,1)

#check count for legality
result=''
endResult=[]
for piece in game.values():
    if piece in pieces:
        if countDict[piece] > pieces[piece]:
            result='Too many ' + str(piece)
            if result not in endResult:
                endResult.append(result)
print(str(endResult))
