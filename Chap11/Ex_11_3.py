def print_hist(h):
    keys = sorted(h.keys())
    for key in keys:
        print(key, h[key])

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h=histogram("hoangducnguyen")
print_hist(h)