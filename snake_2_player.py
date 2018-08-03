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
COLLIDED = False
BONUS_PTS=3
PTS=1
PENALTY_PTS=3

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GREEN = (30, 200, 30) 
RED   = (255, 0, 0) 
BLUE  = (0, 100, 255)

class Player:
    def __init__(self,colour,name):
        self.food = Food(colour)
        self.snake = Snake(colour)
        self.name = name
        self.score = 0
        self.direction = "UP"
        self.collided=False

    def dispScore(self,x,colour):
        text = font.render(self.name+" SCORE : "+str(self.score),True,colour)
        screen.blit(text, [x, 10])
    
    
    def whenOutOfBounds(self):
        global COLLIDED
        # if self.snake.head_x>=w:self.snake.head_x=0
        # elif self.snake.head_x<0:self.snake.head_x=w
        # elif self.snake.head_y>=h:self.snake.head_y=0
        # elif self.snake.head_y<0:self.snake.head_y=h
        if self.snake.head_x<0 or self.snake.head_y<0 or self.snake.head_x>w or self.snake.head_y>h:
            self.collided=True 
        
    def checkCollision(self,otherplayer):
        
        if [self.snake.head_x,self.snake.head_y] in otherplayer.snake.tail:
            if self.score>=PENALTY_PTS:
                self.score-=PENALTY_PTS
            else:
                self.score=0
            otherplayer.score+=PTS

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
        self.draw_food()

    def draw_food(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, SIZE, SIZE])

    def checkifyouatefood(self,player,pts):
        if player.snake.head_x == self.x and player.snake.head_y == self.y:
            player.snake.grow_snake()
            player.score += pts
            eat_sound.play()
            self.generate(player.snake.tail)


class Snake:
    def __init__(self, colour):
        self.length = 3
        self.head_x = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.head_y = random.randint(0, NO_OF_GRIDS)*GRIDSIZE
        self.tail = [[self.head_x,self.head_y]]
        self.colour = colour
        self.is_dead = False

    def drawSnake(self):
        for block in self.tail:
            pygame.draw.rect(screen, self.colour, [block[0], block[1], SIZE, SIZE])

    def grow_snake(self):
        self.length += 1

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
        self.drawSnake()

    def moveBody(self):
        self.tail.append([self.head_x, self.head_y])
        if len(self.tail) > self.length:
            self.tail.pop(0)        


def dispGameOver(str):
        text = font.render(str,True,WHITE)
        screen.blit(text, [w/2-100, h/2])
        pygame.display.flip()
        pygame.exit()

p1 = Player(GREEN,"P1")
p2 = Player(BLUE,"P2")

while not EXIT_GAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            EXIT_GAME = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and p1.direction != "DOWN":
                p1.direction = "UP"
            elif event.key == pygame.K_DOWN and p1.direction != "UP":
                p1.direction = "DOWN"
            elif event.key == pygame.K_LEFT and p1.direction != "RIGHT":
                p1.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and p1.direction != "LEFT":
                p1.direction = "RIGHT"


            elif event.key == pygame.K_w and p2.direction != "DOWN":
                p2.direction = "UP"
            elif event.key == pygame.K_s and p2.direction != "UP":
                p2.direction = "DOWN"
            elif event.key == pygame.K_a and p2.direction != "RIGHT":
                p2.direction = "LEFT"
            elif event.key == pygame.K_d and p2.direction != "LEFT":
                p2.direction = "RIGHT"
    
    screen.fill(BLACK)

    p1.food.draw_food()
    p2.food.draw_food()

    p1.food.checkifyouatefood(p1,PTS)
    p2.food.checkifyouatefood(p2,PTS)
    p1.food.checkifyouatefood(p2,BONUS_PTS)
    p2.food.checkifyouatefood(p1,BONUS_PTS)

    p1.snake.moveSnake(p1.direction)
    p2.snake.moveSnake(p2.direction)
    
    p1.whenOutOfBounds()
    p2.whenOutOfBounds()

    p1.checkCollision(p2)
    p2.checkCollision(p1)

    p1.dispScore(20,p1.snake.colour)
    p2.dispScore(w-120,p2.snake.colour)

    fps_obj.tick(fps)
    if not p1.collided and not p2.collided:
        pygame.display.flip()
    elif p1.collided:
        dispGameOver("PLAYER 2 WINS")
    elif p2.collided:
        dispGameOver("PLAYER 1 WINS")
