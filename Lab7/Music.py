import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
sound = [
    pygame.mixer.Sound("Brooklyn.MPEG"),
    pygame.mixer.Sound("Chto to ot Myagi.MPEG"),
    pygame.mixer.Sound("Ne znau.MPEG"),
    pygame.mixer.Sound("Samaya Vishka.MPEG"),
    pygame.mixer.Sound("Takwe cht to ot Myagi.MPEG"),
]
sound_name = [
    "Brooklyn",
    "не знаю что за трек",
    "также не знаю",
    "самая вышка",
    "что то от Миаги вроде бы"
]
sound_cnt = 0

myfont = pygame.font.SysFont("Times New Roman", 30)

playmusic = myfont.render("Press Space to play music", True, (255, 255, 255))
nextmusic = myfont.render("Press q to play next music", True, (255, 255, 255))
stopmusic = myfont.render("Press w to stop music", True, (255, 255,255))
previousmusic = myfont.render("Press e to play previous music", True, (255,255,255))


musis_on = False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(playmusic, (50, 0))
    screen.blit(nextmusic, (50, 100))
    screen.blit(stopmusic, (50, 200))
    screen.blit(previousmusic, (50, 300))
    screen.blit(myfont.render(f"Music name : {sound_name[sound_cnt]}", True, (255, 255, 255)), (50, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not musis_on:
                musis_on = True
                sound[sound_cnt].play()
            elif event.key == pygame.K_q:
                musis_on = True
                sound[sound_cnt].stop()
                sound_cnt += 1
                if sound_cnt >= len(sound):
                    sound_cnt = 0
                sound[sound_cnt].play()
            elif event.key == pygame.K_w:
                musis_on = False
                sound[sound_cnt].stop()
            elif event.key == pygame.K_e:
                musis_on = True
                sound[sound_cnt].stop()
                sound_cnt -= 1
                if sound_cnt < 0:
                    sound_cnt = len(sound) - 1
                sound[sound_cnt].play()
    pygame.display.flip()