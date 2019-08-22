"""
Gyrofractal
===========
Generates and slowly zooms in on a Julia Fractal set
"""
import display
import utime
import buttons

#======>>CREDIT: Most fractal generation code stolen from https://www.geeksforgeeks.org/julia-fractal-python/
#Device resolution: 160x80
w, h, zoom = 32,16,0.001
xBuffer, yBuffer = 16, 8
pixelSize = 4

cX, cY = -0.7, 0.27015
moveX, moveY = 0.0, 0.0
maxIter = 255

gs = 140
colors = [ ((i>>2)*gs, (i>>1&1)*gs, (i&1)*gs) for i in range(0, maxIter + 1) ]

with display.open() as d:
    d.clear()
    d.update()
    d.close()

with display.open() as d:
    while True:
        print("----------------NEW LOOP START-----------------")
        for x in range(w): 
            for y in range(h): 
                zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX 
                zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY 
                i = maxIter 
                while zx*zx + zy*zy < 4 and i > 1: 
                    tmp = zx*zx - zy*zy + cX 
                    zy,zx = 2.0*zx*zy + cY, tmp 
                    i -= 1
                d.rect(xBuffer + x * pixelSize, yBuffer + y * pixelSize, xBuffer + x * pixelSize + pixelSize, yBuffer + y * pixelSize + pixelSize, col=(255-i,255-i,255-i), filled=True)
            d.update()
        print("======================ONE LOOP COMPLETED=========================")
        if zoom < 0:
            zoom += 0.2
        elif zoom < 1:
            zoom += 0.1
        elif zoom < 3:
            zoom += 0.01
        else:
            zoom += 0.005