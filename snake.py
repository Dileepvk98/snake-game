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
    
    def growSnake(self):
        self.length += 1 

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
    
    def moveBody(self):
        self.body.append([self.head_x, self.head_y])
        if len(self.body) > self.length:
            self.body.pop(0) 

    def moveSnake(self):
        if self.direction == "RIGHT":
            self.head_x += MOVE_RATE
        elif self.direction == "UP":
            self.head_y -= MOVE_RATE
        elif self.direction == "DOWN":
            self.head_y += MOVE_RATE
        elif self.direction == "LEFT":
            self.head_x -= MOVE_RATE    

        self.moveBody()
        self.checkCollision()
        self.whenOutOfBounds()
        self.dispScore()
        self.drawSnake()     
 
    def dispGameOver(self):
        text = font.render("GAME OVER !",True,WHITE)
        screen.blit(text, [w/2-50, h/2-50])
        text = font.render("SCORE : "+str(self.score),True,WHITE)
        screen.blit(text, [w/2-40, h/2])
        text = font.render("HIT SPACEBAR TO RESTART",True,WHITE)
        screen.blit(text, [w/2-100, h/2+50])
        pygame.display.flip()

class Food:
    def __init__(self,colour):
        self.x = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.y = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.colour = colour
        
    def drawFood(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, SIZE, SIZE])

    def checkifyouatefood(self,snake):
        if snake.head_x == self.x and snake.head_y == self.y:
            snake.growSnake()
            snake.score += PTS
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

    screen.fill(BLACK)
    food.drawFood()
    food.checkifyouatefood(snake)
    snake.moveSnake()
   
    fps_obj.tick(fps)
    if not snake.collided:
        pygame.display.flip()
