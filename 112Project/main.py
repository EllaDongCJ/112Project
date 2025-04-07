from cmu_graphics import * 
import random

def onAppStart(app):
    # 0: homepage, 1: instructions, 2: characters, 3: inGameInstruction, 4: Gaming, 5: Menu, 6: Ending
    app.state = 0
    app.width = 1000
    app.height = 500
    app.charX = 160
    app.charY = 320
    app.charBottom = 400
    app.charSelect = 0
    app.grade = 30
    app.win = False
    app.lose = False

    #attack related
    if app.charSelect == 0:
        app.attack = 1
    else:
        app.attack = 1.4
    app.bullets = [] # [bulletX, bulletY] 
    
    # coffee related
    app.showCoffee = False
    app.coffeeX = random.randint(200, 800)
    app.coffeeY = random.randint(100, 350)
    app.coffeeR = 20
    app.coffeeLife = 2
    app.getCoffee = False
    app.coffeeTime = 0
    app.coffeeSpawn = False
    
    # movements/time related
    app.dx = 15
    app.dy = 15
    app.time = 0
    app.integerTime = 0
    app.stepsPerSecond = 20

    # Colors
    app.instructionColor = None
    app.backToMenuColor = None
    app.continueGameColor = None
    app.gainInstructionColor = None
    app.backColor = None
    app.menuColor = "white"
    app.startgameColor = None
    app.backHomeColor = None
    

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def shootCoffee(app):
    i = 0
    for i in range(len(app.bullets)):
        cx, cy = app.bullets[i] 
        if distance(cx, cy, app.coffeeX, app.coffeeY) <= 10 + app.coffeeR:
            return i
    else:
        return None

def onKeyPress(app, key):
    if key== "4":
        app.state= 4
    if key == "5":
        app.state = 5
    if app.state== 4:
        if key == "a":
            app.bullets.append([app.charX + 50, app.charY + 20])
        if key == "up":
            if app.charY - 100 >= 100:
                app.charY -= 100
        if key == "down":
            if app.charY + 100 <= 320:
                app.charY += 100
    if key == "6":
        app.state = 6

def redrawAll(app):
    if app.state == 0:
        drawLabel("112 GPA NOT FOUND", 500, 80, font='monospace', size = 50, bold = True)
        drawRect(500, 280, 300, 50, fill = app.instructionColor, border = "black", align = "center")
        drawRect(500, 180, 300, 50, fill = app.startgameColor, border = "black", align = "center")
        drawLabel("Start Game", 500, 180, size = 20)
        drawLabel("Game Instructions", 500, 280, size = 20)
        drawLabel("Remember to read the instructions before you start!", 500, 380, size = 15)
    elif app.state == 1:
        drawLabel("Instructions 404 not found", 500, 120, size = 20)
        drawRect(880, 440, 80, 40, fill = app.backColor, border = "black")
        drawLabel("Back", 920, 460, size = 20)
    elif app.state == 2:
        drawLabel("Characters 404 not found", 500, 120, size = 20)
        drawRect(880, 440, 80, 40, fill = app.backColor, border = "black")
        drawLabel("Back", 920, 460, size = 20)
    elif app.state == 3:
        drawLabel("Instructions 404 not found", 500, 120, size = 20)
        drawRect(780, 440, 180, 40, fill = app.backColor, border = "black")
        drawLabel("Back to Game", 870, 460, size = 20)
    elif app.state == 4:
        drawRect(0, 400, 1000, 100, fill = "pink")
        drawRect(880, 440, 80, 40, fill = app.menuColor, border = "black")
        drawLabel("MENU", 920, 460, size = 20)
        drawRect(app.charX, app.charY, 20, 80, fill = "cyan")
        drawLabel(f"Time: {app.integerTime}", 500, 40)
        for bullet in app.bullets:
            bulletX, bulletY = bullet
            drawCircle(bulletX, bulletY, 10, fill = "pink")
        if app.showCoffee:
            drawCircle(app.coffeeX, app.coffeeY, app.coffeeR, fill = "brown")
            drawLabel(f"{app.coffeeLife}", app.coffeeX, app.coffeeY, fill = "white", bold = True)
        drawLabel(f"{app.coffeeTime}, {app.attack}", 160, 480)
    elif app.state == 5:
        drawLabel("MENU", 500, 80, size = 50) # type: ignore
        drawRect(500, 280, 300, 50, fill = app.continueGameColor, border = "black", align = "center")
        drawRect(500, 180, 300, 50, fill = app.backToMenuColor, border = "black", align = "center")
        drawRect(500, 380, 300, 50, fill = app.gainInstructionColor, border = "black", align = "center")
        drawLabel("Back to Homepage", 500, 180, size = 20)
        drawLabel("Continue Gaming", 500, 280, size = 20)
        drawLabel("Game Instructions", 500, 380, size = 20)
    elif app.state == 6:
        drawLabel("Semester Summary", 500, 80, font='monospace', size = 50, bold = True)
        drawLabel(f"Your grade is: {app.grade}", 500, 180, size = 20)
        drawLabel(f"Time Used: {app.integerTime}", 500, 280, size = 20)
        drawRect(500, 380, 300, 50, fill = app.backHomeColor, border = "black", align = "center")
        drawLabel("Homepage", 500, 380, size = 20)
        
