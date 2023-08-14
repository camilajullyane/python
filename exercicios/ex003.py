def distancia():
    x1 = float(p1[0])
    x2 = float(p2[0])
    y1 = float(p1[1])
    y2 = float(p2[1])

    res = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    
    print(f'{res:.4f}')
p1 = input().split()
p2 = input().split()

distancia()
