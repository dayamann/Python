import pygame
import math
import random
pygame.font.init()

class cube(object):
    across = 40
    w = 600
    def __init__(self , start,directx=1,directy=0,colour=(247, 165, 226)):
        self.pos = start
        self.directx = 1
        self.directy = 0
        self.colour = colour

        
    def move(self, directx, directy):
        self.directx = directx
        self.directy = directy
        self.pos = (self.pos[0] + self.directx, self.pos[1] + self.directy)

    def build(self, face):
        shape = self.w / self.across
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(face, self.colour, (i*shape+1,j*shape+1, shape-2, shape-2))


class snake(object):
    bod = []
    turn = {}
    def __init__(self, colour, pos):
        self.colour = colour
        self.head = cube(pos)
        self.bod.append(self.head)
        self.directx = 0
        self.directy = 1

    def move(self, timer, timer2):
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
        
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.directx = -1
                    self.directy = 0
                    self.turn[self.head.pos[:]] = [self.directx, self.directy]

                elif keys[pygame.K_RIGHT]:
                    self.directx = 1
                    self.directy = 0
                    self.turn[self.head.pos[:]] = [self.directx, self.directy]

                elif keys[pygame.K_UP]:
                    self.directx = 0
                    self.directy = -1
                    self.turn[self.head.pos[:]] = [self.directx, self.directy]

                elif keys[pygame.K_DOWN]:
                    self.directx = 0
                    self.directy = 1
                    self.turn[self.head.pos[:]] = [self.directx, self.directy]

        for x, y in enumerate(self.bod):
            n = y.pos[:]
            if n in self.turn:
                turns = self.turn[n]
                y.move(turns[0],turns[1])
                if x == len(self.bod)-1:
                    self.turn.pop(n)
            else:
                if y.directx == -1 and y.pos[0] <= 0:
                    print('Score: ', len(char.bod))
                    char.restart((10,10))
                    r = 1
                elif y.directx == 1 and y.pos[0] >= y.across-1:
                    print('Score: ', len(char.bod))
                    char.restart((10,10))
                    r = 1
                elif y.directy == 1 and y.pos[1] >= y.across-1:
                    print('Score: ', len(char.bod))
                    char.restart((10,10))
                    r = 1
                elif y.directy == -1 and y.pos[1] <= 0:
                    print('Score: ', len(char.bod))
                    char.restart((10,10))
                    r = 1
                else:
                    y.move(y.directx,y.directy)
                    r = 0

    def restart(self, pos):
        print("YOU HAVE DIED")
        self.head = cube(pos)
        self.bod = []
        self.bod.append(self.head)
        self.turn = {}
        self.directx = 0
        self.directy = 1
        

    def add(self):
        tail = self.bod[-1]
        dirx, diry = tail.directx, tail.directy

        if dirx == 1 and diry == 0:
            self.bod.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dirx == -1 and diry == 0:
            self.bod.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dirx == 0 and diry == 1:
            self.bod.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dirx == 0 and diry == -1:
            self.bod.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.bod[-1].directx = dirx
        self.bod[-1].directy = diry
        

    def build(self, face):
        for x, y in enumerate(self.bod):
            y.build(face)
        

def updated(face, timer):
    global across, width, char, food;
    face.fill((0,0,0))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    level1 = myfont.render('Level 1', False, (127, 87, 229))
    level2 = myfont.render('Level 2', False, (127, 87, 229))
    level3 = myfont.render('Level 3', False, (127, 87, 229))
    level4 = myfont.render('Level 4', False, (127, 87, 229))
    level5 = myfont.render('Level 5', False, (127, 87, 229))

    if timer == 160 or timer == 158 or timer == 156:
        face.blit(level1, (260, 400))  
    elif timer == 100 or timer == 98 or timer == 96:
        face.blit(level2, (260, 400))
    elif timer == 55 or timer == 53 or timer == 51:
        face.blit(level3, (260, 400))
    elif timer == 25 or timer == 23 or timer == 21:
        face.blit(level4, (260, 400))
    elif timer == 10 or timer == 8 or timer == 6:
        face.blit(level5, (260, 400))
    else:
        timer_text = myfont.render(str(timer), False, (127, 87, 229))
        face.blit(timer_text, (250, 400))
    
    char.build(face)
    food.build(face)
    pygame.display.update()


def eat(across, item):

    positions = item.bod

    while True:
        x = random.randrange(across)
        y = random.randrange(across)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)


def main():
    global width, across, char, food, clock
    across = 40
    width = 600
    pygame.display.set_caption("Python")
    window = pygame.display.set_mode((width, width))
    game_intro()
    char = snake((247, 165, 226), (10,10))
    food = cube(eat(across, char), colour=(247, 165, 226))
    flag = True
    clock = pygame.time.Clock()
    timer = 160
    timer2 = 160
    while flag:
        
        timer-=1
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        if timer%10==0:
            timer2-=1

        pygame.time.delay(10)
        if timer2 > 100 and timer2 <= 160:
            clock.tick(8)
        elif timer2 > 55 and timer2 <= 100:
            clock.tick(12)
        elif timer2 > 25 and timer2 <= 55:
            clock.tick(20)
        elif timer2 > 10 and timer2 <= 25:
            clock.tick(25)
        elif timer2 < 10 and timer2 > 0:
            clock.tick(40)
        elif timer2 == 0:
            flag = False
            
        char.move(timer, timer2)

        if char.bod[0].pos == food.pos:
            char.add()
            food = cube(eat(across, char), colour=(247, 165, 226))

        for x in range(len(char.bod)):
            if char.bod[x].pos in list(map(lambda z:z.pos,char.bod[x+1:])):
                print('Score: ', len(char.bod))
                char.restart((10,10))
                break
   
        updated(window, timer2) 

def text_objects(text, font):
    text = font.render(text, True, (255,255,255))
    return text, text.get_rect()

def game_intro():
    pygame.init()
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        window = pygame.display.set_mode((width, width))
        window.fill((247, 165, 226))
        title = pygame.font.SysFont('Comic Sans MS',50)
        subtitle = pygame.font.SysFont('Comic Sans MS',25)
        q, rect = text_objects("Python", title)
        q1, rect1 = text_objects("Click anywhere to begin!", subtitle)
        rect.center = ((width/2),(width/2))
        rect1.center = ((width/2),(width/3))
        window.blit(q, rect)
        window.blit(q1, rect1)
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                intro = False

def game_end():
    pygame.init()
    end = True

    while end:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window = pygame.display.set_mode((width, width))
        window.fill((247, 165, 226))
        title = pygame.font.SysFont('Comic Sans MS',50)
        subtitle = pygame.font.SysFont('Comic Sans MS',25)
        q, rect = text_objects("You win!", title)
        q1, rect1 = text_objects("Congrats...", subtitle)
        rect.center = ((width/2),(width/2))
        rect1.center = ((width/2),(width/3))
        window.blit(q, rect)
        window.blit(q1, rect1)
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                end = False
                pygame.quit()

main()
game_end()
