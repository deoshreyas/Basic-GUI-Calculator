import pygame 
from pygame.locals import * 
from pygame_menu import font

pygame.init()

# COLORS 
WHITE = (255, 255, 255)
DARK_GREY = (50, 50, 50)
ORANGE = (255, 105, 0)

# FONTS 
MAIN_FONT = pygame.font.Font(font.FONT_DIGITAL, 50)

# WINDOW DESIGN
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 520
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Basic GUI Calculator")

# PROGRAM CLASSES
class DisplayRect:
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.color = color
        self.text = MAIN_FONT.render(text, True, DARK_GREY)
    def draw(self):
        self.rect = pygame.draw.rect(WINDOW, self.color, (self.x, self.y, self.width, self.height))
        WINDOW.blit(self.text, (self.x, self.y))

class Button(DisplayRect):
    def __init__(self, x, y, width, height, color, text):
        super().__init__(x, y, width, height, color, text)  
    def clicked(self):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                return True 
            else: 
                return False

# DISPLAY SCREEN 
screen = DisplayRect(10, 15, 380, 100, WHITE, "")

# BUTTON OBJECTS 
b1 = Button(10, 130, 87.5, 87.5, WHITE, "1")
b2 = Button(107.5, 130, 87.5, 87.5, WHITE, "2")
b3 = Button(205, 130, 87.5, 87.5, WHITE, "3")
b4 = Button(302.5, 130, 87.5, 87.5, WHITE, "4")
b5 = Button(10, 227.5, 87.5, 87.5, WHITE, "5")
b6 = Button(107.5, 227.5, 87.5, 87.5, WHITE, "6")
b7 = Button(205, 227.5, 87.5, 87.5, WHITE, "7")
b8 = Button(302.5, 227.5, 87.5, 87.5, WHITE, "8")
b9 = Button(10, 325, 87.5, 87.5, WHITE, "9")
b0 = Button(107.5, 325, 87.5, 87.5, WHITE, "0")
badd = Button(205, 325, 87.5, 87.5, WHITE, "+")
bminus = Button(302.5, 325, 87.5, 87.5, WHITE, "-")
bmul = Button(10, 422.5, 87.5, 87.5, WHITE, "x")
bdiv = Button(107.5, 422.5, 87.5, 87.5, WHITE, "/")
beql = Button(205, 422.5, 87.5, 87.5, ORANGE, "=")
bclr = Button(302.5, 422.5, 87.5, 87.5, ORANGE, "C")

running = True 
screenText = ""
expression = ""
while running:
    WINDOW.fill(DARK_GREY)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    # DRAWING DISPLAY SCREEN 
    screen.draw()

    # DRAWING THE BUTTONS ON SCREEN 
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b0.draw()
    badd.draw()
    bminus.draw()
    bmul.draw()
    bdiv.draw()
    beql.draw()
    bclr.draw()

    # LOGIC 
    if b1.clicked():
        expression += "1"
        screenText += "1"
    elif b2.clicked():
        expression += "2"
        screenText += "2"
    elif b3.clicked():
        expression += "3"
        screenText += "3"
    elif b4.clicked():
        expression += "4"
        screenText += "4"
    elif b5.clicked():
        expression += "5"
        screenText += "5"
    elif b6.clicked():
        expression += "6"
        screenText += "6"
    elif b7.clicked():
        expression += "7"
        screenText += "7"
    elif b8.clicked():
        expression += "8"
        screenText += "8"
    elif b9.clicked():
        expression += "9"
        screenText += "9"
    elif b0.clicked():
        expression += "0"
        screenText += "0"
    elif badd.clicked():
        if expression!="" and expression[-1]!="+" and expression[-1]!="-" and expression[-1]!="*" and expression[-1]!="/" and expression[-1]!="^":
            screenText = "+"
            expression += "+"
    elif bminus.clicked():
        if expression=="" or expression[-1]!="-":
            screenText = "-"
            expression += "-"
    elif bmul.clicked():
        if expression!="" and expression[-1]!="+" and expression[-1]!="-" and expression[-1]!="*" and expression[-1]!="/" and expression[-1]!="^":
            screenText = "x"
            expression += "*"
    elif bdiv.clicked():
        if expression!="" and expression[-1]!="+" and expression[-1]!="-" and expression[-1]!="*" and expression[-1]!="/" and expression[-1]!="^":
            screenText = "/"
            expression += "/"
    elif beql.clicked(): # EQUAL TO 
        if (expression!="" and expression[-1]!="+" and expression[-1]!="-" and expression[-1]!="*" and expression[-1]!="/" and expression[-1]!="^" or expression[-1]):
            if not("/0" in expression):
                ans = eval(expression)
                if isinstance(ans, float):
                    ans = round(ans, 2)
                screenText = str(ans)
                expression = str(ans)
            else:
                screenText = ""
                expression = ""
    elif bclr.clicked(): # CLEAR
        expression = ""
        screenText = ""

    # BUFFER DELAY 
    pygame.time.delay(125)

    # UPDATIONS 
    screen.text = MAIN_FONT.render(screenText, True, DARK_GREY)
    
    pygame.display.update()