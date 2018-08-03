import pygame
import snake


<<<<<<< HEAD
# pygame.font.init()
# font = pygame.font.SysFont('Arial', 15, False, False)

# size=(640,640)
# screen=pygame.display.set_mode(size)
# w, h = pygame.display.get_surface().get_size()
# pygame.display.set_caption("SNAKE")

print snake.SCORE


=======
pygame.font.init()
font = pygame.font.SysFont('Arial', 15, False, False)

size=(640,640)
screen=pygame.display.set_mode(size)
w, h = pygame.display.get_surface().get_size()
pygame.display.set_caption("CONGRATULATIONS !")

print snake.SCORE
# f = open("highscore.txt", "w")
#f.write()
crrent_string = []
display_box(screen, question + ": " + string.join(current_string,""))
while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
    return string.join(current_string,"")
>>>>>>> 7f16d84fb90bbf56e3214d884e6455ffcd747af2
