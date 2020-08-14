message = 'It was a bright cold day in April, and the clocks were striking
thirteen.'
count = {}

for character in message:
➊ count.setdefault(character, 0)
➋ count[character] = count[character] + 1

print(count)