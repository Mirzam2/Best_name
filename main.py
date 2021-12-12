from block import *
from mobs import *
import pygame
import button
from file import *
from constans import *
from Hume_screen import *
def veb_cam(main_screen, x_cam, y_cam):
    """
    Фунция вызывающая камеру, которая рисует картинку в зависимости от положения игрока
    main_screen - главный экран на котором должна быть картинка
    x_cam, y_cam - положение камеры в предудущий тик
    """
    size_y = len(massive_slov)
    size_x = len(massive_slov[1])
    speed_cam = 1  # коэфициент пропорциональности скорости
    max_distant = 2 * SIZE_BLOCK  # максимальное удаление
    screen = pygame.Surface((size_x * SIZE_BLOCK, size_y * SIZE_BLOCK))
    main_hero.screen = screen
    # отдаление от центра по X
    diff_x = -main_hero.x * SIZE_BLOCK + main_screen.get_size()[0] / 2 - x_cam
    # отдаление от центра по Y
    diff_y = -main_hero.y * SIZE_BLOCK + main_screen.get_size()[1] / 2 - y_cam
    "Собственно движение камеры"
    if diff_x >= max_distant:
        x_cam += speed_cam * diff_x / max_distant
    if diff_x <= -max_distant:
        x_cam += speed_cam * diff_x / max_distant
    if diff_y >= max_distant:
        y_cam += speed_cam * diff_y / max_distant
    if diff_y <= -max_distant:
        y_cam += speed_cam * diff_y / max_distant
    draw_map(massive_slov, types_block, screen)
    main_hero.draw()
    for i in massive_mobs:
        i.screen = screen
        i.draw()
    main_screen.blit(screen, (x_cam, y_cam))
    return x_cam, y_cam

pygame.init()
main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
file = pathlib.Path(pathlib.Path.cwd(), "Queen Bee-Fire-kissvk.com.wav")
pygame.mixer.music.load(file)
pygame.mixer.music.play(1)
"""
ReoNa-Nainai-kissvk.com.mp3
"""
types_block = {}
person_images = {}
types(types_block, person_images)
file = hyme_screen(main_screen)
massive_slov, map_types = load_map(types_block, file)
size_y = len(massive_slov)
size_x = len(massive_slov[1])
screen = pygame.Surface((size_x * SIZE_BLOCK, size_y * SIZE_BLOCK))
main_hero = Main_person(10, 0, person_images, main_screen)
massive_mobs = []

massive_mobs.append(Zombie(20, 0, main_screen))
massive_mobs.append(Zombie(15, 0, main_screen))
x_cam = -main_hero.x * SIZE_BLOCK + main_screen.get_size()[0] / 2
y_cam = -main_hero.y * SIZE_BLOCK + main_screen.get_size()[1] / 2
finished = False

clock = pygame.time.Clock()
pygame.display.update()
while not finished:
    main_screen.fill((0, 0, 0))
    '''начало блока рисования'''
    x_cam, y_cam = veb_cam(main_screen, x_cam, y_cam)
    '''конец блока рисования'''
    dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            main_hero.start_time = pygame.time.get_ticks()
            if event.button == 3:
                main_hero.build(massive_slov)
        main_hero.angle(event, x_cam, y_cam)
    main_hero.broke(massive_slov, types_block)
    main_hero.input(event=0)
    main_hero.control_collision(massive_slov)
    main_hero.update_frame_dependent()
    for i in massive_mobs:
        i.input(main_hero)
        i.control_collision(massive_slov)
        i.move()
        i.kick(main_hero)
    main_hero.move()
    pygame.display.update()
    pygame.display.flip()

save_map(massive_slov)
pygame.quit()
