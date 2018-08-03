import random
import pygame
from multiprocessing.connection import Client

pygame.font.init()
font = pygame.font.SysFont('Arial', 15, False, False)
size = (500, 500)
screen = pygame.display.set_mode(size)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption("SNAKE CLIENT")
fps_obj = pygame.time.Clock()
fps = 12

address = ('127.0.0.1', 6000)
conn = Client(address, authkey='secret password')

GRIDSIZE = 20
NO_OF_GRIDS = (w-GRIDSIZE)/GRIDSIZE
MOVE_RATE = 20
SIZE = 15
EXIT_GAME = False
COLLIDED = False
START = False
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GREEN = (30, 200, 30) 
RED   = (255, 0, 0) 
BLUE  = (0, 100, 255)

def send_data(snake_head_x,snake_head_y,direction,length):
    conn.send("start")
    conn.send(snake_head_x)
    conn.send(snake_head_y)
    conn.send(length)
    conn.send(direction)

class Player:
    def __init__(self,colour,name):
        self.snake = Snake(colour)
        self.food = Food(colour)
        self.name = name
        self.score = 0
        self.out_of_bound = True
        self.direction = "RIGHT"
    
    def whenOutOfBounds(self):
        if self.snake.head_x>w:
            self.out_of_bound = True
            send_data(-20, self.snake.head_y, self.direction,self.snake.length)
                   
        elif self.snake.head_x<0:
            self.out_of_bound = True
            send_data(w, self.snake.head_y, self.direction,self.snake.length)
                   
        elif self.snake.head_y>h:   
            self.snake.head_y = -20     
        elif self.snake.head_y<0:
            self.snake.head_y = h 

class Food:
    def __init__(self,colour):
        self.x = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.y = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.colour = colour

    def generate(self,body):
        for block in body:
            self.x = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
            self.y = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
            if block[0] != self.x or block[1] != self.y:
                break
        self.drawFood()

    def drawFood(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, SIZE, SIZE])

    def checkifyouatefood(self,player):
        if player.snake.head_x == self.x and player.snake.head_y == self.y:
            player.snake.growSnake()
            player.score += 1
            self.generate(player.snake.body)

class Snake:
    def __init__(self, colour):
        self.length = 10
        self.head_x = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.head_y = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.body = [[self.head_x,self.head_y]]
        self.colour = colour

    def drawSnake(self):
        for block in self.body:
            pygame.draw.rect(screen, self.colour, [block[0], block[1], SIZE, SIZE])

    def growSnake(self):
        self.length += 1

    def moveSnake(self, direction,bound):
        if direction == "RIGHT":
            self.head_x += MOVE_RATE
        elif direction == "UP":
            self.head_y -= MOVE_RATE
        elif direction == "DOWN":
            self.head_y += MOVE_RATE
        elif direction == "LEFT":
            self.head_x -= MOVE_RATE
        
        self.moveBody(bound)
        self.drawSnake()

    def moveBody(self,bound):
        if bound:
            self.body.pop(0)
        else:
            self.body.append([self.head_x, self.head_y])
            if len(self.body) > self.length:
                self.body.pop(0)       

p1 = Player(BLUE,"P1")

while not EXIT_GAME :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            conn.send("stop")
            EXIT_GAME = True
        # event handling
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and p1.direction != "DOWN":
                p1.direction = "UP"
            elif event.key == pygame.K_DOWN and p1.direction != "UP":
                p1.direction = "DOWN"
            elif event.key == pygame.K_LEFT and p1.direction != "RIGHT":
                p1.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and p1.direction != "LEFT":
                p1.direction = "RIGHT"
    
    screen.fill(BLACK)

    p1.food.drawFood()
    p1.food.checkifyouatefood(p1)

    if not p1.out_of_bound:
        p1.whenOutOfBounds()       
    else:
        if len(p1.snake.body) == 0:
            condition = conn.recv()
            if condition == "start":
                p1.out_of_bound = False
                p1.snake.head_x = conn.recv()
                p1.snake.head_y = conn.recv() 
                p1.snake.length = conn.recv()
                p1.direction = conn.recv()
            
    p1.snake.moveSnake(p1.direction,p1.out_of_bound)
    fps_obj.tick(fps)
    pygame.display.flip()

conn.close()