def read_rows(lines):
    head = None
    rows = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        linez = [f.strip() for f in line.split(',')]

        if head is None:
            head = linez
            continue

        if len(linez) == len(head):
            rows.append(dict(zip(head, linez)))
    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get('тип')
        if kind is not None:
            counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows, kind):
    total = 0.0
    records = False
    for row in rows:
        if row.get('тип') == kind:
            records = True
            val = row.get('минуты')
            if val is not None:
                val = val.replace(',', '.')
                try:
                    total += float(val)
                except ValueError:
                    continue
    if records:
        return round(total, 1)
    else:
        return 0.0

def to_csv(counts):
    lines = ["тип,количество"]
    for kind in sorted(counts.keys()):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
