# Arcane Game

import pygame, sys, random, time

pygame.init()

screenWidth = 1920
screenHeight = 1080

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
fps = 60

font = pygame.font.Font('assets/fonts/Wayfarers.ttf', 32)
bigFont = pygame.font.Font('assets/fonts/Wayfarers.ttf', 64)
titleFont = pygame.font.Font('assets/fonts/Wayfarers.ttf', 96)

# Game

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        image = pygame.image.load("assets/img/buttonPlay.png").convert_alpha()
        self.image = pygame.transform.scale(image, (128, 128))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y
        self.pressed = False
    
    def Update(self):
        self.rect.x, self.rect.y = self.x, self.y
        mx, my = pygame.mouse.get_cursor()
        if self.rect.collidepoint(self.x, self.y):
            self.pressed = True
    
    def Draw(self):
        screen.blit(self.image, (self.x, self.y))

def DrawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def GetInputs():
    global keys
    global mx, my
    global clickPressed
    global events
    keys = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    clickPressed = pygame.mouse.get_pressed()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

def MainMenu():
    print("Going to Main Menu...")

    # Initiialise
    prevTime = time.time()
    background = pygame.image.load("assets/img/background.png").convert()

    gameLoop = True
    while gameLoop:
        clock.tick(fps)
        screen.fill((0, 0, 0))
        deltaTime = time.time() - prevTime
        GetInputs()

        # Logic
        screen.blit(background, (0, 0))

        # Text
        DrawText("Peculium", titleFont, (255, 255, 255), screen, 550, 200)

        pygame.display.update()

def Game():
    print("Starting game...")
    prevTime = time.time()

    gameLoop = True
    while gameLoop:
        clock.tick(fps)
        screen.fill((0, 0, 0))
        deltaTime = time.time() - prevTime

        GetInputs()
        MainMenu()

        pygame.display.update()


Game()