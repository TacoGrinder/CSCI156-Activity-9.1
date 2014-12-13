__author__ = 'ortus'


def qfastqfurious():
    i = 1
    f = open('rw.txt','w+', encoding='utf-8')
    global counter
    counter = 0
    while i != 0:
        x = input("Input:")
        x.upper()
        if x == "q":
            return counter
        else:
            f.write(x+"\n")
            counter += 1
    f.close()

def getinput(i):
    f = open("rw.txt", "r", encoding="utf-8")
    for j in range(i):
        print(f.readline())
    print(counter)
    f.close()

getinput(qfastqfurious())