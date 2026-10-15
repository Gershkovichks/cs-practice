import tablestats

filename = input().strip()

with open(filename, "r", encoding="utf-8") as file:
    rows = tablestats.read_rows(file)

total = len(rows)
counts = tablestats.count_types(rows)
types = len(counts)
errors = tablestats.total_minutes(rows, "ошибка")

print(total)
print(types)
print(errors)

summary_text = tablestats.to_csv(counts)
with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(summary_text)
