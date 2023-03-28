import random
import time
import pygame

pygame.init()

gray = (60, 60, 60)

black = (255, 0, 0)

display = pygame.display.set_mode((800, 700))

pygame.display.set_caption("My racing game")

carimg = pygame.image.load("C:/Users/m.lee/PycharmProjects/python Car racing game/Assets/car1.png")

backgroundleft = pygame.image.load("C:/Users/m.lee/PycharmProjects/python Car racing game/Assets/left.png")

backgroundright = pygame.image.load("C:/Users/m.lee/PycharmProjects/python Car racing game/Assets/right.jpg")

car_width = 23
car_height = 47


def policecar(police_startx, police_starty, police):
    global police_come
    if police == 0:
        police_come = pygame.image.load("C:/Users/m.lee/PycharmProjects/python Car racing game/Assets/car2.png")
    if police == 1:
        police_come = pygame.image.load("C:/Users/m.lee/PycharmProjects/python Car racing game/Assets/car3.png")
    if police == 2:
        police_come = pygame.image.load("C:/Users/m.lee/PycharmProjects/python Car racing game/Assets/car1.png")
    if police == 3:
        police_come = pygame.image.load("C:/Users/m.lee/PycharmProjects/python Car racing game/Assets/car4.png")
    if police == 4:
        police_come = pygame.image.load("C:/Users/m.lee/PycharmProjects/python Car racing game/Assets/car5.png")
    display.blit(police_come, (police_startx, police_starty))


def background():
    display.blit(backgroundleft, (0, 0))

    display.blit(backgroundright, (725, 0))


def crash():
    message_display("Game Over")


def message_display(text):
    large_text = pygame.font.Font("freesansbold.ttf", 80)

    textsurf, textrect = text_object(text, large_text)

    textrect.center = ((400), (300))

    display.blit(textsurf, textrect)
    pygame.display.update()

    time.sleep(3)

    loop()


def text_object(text, font):
    text_surface = font.render(text, True, black)

    return text_surface, text_surface.get_rect()


def car(x, y):

    display.blit(carimg, (x, y))


def loop():
    x = 400
    y = 540

    x_change = 0
    y_change = 0

    policecar_speed = 8
    police = 0

    police_startx = random.randrange(130, (700 - car_width))
    police_starty = -600

    police_width = 23
    police_height = 47

    bumped = False

    while not bumped:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = - 2

                if event.key == pygame.K_RIGHT:
                    x_change = 2

            elif event.type == pygame.KEYUP:
                x_change = 0

        x+=x_change

        display.fill(gray)

        background()
        police_starty -= (policecar_speed / 1.2)
        policecar(police_startx, police_starty, police)

        police_starty += policecar_speed
        car(x, y)

        if x < 50 or x > 750 - car_width:
            crash()
        if y < 75 or y > 675 - car_height:
            crash()

        if police_starty > 600:
            police_starty = 0 - police_height

            police_startx = random.randrange(130, (1000 - 300))

            police = random.randrange(0, 2)

        if y < police_starty + police_height:
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width:
                crash()

        pygame.display.update()


loop()
pygame.quit()
quit()
