"""
Program Information
Program Name        :    Boucing_ball.py     
Program Description :    To provide a user with a simple golf game.
Date                :    1/25/2014
Game Programmer     :    Brandon L Olson
Game Artist         :    Micheal T Durling
Game Designer       :    Tyler   B Bason
"""

#Import Libraries
import sys
import pygame
import time

#Pygame Initiation
pygame.init()
pygame.font.init()

#Set Color Constants
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0,200,0]

#Initialize Variables
currentGolfBallVelocity = [0, 0]
hitSpeedSwtichCounter = 0
highHitSpeed = 15
mediumHitSpeed = 10
lowHitSpeed = 5
hitSpeed = highHitSpeed
grassFriction = .25
sandFriction = 1
tileUnit = 40
friction = grassFriction
leftDirectionPressed  = False
rightDirectionPressed = False
upDirectionPressed    = False
downDirectionPressed  = False
enterPressed          = False
currentDirectionKeysPressedCount = 0
golfBallHitCounter = 0
gameState = "Title"
titleScreenSize = width, height = 640, 480
playScreenSize = [640,480+110]
winScreenSize = [640, 480]

#Load Images
golfBall = pygame.image.load("golfBall.gif")
leftArrowKey = pygame.image.load("arrowLeft.gif")
rightArrowKey = pygame.image.load("arrowRight.gif")
upArrowKey = pygame.image.load("arrowUp.gif")
downArrowKey = pygame.image.load("arrowDown.gif")
highPoweredSymbol = pygame.image.load("powerHigh.gif")
mediumPoweredSymbol = pygame.image.load("powerMedium.gif")
lowPoweredSymbol = pygame.image.load("powerLow.gif")
golfHole = pygame.image.load("golfHole.gif")
golfWall = pygame.image.load("trapWall.gif")
sandTrap = pygame.image.load("trapSand.gif")
waterTrap = pygame.image.load("trapWater.gif")
titleScreenImage = pygame.image.load("screenTitle.gif")
playingScreenImage = pygame.image.load("screenPlain.gif")
winningScreenImage = pygame.image.load("screenWinning.gif")

#Fonts
arialFont30Point = pygame.font.SysFont("arial", 30)

#Render Text
golfBallHitCounterDisplay = arialFont30Point.render(str(golfBallHitCounter), True, WHITE)

#Create Rects

#Screen Rects
titleScreenImageRect = titleScreenImage.get_rect()
playingScreenImageRect = playingScreenImage.get_rect()
winningScreenImageRect = winningScreenImage.get_rect()

#Golf Ball Rect
golfBallHitBox = golfBall.get_rect()

#Arrow Rects
leftArrowKeyHitBox = leftArrowKey.get_rect()
rightArrowKeyHitBox = rightArrowKey.get_rect()
upArrowKeyHitBox = upArrowKey.get_rect()
downArrowKeyHitBox = downArrowKey.get_rect()

#Playing Screen Rect
golfBallHitCounterRect = golfBallHitCounterDisplay.get_rect()

#Symbol Rects
highPoweredRect = highPoweredSymbol.get_rect()
mediumPoweredRect = mediumPoweredSymbol.get_rect()
lowPoweredRect = lowPoweredSymbol.get_rect()

#Golf Hole Rect
golfHoleHitBox = golfHole.get_rect()

#Golf Wall Rects
golfWallHitBox1 = golfWall.get_rect()
golfWallHitBox2 = golfWall.get_rect()
golfWallHitBox3 = golfWall.get_rect()
golfWallHitBox4 = golfWall.get_rect()
golfWallHitBox5 = golfWall.get_rect()
golfWallHitBox6 = golfWall.get_rect()
golfWallHitBox7 = golfWall.get_rect()
golfWallHitBox8 = golfWall.get_rect()
golfWallHitBox9 = golfWall.get_rect()
golfWallHitBox10 = golfWall.get_rect()
golfWallHitBox11 = golfWall.get_rect()
golfWallHitBox12 = golfWall.get_rect()
golfWallHitBox13 = golfWall.get_rect()
golfWallHitBox14 = golfWall.get_rect()
golfWallHitBox15 = golfWall.get_rect()
golfWallHitBox16 = golfWall.get_rect()
golfWallHitBox17 = golfWall.get_rect()
golfWallHitBox18 = golfWall.get_rect()
golfWallHitBox19 = golfWall.get_rect()
golfWallHitBox20 = golfWall.get_rect()
golfWallHitBox21 = golfWall.get_rect()

