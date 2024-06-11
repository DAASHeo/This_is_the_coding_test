n = int(input())
group_word = n
for _ in range(n):
    word = list(input())
    for i in range(len(word)):
        if (i != (len(word)-1)):
            if(word[i] != word[i+1]):
                if(word[i] in word[i+1:]):
                    group_word -= 1
                    break;


print(group_word)
