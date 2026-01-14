def minimum_machines(tasks):
    events = []
    for s, e in tasks:
        events.append((s, 1))    # start -> need one more machine
        events.append((e, -1))   # end   -> free one machine

    # If times tie, process ends before starts (so end at t frees machine for start at t)
    events.sort(key=lambda x: (x[0], x[1]))

    cur = 0
    best = 0
    for _, delta in events:
        cur += delta
        if cur > best:
            best = cur
    return best