#Sand Trap Rects
sandTrapHitBox1 = sandTrap.get_rect()
sandTrapHitBox2 = sandTrap.get_rect()
sandTrapHitBox3 = sandTrap.get_rect()
sandTrapHitBox4 = sandTrap.get_rect()
sandTrapHitBox5 = sandTrap.get_rect()
sandTrapHitBox6 = sandTrap.get_rect()
sandTrapHitBox7 = sandTrap.get_rect()
sandTrapHitBox8 = sandTrap.get_rect()

#Water Trap Rects
waterTrapHitBox1 = waterTrap.get_rect()
waterTrapHitBox2 = waterTrap.get_rect()
waterTrapHitBox3 = waterTrap.get_rect()
waterTrapHitBox4 = waterTrap.get_rect()
waterTrapHitBox5 = waterTrap.get_rect()
waterTrapHitBox6 = waterTrap.get_rect()
waterTrapHitBox7 = waterTrap.get_rect()
waterTrapHitBox8 = waterTrap.get_rect()
waterTrapHitBox9 = waterTrap.get_rect()
waterTrapHitBox10 = waterTrap.get_rect()
waterTrapHitBox11 = waterTrap.get_rect()
waterTrapHitBox12 = waterTrap.get_rect()

#Move the rects

#Move Direction keys
leftArrowKeyHitBox   = leftArrowKeyHitBox.move(playScreenSize[0] - 170 , playScreenSize[1] - 50)
rightArrowKeyHitBox = rightArrowKeyHitBox.move(playScreenSize[0] - 50  , playScreenSize[1] - 50)
upArrowKeyHitBox       = upArrowKeyHitBox.move(playScreenSize[0] - 110 , playScreenSize[1] - 90)
downArrowKeyHitBox   = downArrowKeyHitBox.move(playScreenSize[0] - 110 , playScreenSize[1] - 50)

#Move Hit Counter
golfBallHitCounterRect = golfBallHitCounterRect.move(320, 150)

#Move Symobols
symbolPos = [playScreenSize[0] - 220 ,playScreenSize[1] - 50]
highPoweredRect = highPoweredRect.move(symbolPos)
mediumPoweredRect = mediumPoweredRect.move(symbolPos)
lowPoweredRect = lowPoweredRect.move(symbolPos)

#Move Golf ball
golfHoleHitBox = golfHoleHitBox.move(11*tileUnit,7*tileUnit)

#width height
golfWallHitBox1 = golfWallHitBox1.move(0,3*tileUnit)
golfWallHitBox2 = golfWallHitBox2.move(1*tileUnit,3*tileUnit)
golfWallHitBox3 = golfWallHitBox3.move(2*tileUnit,3*tileUnit)
golfWallHitBox4 = golfWallHitBox4.move(3*tileUnit,3*tileUnit)
golfWallHitBox5 = golfWallHitBox5.move(4*tileUnit,3*tileUnit)
golfWallHitBox6 = golfWallHitBox6.move(10*tileUnit,3*tileUnit)
golfWallHitBox7 = golfWallHitBox7.move(10*tileUnit,4*tileUnit)
golfWallHitBox8 = golfWallHitBox8.move(10*tileUnit,5*tileUnit)
golfWallHitBox9 = golfWallHitBox9.move(10*tileUnit,6*tileUnit)
golfWallHitBox10 = golfWallHitBox10.move(10*tileUnit,7*tileUnit)
golfWallHitBox11 = golfWallHitBox11.move(10*tileUnit,8*tileUnit)
golfWallHitBox12 = golfWallHitBox12.move(10*tileUnit,9*tileUnit)
golfWallHitBox13 = golfWallHitBox13.move(10*tileUnit,0*tileUnit)
golfWallHitBox14 = golfWallHitBox14.move(1*tileUnit,9*tileUnit)
golfWallHitBox15 = golfWallHitBox15.move(2*tileUnit,9*tileUnit)
golfWallHitBox16 = golfWallHitBox16.move(3*tileUnit,9*tileUnit)
golfWallHitBox17 = golfWallHitBox17.move(11*tileUnit,6*tileUnit)
golfWallHitBox18 = golfWallHitBox18.move(12*tileUnit,6*tileUnit)
golfWallHitBox19 = golfWallHitBox19.move(13*tileUnit,6*tileUnit)
golfWallHitBox20 = golfWallHitBox20.move(9*tileUnit,8*tileUnit)
golfWallHitBox21 = golfWallHitBox21.move(8*tileUnit,8*tileUnit)

