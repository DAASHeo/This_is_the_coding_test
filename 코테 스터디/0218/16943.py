a, b = map(int, input().split())
arr = [i for i in a]
result = []
def sequence(b):
    result = []
    if result < b:
        return max(result)
def sol(key):
    if key == len(arr):
        return arr
    for i in arr:
        if i not in result:
            result.append(i)
            sol(key + 1)
            result.pop()

def main():

    sol(0)
    sequence(b)