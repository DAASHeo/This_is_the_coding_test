def answer(logs):
    count = {}
    well_known = {}
    for user in logs:
        a, b = user.split()

        if not count.get(a):
            count[a] = [b]
        else:
            count[a].append(b)

    for check in count:
        if len(count[check]) >= 1:
            for i in count[check]:
                if not well_known.get(i):
                    well_known[i] = 1
                else:
                    well_known[i] += 1

    average = len(count) / 2
    answer = [problem for problem, count in well_known.items() if count >= average]
    print(answer)

logs = ["morgan string_compare", "felix string_compare","morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]
answer(logs)