def onMouseMove(app, mouseX, mouseY):
    if app.state == 0:
        if (350 <= mouseX <= 650 and 155 <= mouseY <= 205):
            app.startgameColor = "lightBlue" 
        else:
            app.startgameColor = None
        if (350 <= mouseX <= 650 and 255 <= mouseY <= 305):
            app.instructionColor = "lightBlue" 
        else:
            app.instructionColor = None
    if app.state == 1:
        if (880 <= mouseX <= 960 and 440 <= mouseY <= 480):
            app.backColor = "lightBlue"
        else:
            app.backColor = None
    if app.state == 4:
        if (880 <= mouseX <= 960 and 440 <= mouseY <= 480):
            app.menuColor = "lightBlue"
        else:
            app.menuColor = "white"
    if app.state == 5:
        if (350 <= mouseX <= 650 and 155 <= mouseY <= 205):
            app.backToMenuColor = "lightBlue" # back to menu
        else:
            app.backToMenuColor = None
        if (350 <= mouseX <= 650 and 255 <= mouseY <= 305):
            app.continueGameColor = "lightBlue" # continue gaming
        else:
            app.continueGameColor = None
        if (350 <= mouseX <= 650 and 355 <= mouseY <= 405):
            app.gainInstructionColor = "lightBlue" # game instruction
        else:
            app.gainInstructionColor = None
    if app.state == 6:
        if (350 <= mouseX <= 650 and 355 <= mouseY <= 405):
            app.backHomeColor = "lightBlue" # game instruction
        else:
            app.backHomeColor = None

def onMousePress(app, mouseX, mouseY):
    if app.state == 0:
        if (350 <= mouseX <= 650 and 155 <= mouseY <= 205):
            app.state = 2 # back to menu
        if (350 <= mouseX <= 650 and 255 <= mouseY <= 305):
            app.state = 1 # continue gaming
    if app.state == 1 or app.state == 2:
        if (880 <= mouseX <= 960 and 440 <= mouseY <= 480):
            app.state = 0
    if app.state == 3:
        if 780 <= mouseX <= 960 and 440 <= mouseY <= 480:
            app.state = 4
    if app.state == 4:
        if (880 <= mouseX <= 960 and 440 <= mouseY <= 480):
            app.state = 5
    if app.state == 5:
        if (350 <= mouseX <= 650 and 155 <= mouseY <= 205):
            app.state = 0 # back to menu
        if (350 <= mouseX <= 650 and 255 <= mouseY <= 305):
            app.state = 4 # continue gaming
        if (350 <= mouseX <= 650 and 355 <= mouseY <= 405):
            app.state = 3 # game instruction
    if app.state == 6:
        if (350 <= mouseX <= 650 and 355 <= mouseY <= 405):
            app.state = 0

def onStep(app):
    if app.state == 4:
        if app.lose or app.win:
            app.state = 6

        # 更新时间
        app.time += 0.05
        app.integerTime = int(app.time)

        if app.integerTime > 0 and app.integerTime % 30 == 0 and not app.coffeeSpawn:
            app.showCoffee = True
            app.coffeeSpawn = True
            app.coffeeLife = 3
        elif app.integerTime % 30 != 0:
            app.coffeeSpawn = False

        if app.showCoffee:
            coffeeIndex = shootCoffee(app)
            if coffeeIndex is not None:
                app.bullets.pop(coffeeIndex)
                app.coffeeLife -= app.attack
            if app.coffeeLife <= 0:
                app.getCoffee = True
                app.showCoffee = False

        if app.getCoffee:
            app.coffeeTime += 0.05
            if app.charSelect == 0:
                app.attack = 2
            elif app.charSelect == 1:
                app.attack = 2.4
            if app.coffeeTime > 5:
                app.getCoffee = False
                app.coffeeTime = 0
                app.coffeeLife = 3
                if app.charSelect == 0:
                    app.attack = 1
                elif app.charSelect == 1:
                    app.attack = 1.4

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

def jumping(app):
    pass


def main():
    runApp()

main()
