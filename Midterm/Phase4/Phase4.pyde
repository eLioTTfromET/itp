x = 500 # Set the x dimension of the size of the canvas
y = 500 # Set the y dimension of the size of the canvas
nx = 20 # Set the x dimension of the grid of visual objects
ny = 20 # Set the y dimension of the grid of visual objects

def setup():
    background(0)
    size(x,y)
    noStroke()
    
def drawObject(x,y,nx,ny):
    push()
    translate(x,y)
    scale((width-(width/(4.0*nx)))/(nx*30),(height-(height/(4.0*ny)))/(ny*30))
    fill(127)
    rect(0, 0, 40, 10)
    rect(0, 0,  10, 40)
    rect(30, 0,  10, 40)
    rect(0, 30, 40, 10)
    fill(255)
    ellipse(5, 5, 20, 20)
    ellipse(35, 5, 20, 20)
    ellipse(5, 35, 20, 20)
    ellipse(35, 35, 20, 20)
    pop()
    
def draw():
    for i in range(nx):
        for j in range(ny):
            drawObject((i*(width-(width/(4.0*nx)))/nx),(j*(height-(height/(4.0*ny)))/ny),nx,ny)
