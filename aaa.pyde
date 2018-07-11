def setup():
    size(800, 600)
    fill(0, 0, 255)
    rect(0, 0, 155, 155)
    fill(255, 0, 0)
    rect(0, 114, 155, 155)
    fill(0, 155, 0)
    rect(0, 224, 155, 155)
    fill(255, 255, 255)
    rect(0, 334, 155, 155)
    
def draw():
    if mousePressed and mouseX > 158:
       line(pmouseX, pmouseY, mouseX, mouseY)
    if mouseX <= 200 and mouseY >= 100:
       stroke(0, 0, 99)
    if mouseX <= 100 and mouseY >= 200:
       stroke(255, 0, 0)

def mouseClicked():
    if mouseX > 200:
        if mouseY < 100:
          stroke(255, 0, 0)
        else:
          stroke(0, 255, 0)
       
    
    
        
    

    
