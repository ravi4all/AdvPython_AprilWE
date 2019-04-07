import pygame, random
pygame.init()

height = 500
width = 1000
screen = pygame.display.set_mode((width, height))
white = 255,255,255
black = 0,0,0
red = 255,0,0
blue = 0,0,255
green = 0,255,0
colors = [black,red,green,blue]

class Ball():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.moveX = random.random() * 5
        self.moveY = random.random() * 5
        self.color = random.choice(colors)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - 50:
            self.moveX = -random.random() * 5
        elif self.y > height - 50:
            self.moveY = -random.random() * 5
        elif self.x < 0:
            self.moveX = random.random() * 5
        elif self.y < 0:
            self.moveY = random.random() * 5

# ball_1 = Ball()
# ball_2 = Ball()
ballsList = []
n = 100
for i in range(n):
    ball = Ball()
    ballsList.append(ball)

clock = pygame.time.Clock()
FPS = 1000
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # pygame.draw.rect(screen, black, [ball_1.x,ball_1.y,50,50])
    # pygame.draw.rect(screen, black, [ball_2.x, ball_2.y, 50, 50])
    # ball_1.update()
    # ball_2.update()

    for i in range(len(ballsList)):
        pygame.draw.rect(screen, ballsList[i].color, [ballsList[i].x,
                                                      ballsList[i].y, 50, 50])
        ballsList[i].update()

    pygame.display.update()
    clock.tick(FPS)