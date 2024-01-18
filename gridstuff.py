grid=[[1]+8 for n in range(8)]
grid [0,1,2,3,4,5,6,7]

w=70

def setup ():
    size(800,600)
def draw():
    x,y=0,0
    for row in grid:
        for col in row:
              rect(x,y,w,w)
              x=x+w
        y=y+w
        x=0
