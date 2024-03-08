import itertools

def main():
    a, b = map(int, input().split())
    arr = [i for i in str(a)]
    arr = list(map(int, arr))
    result = list(itertools.permutations(arr, len(arr)))
    result = [(''.join(map(str, t))) for t in result if int(''.join(map(str, t))) < b and (''.join(map(str, t))[0]) != '0']
    if len(result) == 0:
        return print(-1)
    else:
        return print(max(result))

main()