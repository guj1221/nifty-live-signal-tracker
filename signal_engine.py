def decide_signal(current, previous, gap):
    if current - previous >= gap:
        return "BUY CALL", current + gap
    elif previous - current >= gap:
        return "BUY PUT", current - gap
    else:
        return "HOLD", None
