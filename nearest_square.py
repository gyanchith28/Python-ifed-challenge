import math
def nearest_square(n):
    if n<0:
        return 0
    else:
        root = math.sqrt(n)
        for i in range(n,-1,-1):
            if int(root)**2 ==i:
                return i
            else:
                continue

