import pygame

SCREEN_WIDTH  = 300
SCREEN_HEIGHT = 400
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Paint')

CANVAS_WIDTH  = SCREEN_WIDTH
CANVAS_HEIGHT = CANVAS_WIDTH
CANVAS        = pygame.Rect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
TILE_SIZE     = 20

DECK_HEIGHT = 100
DECK_COLOR  = (40, 40, 40)
DECK        = pygame.Rect(0, SCREEN_HEIGHT - DECK_HEIGHT, SCREEN_WIDTH, DECK_HEIGHT)

COLOR_RED    = (200, 0, 0)
COLOR_GREEN  = (0, 200, 0)
COLOR_BLUE   = (0, 0, 200)
COLOR_YELLOW = (200, 200, 0)
COLOR_PURPLE = (200, 0, 200)
COLOR_CYAN   = (0, 200, 200)
COLOR_ORANGE = (225, 150, 0)
COLOR_WHITE  = (200, 200, 200)

CURRENT_COLOR = COLOR_RED

BOX_WIDTH  = 65
BOX_HEIGHT = 30

RED_BOX    = pygame.Rect(20, SCREEN_HEIGHT - DECK_HEIGHT + 20, BOX_WIDTH, BOX_HEIGHT)
GREEN_BOX  = pygame.Rect(20 + BOX_WIDTH, SCREEN_HEIGHT - DECK_HEIGHT + 20, BOX_WIDTH, BOX_HEIGHT)
BLUE_BOX   = pygame.Rect(20 + BOX_WIDTH * 2, SCREEN_HEIGHT - DECK_HEIGHT + 20, BOX_WIDTH, BOX_HEIGHT)
YELLOW_BOX = pygame.Rect(20 + BOX_WIDTH * 3, SCREEN_HEIGHT - DECK_HEIGHT + 20, BOX_WIDTH, BOX_HEIGHT)
PURPLE_BOX = pygame.Rect(20, SCREEN_HEIGHT - DECK_HEIGHT + 20 + BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT)
CYAN_BOX   = pygame.Rect(20 + BOX_WIDTH, SCREEN_HEIGHT - DECK_HEIGHT + 20 + BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT)
ORANGE_BOX = pygame.Rect(20 + BOX_WIDTH * 2, SCREEN_HEIGHT - DECK_HEIGHT + 20 + BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT)
WHITE_BOX  = pygame.Rect(20 + BOX_WIDTH * 3, SCREEN_HEIGHT - DECK_HEIGHT + 20 + BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT)

drawedTiles = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if RED_BOX.collidepoint(mousePos):
                CURRENT_COLOR = COLOR_RED
            elif GREEN_BOX.collidepoint(mousePos):
                CURRENT_COLOR = COLOR_GREEN
            elif BLUE_BOX.collidepoint(mousePos):
                CURRENT_COLOR = COLOR_BLUE
            elif YELLOW_BOX.collidepoint(mousePos):
                CURRENT_COLOR = COLOR_YELLOW
            elif PURPLE_BOX.collidepoint(mousePos):
                CURRENT_COLOR = COLOR_PURPLE
            elif CYAN_BOX.collidepoint(mousePos):
                CURRENT_COLOR = COLOR_CYAN
            elif ORANGE_BOX.collidepoint(mousePos):
                CURRENT_COLOR = COLOR_ORANGE
            elif WHITE_BOX.collidepoint(mousePos):
                CURRENT_COLOR = COLOR_WHITE

    if pygame.mouse.get_pressed()[0]:
        mousePos = pygame.mouse.get_pos()
        tileX = mousePos[0] // TILE_SIZE
        tileY = mousePos[1] // TILE_SIZE
        drawedTiles.append([tileX, tileY, CURRENT_COLOR])

    SCREEN.fill((0, 0, 0))

    for tile in drawedTiles:
        pygame.draw.rect(SCREEN, tile[2], pygame.Rect(tile[0] * TILE_SIZE, tile[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.draw.rect(SCREEN, DECK_COLOR, DECK)
    pygame.draw.rect(SCREEN, COLOR_RED, RED_BOX)
    pygame.draw.rect(SCREEN, COLOR_GREEN, GREEN_BOX)
    pygame.draw.rect(SCREEN, COLOR_BLUE, BLUE_BOX)
    pygame.draw.rect(SCREEN, COLOR_YELLOW, YELLOW_BOX)
    pygame.draw.rect(SCREEN, COLOR_PURPLE, PURPLE_BOX)
    pygame.draw.rect(SCREEN, COLOR_CYAN, CYAN_BOX)
    pygame.draw.rect(SCREEN, COLOR_ORANGE, ORANGE_BOX)
    pygame.draw.rect(SCREEN, COLOR_WHITE, WHITE_BOX)

    pygame.display.update()
