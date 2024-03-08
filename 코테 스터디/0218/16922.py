# I : 1, V : 5, X : 10 , L: 50
dict = {"I" : 1, "V" : 5, "X" : 10 , "L": 50}
def roof(N, arr):
    result = []
    if len(arr) == 0:
        return[]
    for i in range(len(arr)):
        element = arr[i]
        for word in roof(N-1, arr):
            result.append(element + word)
    return result

def main():
    arr = [key for key in dict]
    result = []
    N = int(input())
    picked = roof(N, arr)
    for a,b in picked:
        result.append(dict[a] + dict[b])

    return len(list(set(result)))

main()

