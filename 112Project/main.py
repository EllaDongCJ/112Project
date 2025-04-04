from cmu_graphics import *
import random


def onAppStart(app):
    app.width = 1000
    app.height = 500
    app.monster = []
    app.fire = False
    app.bullets = [] # [bulletX, bulletY]
    app.charX = 160
    app.charY = 320
    app.charBottom = 400
    app.attack = 1
    app.stepsPerSecond = 20
    app.coffeeX = random.randint(200, 800)
    app.coffeeY = random.randint(100, 350)
    app.coffeeR = 20
    app.menuColor = None
    app.state = 0
    app.dx = 10
    app.dy = 10
    app.time = 0
    
def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def onKeyPress(app, key):
    if key=="4":
        app.state=4
    if key == "5":
        app.state = 5
    if app.state==4:
        if key == "a":
            app.bullets.append([app.charX + 50, app.charY + 20])
        if key == "up":
            if app.charY - 100 >= 100:
                app.charY -= 100
        if key == "down":
            if app.charY + 100 <= 320:
                app.charY += 100
    

def redrawAll(app):
    if app.state==4:
        drawRect(880, 440, 80, 40, fill = app.menuColor, border = "black")
        drawLabel("MENU", 920, 460, size = 20)
        drawRect(app.charX, app.charY, 20, 80, fill = "cyan")
        for bullet in app.bullets:
            bulletX, bulletY = bullet
            drawCircle(bulletX, bulletY, 10, fill = "pink")
        if app.time > 0 and app.time % 30 == 0:
            drawCircle(app.coffeeX, app.coffeeY, app.coffeeR, fill = "brown")
    if app.state == 5:
        drawLabel("MENU", 500, 80, size = 50)
        drawRect(500, 280, 300, 50, fill = None, border = "black", align = "center")
        drawRect(500, 180, 300, 50, fill = None, border = "black", align = "center")
        drawRect(500, 380, 300, 50, fill = None, border = "black", align = "center")
        drawLabel("Back to Homepage", 500, 180, size = 20)
        drawLabel("Continue Gaming", 500, 280, size = 20)
        drawLabel("Game Instructions", 500, 380, size = 20)
        
def hitMonster(app):
    pass

def onMouseMove(app, mouseX, mouseY):
    if app.state==4:
        if (880 <= mouseX <= 960 and 440 <= mouseY <= 480):
            app.menuColor = "lightBlue"
        else:
            app.menuColor = None
        pass

def onMousePress(app, mouseX, mouseY):
    if app.state==4:
        if (880 <= mouseX <= 960 and 440 <= mouseY <= 480):
            app.state = 5

def onStep(app):
    moveBullets(app)
    bounceHorizontally(app)
    bounceVertically(app)
    pass

def moveBullets(app):
    for bullet in app.bullets:
        bullet[0] += 10
    pass

def bounceHorizontally(app):
    app.coffeeX += app.dx
    if app.coffeeX + app.coffeeR >= app.width:
        # bounce off the right edge of the canvas:
        app.coffeeX = app.width - app.coffeeR
        app.dx = -app.dx
    elif app.coffeeX <= app.coffeeR:
        # bounce off the left edge of the canvas (note that you will change
        # this code in your solution):
        app.coffeeX = app.coffeeR
        app.dx = -app.dx

def bounceVertically(app):
    app.coffeeY += app.dy
    if app.coffeeY + app.coffeeR >= app.height:
        app.coffeeY = app.height - app.coffeeR 
        app.dy = -app.dy
    elif app.coffeeY <= app.coffeeR:
        app.coffeeY = app.coffeeR
        app.dy = -app.dy
        
        


def main():
    runApp()

main()