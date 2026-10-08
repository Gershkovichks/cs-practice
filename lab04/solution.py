def winner(names, scores):
    Max = max(scores)
    for i in range(len(scores)):
        if Max == scores[i]:
            name = names[i]
            break
    return name

def average(scores):
    if len(scores) > 0:
        Avg = round(sum(scores) / len(scores), 2)
        return Avg
    else:
        return 0

def ranking(names, scores):
    sorted_list = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
    return [name for name, scores in sorted_list]

def above_average(names, scores):
    Avg = average(scores)
    aname = [name for name, score in zip(names, scores) if score > Avg]
    return aname

"""
names = ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

print(winner(names, scores))
print(average(scores))
print(ranking(names, scores))
print(above_average(names, scores))
"""
