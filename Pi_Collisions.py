from time import time



def intersectBoxes():
    global x1, x2, v1, v2, m2

    if v1 == v2:
        return None

    t = (x2 - x1) / (v1 - v2);

    _v1 = ((1 - m2) * v1 + 2 * m2 * v2)/(1 + m2)
    _v2 = ((m2 - 1) * v2 + 2 * v1)/(1 + m2)

    return x1 + v1 * t, x2 + v2 * t, _v1, _v2, t


def intersectWall():
    global x1, x2, v1, v2, m2

    if v1 == 0:
        return None

    t = -x1 / v1

    return 0, -v1, t


def done():
    return (intersectBoxes() == None or intersectBoxes()[-1] <= 0) \
        and (intersectWall() == None or intersectWall()[-1] <= 0)


def printState():
    global x1, x2, v1, v2, m2
    print('Box 1: x = {}, v = {}.\nBox 2: x = {}, v = {}.'.format(x1, v1, x2, v2))


def run(p):
    global x1, x2, v1, v2, m2
    
    x1 = 1
    x2 = 2

    v1 = 0
    v2 = -1

    m2 = 100**(p - 1)

    print('m2 = {} m1'.format(m2))
    
    counter = 0

    t0 = time()

    while not done():
        x1, x2, v1, v2, _ = intersectBoxes()
        counter += 1

        if done():
            break

        x1, v1, _ = intersectWall()
        counter += 1

    print('{} collisions in total.'.format(counter))
    print('It took {}s to compute.\n\n\n'.format(time() - t0))


p = 8


for i in range(p):
    run(i + 1)

    

    
