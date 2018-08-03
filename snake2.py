import random
import pygame

#initialize
#pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

font = pygame.font.SysFont('Arial', 15, False, False)
eat_sound = pygame.mixer.Sound("beep.wav")
crash_sound=pygame.mixer.Sound("crash.wav")

size=(640,640)
screen=pygame.display.set_mode(size)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption("SNAKE")

exitgame=False
gameover=False
moved=False
fps_obj=pygame.time.Clock()
fps=30


GRIDSIZE=20
NO_OF_GRIDS=(w-GRIDSIZE)/GRIDSIZE
MOVE_RATE=20
SIZE=15

BLACK = (0, 0, 0)   
WHITE = (255, 255, 255)
GREEN = (30, 200, 30) 
RED   = (255, 0, 0)
BLUE  = (0, 100, 255)

class Food:
    x = random.randint(0,NO_OF_GRIDS)*GRIDSIZE
    y = random.randint(0,NO_OF_GRIDS)*GRIDSIZE

class Snake:
    name=""
    length = 3
    head_x = 0
    head_y = 0
    score = 0
    colour = []
    tail = []   
    direction="RIGHT"

    def __init__(self,name,colour):
        self.head_x=random.randint(0,NO_OF_GRIDS)*GRIDSIZE
        self.head_y=random.randint(0,NO_OF_GRIDS)*GRIDSIZE
        self.colour=colour
        self.name=name
    
    def growSnake(self):
        self.length+=1

    def moveBody(self,x,y):
        self.tail.append([x,y])
        if len(self.tail) > self.length:
            self.tail.pop(0)

    def moveSnake(self,dir):
        if dir=="RIGHT":          
            self.head_x+=MOVE_RATE
        elif dir=="UP" :            
            self.head_y-=MOVE_RATE
        elif dir=="DOWN" :          
            self.head_y+=MOVE_RATE
        elif dir=="LEFT" :         
            self.head_x-=MOVE_RATE

        self.moveBody(self.head_x,self.head_y)
        self.drawSnake()
    
    def drawSnake(self): 
        screen.fill(BLACK)
        for list in self.tail:
            pygame.draw.rect(screen,self.colour,[list[0],list[1],SIZE,SIZE])


#create instances
food1=Food()
food2=Food()
p1=Snake("P1",GREEN)
p2=Snake("P2",BLUE)


#draw functions
def drawFood():
    pygame.draw.rect(screen,RED,[food.x,food.y,SIZE,SIZE])

#main game loop
while not exitgame:
    
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitgame=True

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if direction != "DOWN":
                    direction="UP"  
            elif event.key == pygame.K_DOWN:
                if direction != "UP":
                    direction="DOWN"  
            elif event.key == pygame.K_LEFT:
                if direction != "RIGHT":
                    direction="LEFT"     
            elif event.key == pygame.K_RIGHT:
                if direction != "LEFT":
                    direction="RIGHT"  
    p1.moveSnake(direction)
            # if event.key == pygame.K_w:
            #     if p2.direction != "DOWN":
            #         p2.direction="UP"  
            # elif event.key == pygame.K_s:
            #     if p2.direction != "UP:
            #         direction="DOWN"  
            # elif event.key == pygame.K_a:
            #     if p2.direction != "RIGHT":
            #         direction="LEFT"     
            # elif event.key == pygame.K_d:
            #     if p2.direction != "LEFT:
            #         p2.direction="RIGHT"  
            
    #moved=True
    fps_obj.tick(fps)
    pygame.display.flip()

pygame.quit()