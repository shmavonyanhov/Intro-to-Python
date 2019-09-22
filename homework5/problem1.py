def max(*args):
    if len(args)==0:
        return "no numbers given"

    m=args[0]
    for i in args:
        if i>m:
            m=i
    return m


