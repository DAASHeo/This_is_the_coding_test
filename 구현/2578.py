import sys
player = [] * 5
director = []
temp_down = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
temp_up = [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]
check = [[False] * 5 for i in range(5)]
count = 0

for _ in range(5):
    player.append(list(map(int, sys.stdin.readline().strip().split())))

for _ in range(5):
    director += (list(map(int, sys.stdin.readline().strip().split())))

for i in director:


def bingo_check():
    while (count != 3):
        for a, b in temp_down:
            if check[a][b] == False:
                break
        for a, b in temp_up:
            if check[a][b] == False:
                break

