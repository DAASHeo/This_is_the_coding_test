n, m = map(int, input().split())
card = []
for _ in range(n):
    card.append(list(map(int, input().split())))

picked = 0
for i in card:
    if picked == 0 or min(i) > picked:
        picked = min(i)


print(picked)