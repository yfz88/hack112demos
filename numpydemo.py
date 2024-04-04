from cmu_graphics import *
from PIL import Image
import random
import numpy as np

#main perlin function, taking two int values and a default seed value of 0 which can be changed
def perlin(x, y, seed=0):
    x0 = x.astype(int)
    x1 = x0 + 1
    y0 = y.astype(int)
    y1 = y0 + 1

    #creates random seed
    np.random.seed(seed)
    #generates probability table with int data type
    ptable = np.arange(256, dtype = int)
    #shuffles the probability table
    np.random.shuffle(ptable)
    #stacks then flattens table to act as a 2d grid
    ptable = np.stack([ptable, ptable]).flatten()

    distanceX = x - x0
    distanceY = y - y0

    #fade function (see papers and other documentation of perlin noise for why the fade function is the way it is)
    smoothX = fade(distanceX)
    smoothY = fade(distanceY)

    #gradient function that takes in coordinate values and applies a gradient to the 2d vectors
    n00 = gradientFunc(ptable[ptable[x0] + y0], x0, y0, x, y)
    n01 = gradientFunc(ptable[ptable[x0] + y0 + 1],x0, y1, x, y)
    n11 = gradientFunc(ptable[ptable[x0 + 1] + y0 + 1], x1, y1, x, y)
    n10 = gradientFunc(ptable[ptable[x0 + 1] + y0],x1, y0, x, y)

    #linear interpolation on the output of the gradient function which generates "smoothness"
    x1LinInterp = lerp(n00, n10, smoothX)
    x2LinInterp = lerp(n01, n11, smoothX)
    return lerp(x1LinInterp, x2LinInterp, smoothY)

def gradientFunc(iteration, integerX, integerY, x, y):
    dx = x - integerX
    dy = y - integerY

    vectors = np.array([[0,1], [0,-1], [1,0], [-1,0]])
    gradient = vectors[iteration % 4]
  
    return (dx*gradient[:, :, 0] + dy*gradient[:, :, 1])

def lerp(a, b, x):
    return a + x * (b - a)

def fade(z):
    return 6 * z**5 - 15 * z**4 + 10 * z**3

def redrawAll(app):
    #creates evenly spaced lienar space based on inputs given
    #in this case effectively changes cluster of image in final graphics output
    numArray = np.linspace(1, 20, 50, endpoint = False)
    #meshgrid turns numpy arrays into coordinate matrices (i.e. grids of values)
    x, y = np.meshgrid(numArray, numArray)
    seedNum = random.randrange(0, 1000000000)
    img = Image.fromarray(perlin(x, y, seed = seedNum) * 255, 'I')
    img = img.resize((1600, 1600))
    img = CMUImage(img)
    drawImage(img, 800, 800, align = 'center')    

def main():
    runApp()

main()
