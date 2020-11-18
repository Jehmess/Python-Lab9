# James Aufleger
# EtchASketch on RaspberryPi - Using GFX HAT


from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

print('etch a sket is a go, use arrow arrow keys to draw. "r" to restart, "q" to quit')
## init loops
quit = False
## Set starting point -- Middle of screen
x = 64
y = 32
## Clear Screen
clearScreen(lcd)
displayText("Etch a Sketch",lcd, 10, 20)
print("press 'c' to clear the screen and start writing")
# While loop
while(quit != True):
    keyPress = getchar()
    ## up
    if (keyPress == '\x1b[A'):
        y -=1
        if (y < 0):
            y = 63
        lcd.set_pixel(x,y,1)
        lcd.show()
    # down
    elif (keyPress == '\x1b[B'):
        y += 1
        if (y > 63):
            y = 0
        lcd.set_pixel(x,y,1)
        lcd.show()
    #right    
    elif (keyPress == '\x1b[C'):
        x +=1
        if(x > 127):
            x = 0
        lcd.set_pixel(x,y,1)
        lcd.show()
    # left    
    elif (keyPress == '\x1b[D'):
        x -= 1
        if(x < 0):
            x = 127
        lcd.set_pixel(x,y,1)
        lcd.show()
    #finish        
    elif (keyPress == 'f'):
        quit = True 
    #clear screen    
    elif(keyPress == 'c'):
        lcd.clear()
        lcd.show()


