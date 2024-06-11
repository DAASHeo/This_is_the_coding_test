word = input().upper()
word_list = list(set(word))
list = []

for i in word_list:
    list.append(word.count(i))

if list.count(max(list)) >= 2:
    print("?")
else:
    print(word_list[list.index(max(list))])