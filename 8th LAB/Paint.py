import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("lines")
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    square_size = 50
    square_x, square_y = 0, 0

    circle_radius = 25
    circle_x, circle_y = 0, 0

    draw_square = False
    draw_circle = False

    prev_mouse_x, prev_mouse_y = 0, 0
    
    radius = 15
    mode = 'blue'
    points = []
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    draw_circle = False
                    draw_square = True
                    square_x, square_y = pygame.mouse.get_pos()
                elif event.key == pygame.K_5:
                    draw_square = False
                    draw_circle = True
                    circle_x, circle_y = pygame.mouse.get_pos()
                elif event.key == pygame.K_1:
                    points.clear()
                elif event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)

            
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append(position)
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        if draw_square:
            pygame.draw.rect(screen, RED, (square_x - square_size // 2, square_y - square_size // 2, square_size, square_size))
        elif draw_circle:
            pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width // 2)

main()