sandTrapHitBox1 = sandTrapHitBox1.move(9*tileUnit,7*tileUnit)
sandTrapHitBox2 = sandTrapHitBox2.move(9*tileUnit,6*tileUnit)
sandTrapHitBox3 = sandTrapHitBox3.move(8*tileUnit,7*tileUnit)
sandTrapHitBox4 = sandTrapHitBox4.move(8*tileUnit,6*tileUnit)
sandTrapHitBox5 = sandTrapHitBox5.move(7*tileUnit,6*tileUnit)
sandTrapHitBox6 = sandTrapHitBox6.move(7*tileUnit,7*tileUnit)
sandTrapHitBox7 = sandTrapHitBox7.move(10*tileUnit,10*tileUnit)
sandTrapHitBox8 = sandTrapHitBox8.move(10*tileUnit,11*tileUnit)


waterTrapHitBox1 = waterTrapHitBox1.move(0*tileUnit,4*tileUnit)
waterTrapHitBox2 = waterTrapHitBox2.move(0*tileUnit,5*tileUnit)
waterTrapHitBox3 = waterTrapHitBox3.move(0*tileUnit,6*tileUnit)
waterTrapHitBox4 = waterTrapHitBox4.move(0*tileUnit,7*tileUnit)
waterTrapHitBox5 = waterTrapHitBox5.move(0*tileUnit,8*tileUnit)
waterTrapHitBox6 = waterTrapHitBox6.move(0*tileUnit,9*tileUnit)
waterTrapHitBox7 = waterTrapHitBox7.move(0*tileUnit,10*tileUnit)
waterTrapHitBox8 = waterTrapHitBox8.move(0*tileUnit,11*tileUnit)
waterTrapHitBox9 = waterTrapHitBox9.move(13*tileUnit,0*tileUnit)
waterTrapHitBox10 = waterTrapHitBox10.move(13*tileUnit,1*tileUnit)
waterTrapHitBox11 = waterTrapHitBox11.move(13*tileUnit,2*tileUnit)
waterTrapHitBox12 = waterTrapHitBox12.move(13*tileUnit,3*tileUnit)


#Referance Lists
listOfWallHitBoxs = [golfWallHitBox1, golfWallHitBox2, golfWallHitBox3, golfWallHitBox4, golfWallHitBox5, 
golfWallHitBox6, golfWallHitBox7, golfWallHitBox8, golfWallHitBox9, golfWallHitBox10, golfWallHitBox11, 
golfWallHitBox12, golfWallHitBox13, golfWallHitBox14, golfWallHitBox15, golfWallHitBox16, golfWallHitBox17,
golfWallHitBox18, golfWallHitBox19, golfWallHitBox20, golfWallHitBox21]

listOfSandTraps = [sandTrapHitBox1, sandTrapHitBox2, sandTrapHitBox3, sandTrapHitBox4, sandTrapHitBox5, 
sandTrapHitBox6, sandTrapHitBox7, sandTrapHitBox8]

listOfWaterTraps = [waterTrapHitBox1, waterTrapHitBox2, waterTrapHitBox3, waterTrapHitBox4, waterTrapHitBox5, 
waterTrapHitBox6, waterTrapHitBox7, waterTrapHitBox8, waterTrapHitBox9, waterTrapHitBox10, waterTrapHitBox11, 
waterTrapHitBox12]


