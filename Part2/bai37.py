words = []
while True:
    word = input()
    if not word:
        break
    if word not in words:
        words.append(word)

for word in words:
    print(word)
