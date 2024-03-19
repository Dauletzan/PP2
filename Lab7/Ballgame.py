import pygame

pygame.init()
HEIGHT, WIDTH = 600 , 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("ball")

x, y = WIDTH//2, HEIGHT//2
x_change = 0
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_LEFT]) and x > 25:
        x -= 20
    if (pressed[pygame.K_RIGHT]) and WIDTH - 25 > x:
        x += 20
    if (pressed[pygame.K_UP]) and y > 25:
        y -= 20
    if (pressed[pygame.K_DOWN]) and y < HEIGHT - 25:
        y += 20
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (x, y), 25)
    pygame.display.flip()