#If the ball hits any of the inside or outside wall it will be removed from the inside of
#the wall and the ball will bounce off at an equal and opposite velocity
def collideWithWall(ballHitBox, ballVelocity, listOfWalls):
    for wall in listOfWalls:
        if ballHitBox.top+20 >= wall.top and ballHitBox.top+20 <= wall.bottom:
            #Ball hits the left side of a wall
            if ballHitBox.right >= wall.left and ballHitBox.right <= wall.right:
                ballHitBox = ballHitBox.move(-(ballHitBox.right - wall.left),0)
                ballVelocity[0] = -ballVelocity[0]
            #Ball hits the right side of a wall
            if ballHitBox.left <= wall.right and ballHitBox.left >= wall.left:
                ballHitBox = ballHitBox.move(-(ballHitBox.left - wall.right),0)
                ballVelocity[0] = -ballVelocity[0]
    
        if ballHitBox.left+20 >= wall.left and ballHitBox.left+20 <= wall.right:
            #Ball hits the top side of a wall
            if ballHitBox.top <= wall.top and ballHitBox.bottom >= wall.top:
                ballHitBox = ballHitBox.move(0, -(ballHitBox.bottom - wall.top))
                ballVelocity[1] = -ballVelocity[1]
            #Ball hits the bottom side of a wall
            if ballHitBox.top <= wall.bottom and ballHitBox.bottom >= wall.bottom:
                ballHitBox = ballHitBox.move(0,(wall.bottom - ballHitBox.top))
                ballVelocity[1] = -ballVelocity[1]

    #Ball hits the outside wall
    if ballHitBox.left <= 0:
        ballHitBox = ballHitBox.move(-ballHitBox.left,0)
        currentGolfBallVelocity[0] = -currentGolfBallVelocity[0]
    if ballHitBox.right >= playScreenSize[0]:
            ballHitBox = ballHitBox.move(-(ballHitBox.right-playScreenSize[0]),0)
            currentGolfBallVelocity[0] = -currentGolfBallVelocity[0]
    if ballHitBox.top <= 0:
            ballHitBox = ballHitBox.move(0,-ballHitBox.top)
            currentGolfBallVelocity[1] = -currentGolfBallVelocity[1]
    if ballHitBox.bottom >= playScreenSize[1]-110:
            ballHitBox = ballHitBox.move(0,-(ballHitBox.bottom-(playScreenSize[1]-110)))
            currentGolfBallVelocity[1] = -currentGolfBallVelocity[1]
    
    return ballHitBox, ballVelocity

#Active action for hitting sand hazard
def collideWithSand(ballHitBox, listOfSandTraps, friction, sandFriction, grassFriction):
    for sandHazard in listOfSandTraps:
        if golfBallHitBox.colliderect(sandHazard):
            friction = sandFriction
            return friction
        else:
            friction = grassFriction
    return friction

#Active action for hitting water hazard
def collideWithWater(ballHitBox, ballVelocity, listOfWaterTraps):
    for waterHazard in listOfWaterTraps:
        if ballHitBox.colliderect(waterHazard):
            ballVelocity = [0,0]
            ballHitBox = ballHitBox.move([-(ballHitBox.left), -(ballHitBox.top)])
    return ballHitBox, ballVelocity

#Rotates Images
def rotateImage(image, rotate90NumTimes):
    rotatedImage = pygame.transform.rotate(image, -rotate90NumTimes*90)
    return rotatedImage

