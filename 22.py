def euler():
    f = open('22/names.txt')
    names = f.read().replace('"','').split(',')
    names.sort()
    total = 0
    for name,i in zip(names,range(1,len(names)+1)):
        total += score(name)*i
    return total

def score(name):
    sc = 0
    for c in list(name):
        sc += ord(c)-64
    return sc
                          
if __name__ == '__main__':
    print euler()
