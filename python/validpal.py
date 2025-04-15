def work(s):
    sett = ('abcdefghijklmnopqrstuvwxyz0123456789')

    work = [x for x in s.strip().lower() if x in sett]
    return work == work[::-1]