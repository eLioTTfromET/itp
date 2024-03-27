def setup():
    background(0)
    size(150, 150) # Set the size of canvas
    noStroke() # Disable drawing the stroke
    
def draw():
    fill(127) # Fill in with black color
    rect(25, 25, 40, 10) # Draw rectangles
    rect(25, 25,  10, 40)
    rect(55, 25,  10, 40)
    rect(25, 55, 40, 10)
    fill(255)
    ellipse(30, 30, 20, 20)
    ellipse(60, 30, 20, 20)
    ellipse(30, 60, 20, 20)
    ellipse(60, 60, 20, 20)
