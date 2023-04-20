def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) > len(b):
        if b == a[-len(b):]:
            return True
        else:
            return False
    else:
        if a == b[-len(a):]:
            return True
        else:
            return False

