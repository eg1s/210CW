def findhighperfectsq(a):
    import math
    SquareRoot = math.sqrt(a)

    if round(SquareRoot) - SquareRoot == 0:
        cRoot = 'PerfectSquaRe'
        print('PerfectSquaRe')
    else:
        cRoot = 'NotPerfectSquaRe'

        aRounded = math.floor(SquareRoot)
        aRoundedSquare = aRounded * aRounded
        print (aRoundedSquare, 'Largest perfect square that is less than', a)
        
findhighperfectsq(15)
