"""
platformer.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Background
black = Color(0x000000, 1)
white = Color(0xffffff, 1)
brickcolor= Color(0x660011, 1)
noline = LineStyle(0, black)
line1= LineStyle(1,black)
grid=RectangleAsset(20, 20, line1, white)
Sprite(grid, (0,0))
width=list(range(0,60))
height=list(range(0,30))


for x in width:
    for y in height:
        Sprite(grid, (x*20, y*20))

brick_asset=RectangleAsset(20,20,line1, brickcolor)

class brickwall(Sprite)

def __init__(self, position):
    super().__init__(brick_asset.asset, position)
    
    wall.listenKey



myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()