def setup():
    background(0)
    size(400, 400) # Set the size of canvas
    noStroke() # Disable drawing the stroke
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(127) # Fill in with black color
    rect(0, 0, 40, 10) # Draw rectangles
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
    drawObject(100,100,2)
    drawObject(200,200,2)
