## Legend
#   o: origin stack
#   x: extra stack
#   d: destination stack

disks = int(input())
o = [i for i in range(disks, 0, -1)]
x = []
d = []

def printStacks():
    global o, x, d
    print(o, x, d, sep='\n', end="\n\n")

def moveOne(o, d):
    printStacks()
    d.append(o.pop())
    return 1

def moveSubStack(o, d, x, l):
    if l <= 1:
        return moveOne(o, d)
    else:
        return moveSubStack(o, x, d, l - 1) + moveOne(o, d) + moveSubStack(x, d, o, l - 1)

def moveStack(o, x, d):
    moves = moveSubStack(o, d, x, len(o))
    printStacks()
    print(f"Moves Required: {moves}")

moveStack(o, x, d)