#The Main Game Loop
while gameState != "Quit":

        #Time Delay
        pygame.time.delay(15)
        
        #User is currently on the title screen
        if gameState == "Title":
            titleScreen = pygame.display.set_caption("Octo-Golf: Title Screen")
            titleScreen = pygame.display.set_mode(titleScreenSize)
            
            #Display Title Screen Text
            titleScreen.blit(titleScreenImage, titleScreenImageRect)

            pygame.display.flip()

            for event in pygame.event.get():
                    #if event.key == pygame.K_ESCAPE:
                    #        gameState = "Quit"
                    if event.type == pygame.QUIT:
                            gameState = "Quit"
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                gameState = "Quit"
                            else:
                               gameState = "Playing"
                               playScreen = pygame.display.set_caption("Octo-Golf: Game Screen")
                               playScreen = pygame.display.set_mode(playScreenSize)

        #User is currently on the playing the game
        if gameState == "Playing":

            #Draw Sand Traps
            playScreen.blit(playingScreenImage, playingScreenImageRect)
            playScreen.blit(sandTrap, sandTrapHitBox1)
            playScreen.blit(sandTrap, sandTrapHitBox2)
            playScreen.blit(sandTrap, sandTrapHitBox3)
            playScreen.blit(sandTrap, sandTrapHitBox4)
            playScreen.blit(sandTrap, sandTrapHitBox5)
            playScreen.blit(sandTrap, sandTrapHitBox6)
            playScreen.blit(sandTrap, sandTrapHitBox7)
            playScreen.blit(sandTrap, sandTrapHitBox8)

            #Draw Water Traps
            playScreen.blit(waterTrap, waterTrapHitBox1)
            playScreen.blit(waterTrap, waterTrapHitBox2)
            playScreen.blit(waterTrap, waterTrapHitBox3)
            playScreen.blit(waterTrap, waterTrapHitBox4)
            playScreen.blit(waterTrap, waterTrapHitBox5)
            playScreen.blit(waterTrap, waterTrapHitBox6)
            playScreen.blit(waterTrap, waterTrapHitBox7)
            playScreen.blit(waterTrap, waterTrapHitBox8)
            playScreen.blit(waterTrap, waterTrapHitBox9)
            playScreen.blit(waterTrap, waterTrapHitBox10)
            playScreen.blit(waterTrap, waterTrapHitBox11)
            playScreen.blit(waterTrap, waterTrapHitBox12)

            #Draw Golf Hole
            playScreen.blit(golfHole, golfHoleHitBox)

            #Draw Golf Ball
            playScreen.blit(golfBall, golfBallHitBox)
            
            #Draw Walls
            playScreen.blit(golfWall,golfWallHitBox1)
            playScreen.blit(golfWall,golfWallHitBox2)
            playScreen.blit(golfWall,golfWallHitBox3)
            playScreen.blit(golfWall,golfWallHitBox4)
            playScreen.blit(golfWall,golfWallHitBox5)
            playScreen.blit(golfWall,golfWallHitBox6)
            playScreen.blit(golfWall,golfWallHitBox7)
            playScreen.blit(golfWall,golfWallHitBox8)
            playScreen.blit(golfWall,golfWallHitBox9)
            playScreen.blit(golfWall,golfWallHitBox10)
            playScreen.blit(golfWall,golfWallHitBox11)
            playScreen.blit(golfWall,golfWallHitBox12)
            playScreen.blit(golfWall,golfWallHitBox13)
            playScreen.blit(golfWall,golfWallHitBox14)
            playScreen.blit(golfWall,golfWallHitBox15)
            playScreen.blit(golfWall,golfWallHitBox16)
            playScreen.blit(golfWall,golfWallHitBox17)
            playScreen.blit(golfWall,golfWallHitBox18)
            playScreen.blit(golfWall,golfWallHitBox19)
            playScreen.blit(golfWall,golfWallHitBox20)
            playScreen.blit(golfWall,golfWallHitBox21)       

            #Count the number of toggle ON direction keys
            currentDirectionKeysPressedCount = leftDirectionPressed + rightDirectionPressed + upDirectionPressed + downDirectionPressed

            #Cycle Through Power Settings
            if hitSpeedSwtichCounter == 0:
                hitSpeed = highHitSpeed
                playScreen.blit(highPoweredSymbol, highPoweredRect)
            if hitSpeedSwtichCounter == 1:
                hitSpeed = mediumHitSpeed
                playScreen.blit(mediumPoweredSymbol, mediumPoweredRect)
            if hitSpeedSwtichCounter == 2:
                hitSpeed = lowHitSpeed
                playScreen.blit(lowPoweredSymbol, lowPoweredRect)
            if hitSpeedSwtichCounter >= 3:
                hitSpeedSwtichCounter = 0

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        gameState = "Quit"

                if event.type == pygame.KEYDOWN and currentGolfBallVelocity[0] == 0 and currentGolfBallVelocity[1] == 0:

                        #Toggle Direction Keys
                        if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and (currentDirectionKeysPressedCount < 2 or leftDirectionPressed) and rightDirectionPressed == False:
                                leftDirectionPressed = not leftDirectionPressed
                        if (event.key == pygame.K_w or event.key == pygame.K_UP) and (currentDirectionKeysPressedCount < 2 or upDirectionPressed) and downDirectionPressed == False:
                                upDirectionPressed = not upDirectionPressed
                        if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and (currentDirectionKeysPressedCount < 2 or downDirectionPressed) and upDirectionPressed == False:
                                downDirectionPressed = not downDirectionPressed
                        if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (currentDirectionKeysPressedCount <  2 or rightDirectionPressed) and leftDirectionPressed == False:
                                rightDirectionPressed = not rightDirectionPressed
                        if event.key == pygame.K_SPACE:
                            hitSpeedSwtichCounter += 1
                            golfBallHitBox.move(-(golfBallHitBox.left), -(golfBallHitBox.top))
                        if event.key == pygame.K_ESCAPE:
                            gameState = "Quit"

                        #User Confirm the hit on the golf ball and the hitspeed is added to the golf ball velocity
                        if event.key == pygame.K_RETURN and currentDirectionKeysPressedCount > 0:
                                if leftDirectionPressed and not rightDirectionPressed:
                                        currentGolfBallVelocity[0] = -hitSpeed
                                if rightDirectionPressed and not leftDirectionPressed:
                                        currentGolfBallVelocity[0] = hitSpeed
                                if downDirectionPressed and not upDirectionPressed:
                                        currentGolfBallVelocity[1] = hitSpeed
                                if upDirectionPressed and not downDirectionPressed:
                                        currentGolfBallVelocity[1] = -hitSpeed

                                #Reset Key States
                                leftDirectionPressed  = False
                                rightDirectionPressed = False
                                upDirectionPressed    = False
                                downDirectionPressed  = False

                                #Increment Golf Ball Hit Count
                                golfBallHitCounter += 1

            #Determine ball collisions
            golfBallHitBox, currentGolfBallVelocity = collideWithWall(golfBallHitBox, currentGolfBallVelocity, listOfWallHitBoxs)
            friction = collideWithSand(golfBallHitBox, listOfSandTraps, friction, sandFriction, grassFriction)
            golfBallHitBox, currentGolfBallVelocity = collideWithWater(golfBallHitBox, currentGolfBallVelocity, listOfWaterTraps)

            #Move the golf ball using the current velocity
            golfBallHitBox = golfBallHitBox.move(currentGolfBallVelocity)

            #Calculate the current golf ball velocity
            if abs(currentGolfBallVelocity[0]) > 0:
                    currentGolfBallVelocity[0] = currentGolfBallVelocity[0] - (abs(currentGolfBallVelocity[0])/currentGolfBallVelocity[0]) * friction
                    if abs(currentGolfBallVelocity[0]) < friction:
                        currentGolfBallVelocity[0] = 0
            if abs(currentGolfBallVelocity[1]) > 0:
                    currentGolfBallVelocity[1] = currentGolfBallVelocity[1] - (abs(currentGolfBallVelocity[1])/currentGolfBallVelocity[1]) * friction
                    if abs(currentGolfBallVelocity[1]) < friction:
                        currentGolfBallVelocity[1] = 0

            #Display Arrow Keys To User When They Are Pressed and the Hit Power Level
            if leftDirectionPressed  == True:
                    playScreen.blit(leftArrowKey, leftArrowKeyHitBox)
            if rightDirectionPressed == True:
                    playScreen.blit(rightArrowKey, rightArrowKeyHitBox)
            if upDirectionPressed    == True:
                    playScreen.blit(upArrowKey, upArrowKeyHitBox)
            if downDirectionPressed  == True:
                    playScreen.blit(downArrowKey, downArrowKeyHitBox)

            #Determine Wining Stats
            if (golfBallHitBox.left + 20 > golfHoleHitBox.left) and (golfBallHitBox.left + 20 < golfHoleHitBox.right) and (golfBallHitBox.top + 20 > golfHoleHitBox.top) and (golfBallHitBox.top + 20 < golfHoleHitBox.bottom) and (currentGolfBallVelocity[0] <= 7 and currentGolfBallVelocity[1] <= 7):
                    gameState = "Win"
                    winScreen = pygame.display.set_caption("Octo-Golf: Win Screen")
                    winScreen = pygame.display.set_mode(winScreenSize)
                    
            pygame.display.flip()

        #User has won the game
        if gameState == "Win":
            winScreen.blit(winningScreenImage, winningScreenImageRect)

            #Update Hit Counter Display
            golfBallHitCounterDisplay = arialFont30Point.render(str(golfBallHitCounter), True, BLACK)
            winScreen.blit(golfBallHitCounterDisplay, golfBallHitCounterRect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameState = "Quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameState = "Quit"

#Exit Cleanly
pygame.quit()
sys.exit()