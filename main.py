import pygame

SCREEN_WIDTH  = 300
SCREEN_HEIGHT = 400
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Paint')

DECK_HEIGHT = 100
DECK_COLOR  = (40, 40, 40)
DECK        = pygame.Rect(0, SCREEN_HEIGHT - DECK_HEIGHT, SCREEN_WIDTH, DECK_HEIGHT)

COLOR_RED    = (200, 0, 0)
COLOR_GREEN  = (0, 200, 0)
COLOR_BLUE   = (0, 0, 200)
COLOR_YELLOW = (200, 200, 0)

BOX_WIDTH  = 65
BOX_HEIGHT = 30

RED_BOX    = pygame.Rect(20, SCREEN_HEIGHT - DECK_HEIGHT + 20, BOX_WIDTH, BOX_HEIGHT)
GREEN_BOX  = pygame.Rect(20 + BOX_WIDTH, SCREEN_HEIGHT - DECK_HEIGHT + 20, BOX_WIDTH, BOX_HEIGHT)
BLUE_BOX   = pygame.Rect(20 + BOX_WIDTH * 2, SCREEN_HEIGHT - DECK_HEIGHT + 20, BOX_WIDTH, BOX_HEIGHT)
YELLOW_BOX = pygame.Rect(20 + BOX_WIDTH * 3, SCREEN_HEIGHT - DECK_HEIGHT + 20, BOX_WIDTH, BOX_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill((0, 0, 0))

    pygame.draw.rect(SCREEN, DECK_COLOR, DECK)
    pygame.draw.rect(SCREEN, COLOR_RED, RED_BOX)
    pygame.draw.rect(SCREEN, COLOR_GREEN, GREEN_BOX)
    pygame.draw.rect(SCREEN, COLOR_BLUE, BLUE_BOX)
    pygame.draw.rect(SCREEN, COLOR_YELLOW, YELLOW_BOX)

    pygame.display.update()
