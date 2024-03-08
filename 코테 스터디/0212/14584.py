def solution(code, dict):
    for i in range(len(code)):
        n = abs(ord(code[i]) - ord(dict[i]))
        print(n)
        count = 0
        for j in range(len(dict)):
            print(ord(dict[j]) + n, ord(code[j]), ord("z"))
            if(ord(dict[j]) + n) > ord("z"):
                num = ord(dict[j])+n - ord("z")
                print("num : ", num)
                if (chr(ord(dict[0]) + num) == code[j]):
                    count += 1
                    continue
            else:
                if(chr(ord(dict[j]) + n) == code[j]):
                    count += 1
                    print("count",count)
                else: break
        if(count == len(dict)):
            return n
    return -1

def main():
    code = input()
    answer = []
    number = int(input())
    for _ in range(number):
        dict = input()
        if (solution(code, dict) != -1):
            for i in range(len(code)):
                answer.append(chr(ord(code[i])+solution(code, dict)))
            break
    return  ''.join(answer)

main()