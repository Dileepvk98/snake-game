import random
import pygame

pygame.font.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
font = pygame.font.SysFont('Arial', 15, False, False)
eat_sound = pygame.mixer.Sound("beep.wav")
crash_sound = pygame.mixer.Sound("crash.wav")
size = (640, 640)
screen = pygame.display.set_mode(size)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption("SNAKE")
fps_obj = pygame.time.Clock()
fps = 12
GRIDSIZE = 20
NO_OF_GRIDS = (w-GRIDSIZE)/GRIDSIZE
MOVE_RATE = 20
SIZE = 15
EXIT_GAME = False
PTS=1
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GREEN = (30, 200, 30) 
RED   = (255, 0, 0) 
BLUE  = (0, 100, 255)

class Snake:
    def __init__(self, colour):
        self.length = 10
        self.head_x = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.head_y = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.body = [[self.head_x,self.head_y]]
        self.colour = colour
        self.score = 0
        self.direction = "UP"
        self.collided = False
 
    def dispScore(self):
        text = font.render("SCORE : "+str(self.score),True,WHITE)
        screen.blit(text, [20, 10])   
    
<<<<<<< HEAD
    def growSnake(self):
        self.length += 1 
=======
class SnakeSegment:
    gotfood=False
    length=3
    x=NO_OF_GRIDS/2*GRIDSIZE
    y=NO_OF_GRIDS/2*GRIDSIZE
    direction=0   
    prev_direction=5     

#create instances
food=Food()
segment=SnakeSegment()

#draw functions
def drawRect(screen,color,xylw):
    pygame.draw.rect(screen,color,[xylw[0],xylw[1],xylw[2],xylw[3]])

def drawFood():
    drawRect(screen,RED,[food.x,food.y,SIZE,SIZE])

def dispStart():
    text = font.render("Hit any ARROW KEY to START",True,WHITE)
    screen.blit(text, [w/2-120,h/2+50])

def dispScore():
    text = font.render("SCORE : "+str(SCORE),True,WHITE)
    screen.blit(text, [15, 10])

def dispGameOver():
    screen.fill(BLACK)
    drawSnake(screen,GREEN)
    dispScore()
    text = font.render("GAME OVER !",True,WHITE)
    screen.blit(text, [w/2-50, h/2-50])
    # text = font.render("Press SPACE to start a new game",True,WHITE)
    # screen.blit(text, [w/2-120,h/2-50])
    pygame.display.flip()
>>>>>>> 7f16d84fb90bbf56e3214d884e6455ffcd747af2

    def drawSnake(self):
        for block in self.body:
            pygame.draw.rect(screen, self.colour, [block[0], block[1], SIZE, SIZE]) 
    
    def whenOutOfBounds(self):
        if snake.head_x > w :
            snake.head_x=-20
        elif snake.head_x < 0 :
            snake.head_x=w
        elif snake.head_y > h :
            snake.head_y=-20
        elif snake.head_y < 0 :
            snake.head_y=h           
 
    def resetGame(self):
        self.collided = False
        self.score = 0
        self.length = 3 
        while len(self.body) > self.length:
            self.body.pop(0) 

    def checkCollision(self):
        for segment in self.body[:-2]:
            if segment == [self.head_x, self.head_y]:
                self.collided = True  
                self.dispGameOver()
                pygame.display.flip()     
    
<<<<<<< HEAD
    def moveBody(self):
        self.body.append([self.head_x, self.head_y])
        if len(self.body) > self.length:
            self.body.pop(0) 

    def moveSnake(self, direction):
        if direction == "RIGHT":
            self.head_x += MOVE_RATE
        elif direction == "UP":
            self.head_y -= MOVE_RATE
        elif direction == "DOWN":
            self.head_y += MOVE_RATE
        elif direction == "LEFT":
            self.head_x -= MOVE_RATE    

        self.moveBody()
        self.checkCollision()
        self.whenOutOfBounds()
        self.dispScore()
        self.drawSnake()     
 
    def dispGameOver(self):
        text = font.render("GAME OVER !",True,WHITE)
        screen.blit(text, [w/2-50, h/2])
        text = font.render("HIT SPACEBAR TO RESTART",True,WHITE)
        screen.blit(text, [w/2-100, h/2+25])
        pygame.display.flip()
=======
    collided=checkCollision()
    if collided:
        return True

    whenOutOfBounds()
    tailControl(segment.x,segment.y)
    return False

def checkifyouatefood():
    global SCORE
    if segment.x==food.x and segment.y==food.y:
            eat_sound.play()              
            segment.gotfood=True
            SCORE+=1
            food.x=random.randint(0,NO_OF_GRIDS)*GRIDSIZE
            food.y=random.randint(0,NO_OF_GRIDS)*GRIDSIZE

def growSnake():
    if segment.gotfood==True:
        segment.length+=1
        segment.gotfood=False

#main game loop
while not exitgame:
>>>>>>> 7f16d84fb90bbf56e3214d884e6455ffcd747af2

class Food:
    def __init__(self,colour):
        self.x = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.y = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.colour = colour
    def drawFood(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, SIZE, SIZE])
    def checkifyouatefood(self,snake,pts):
        if snake.head_x == self.x and snake.head_y == self.y:
            snake.growSnake()
            snake.score += pts
            self.x = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
            self.y = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
            eat_sound.play()
            self.drawFood()

snake = Snake(BLUE)
food = Food(RED)

while not EXIT_GAME:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT_GAME = True
        elif event.type == pygame.KEYDOWN:
<<<<<<< HEAD
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
            elif event.key == pygame.K_SPACE:
                snake.resetGame()
=======
            if event.key == pygame.K_UP:
                if segment.prev_direction != 2:
                    segment.direction=1  
            elif event.key == pygame.K_DOWN:
                if segment.prev_direction != 1:
                    segment.direction=2  
            elif event.key == pygame.K_LEFT:
                if segment.prev_direction != 4:
                    segment.direction=3     
            elif event.key == pygame.K_RIGHT:
                if segment.prev_direction != 3:
                    segment.direction=4  
            # elif event.key == pygame.K_SPACE:
            #     gameover=False
            #     collided=False
            #     segment.length=3
            moved=True
>>>>>>> 7f16d84fb90bbf56e3214d884e6455ffcd747af2

    screen.fill(BLACK)
    food.drawFood()
    food.checkifyouatefood(snake,PTS)
    snake.moveSnake(snake.direction)
   
    fps_obj.tick(fps)
    if not snake.collided:
        pygame.display.flip()
    