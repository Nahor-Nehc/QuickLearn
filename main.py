import pygame, sys, os
import pygmtlsv4dot1 as tools


pygame.init()

PADDING = 20

WIDTH, HEIGHT = 600, 700
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
FLASHCARD_WIDTH, FLASHCARD_HEIGHT = 400, 200
RETURN_TO_MENU_WIDTH, RETURN_TO_MENU_HEIGHT = 60, 60

ARROW_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "arrow.png")), (RETURN_TO_MENU_WIDTH-PADDING/2, RETURN_TO_MENU_HEIGHT-PADDING/2))

INITIAL_TIME = 10

MAX_LIVES = 5

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word bomb")

BLACK =  (  0,   0,   0)
WHITE =  (255, 255, 255)
RED =    (211,   0,   0)
GREEN =  (  0, 150,   0)
DGREEN = (  0, 100,   0)
BLUE =   (  0,   0, 211)
LBLUE =  (137, 207, 240)
GREY =   (201, 201, 201)
LGREY =  (231, 231, 231)
DGREY =  ( 50,  50,  50)
LBROWN = (185, 122,  87)
DBROWN = (159, 100,  64)

DURATION = 200 #ms
FPS = 60

FONT = lambda x: pygame.font.SysFont("consolas.ttf", x)

CREATE = pygame.USEREVENT + 1
FLASHCARDS = pygame.USEREVENT + 2
GO_TO_MENU = pygame.USEREVENT + 3

def drawWin(state, buttons, flashcard_rect):
  pygame.draw.rect(WIN, WHITE, pygame.Rect(0, 0, WIDTH, HEIGHT))

  buttons.draw(WIN)
  
  if state == "create" or state == "flashcards":
    WIN.blit(ARROW_IMAGE, (PADDING/4, PADDING/4))
    pygame.draw.rect(WIN, LGREY, flashcard_rect, 2)
  
  pygame.display.flip()

def main():
  
  buttons = tools.Button()
  
  create_rect = pygame.Rect(WIDTH/2-BUTTON_WIDTH/2, HEIGHT*2/3, BUTTON_WIDTH, BUTTON_HEIGHT)
  buttons.create(create_rect, LGREY, CREATE, text = "CREATE", font = FONT(30), textColour=BLACK)
  
  flashcards_rect = pygame.Rect(WIDTH/2-BUTTON_WIDTH/2, HEIGHT*1/3, BUTTON_WIDTH, BUTTON_HEIGHT)
  buttons.create(flashcards_rect, LGREY, FLASHCARDS, text = "FLASHCARDS", font = FONT(30), textColour=BLACK)
  
  flashcard_rect = pygame.Rect(WIDTH/2-FLASHCARD_WIDTH/2, HEIGHT*1/4, FLASHCARD_WIDTH, FLASHCARD_HEIGHT)
  
  return_to_menu_rect = pygame.Rect(0, 0, RETURN_TO_MENU_WIDTH, RETURN_TO_MENU_HEIGHT)
  buttons.create(return_to_menu_rect, LGREY, GO_TO_MENU, visible=False)
  
  state = "menu"
  
  #initiates the clock
  clock = pygame.time.Clock()
  
  #initiates game loop
  run = True
  while run:
    
    #ticks the clock
    clock.tick(FPS)

    #gets mouse position
    mouse = pygame.mouse.get_pos()
    
    #for everything that the user has inputted ...
    for event in pygame.event.get():

      #if the "x" button is pressed ...
      if event.type == pygame.QUIT:

        #ends game loop
        run = False

        #terminates pygame
        pygame.quit()

        #terminates system
        sys.exit()
        
      elif event.type == pygame.MOUSEBUTTONUP:
        buttons.check(mouse)
        
      elif event.type == CREATE:
        state = "create"
        buttons.toggleVis(flashcards_rect)
        buttons.toggleVis(create_rect)
        buttons.toggleVis(return_to_menu_rect)
        
      elif event.type == FLASHCARDS:
        state = "flashcards"
        buttons.toggleVis(flashcards_rect)
        buttons.toggleVis(create_rect)
        buttons.toggleVis(return_to_menu_rect)
        
      elif event.type == GO_TO_MENU:
        state = "menu"
        buttons.toggleVis(flashcards_rect)
        buttons.toggleVis(create_rect)
        buttons.toggleVis(return_to_menu_rect)
        
    drawWin(state, buttons, flashcard_rect)


main()