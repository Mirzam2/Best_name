import block
import mobs
import pygame
import file
from constans import *
import Hume_screen
import pathlib
import inventoty
from not_constant import types_block, person_images


def veb_cam(screen, x, y):
    """
    Фунция вызывающая камеру, которая рисует картинку в зависимости от положения игрока
    main_screen - главный экран на котором должна быть картинка
    x_cam, y_cam - положение камеры в предудущий тик
    """
    speed_cam = 1  # коэфициент пропорциональности скорости
    max_distant = 2 * SIZE_BLOCK  # максимальное удаление
    cam_screen = pygame.Surface(
        (SIZE_MAP_X * SIZE_BLOCK, SIZE_MAP_Y * SIZE_BLOCK))
    main_hero.screen = cam_screen
    # отдаление от центра по X
    diff_x = -main_hero.x * SIZE_BLOCK + screen.get_size()[0] / 2 - x
    # отдаление от центра по Y
    diff_y = -main_hero.y * SIZE_BLOCK + screen.get_size()[1] / 2 - y
    "Собственно движение камеры"
    if diff_x >= max_distant:
        x += speed_cam * diff_x / max_distant
    if diff_x <= -max_distant:
        x += speed_cam * diff_x / max_distant
    if diff_y >= max_distant:
        y += speed_cam * diff_y / max_distant
    if diff_y <= -max_distant:
        y += speed_cam * diff_y / max_distant
    file.draw_map(massive_slov, cam_screen)
    main_hero.draw()
    for mob in massive_mobs:
        mob.screen = cam_screen
        mob.draw()
    screen.blit(cam_screen, (x, y))
    return x, y


pygame.init()
main_screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
file_world = pathlib.Path(pathlib.Path.cwd(), "music.wav")
pygame.mixer.music.load(file_world)
pygame.mixer.music.play(-1)
file_world = Hume_screen.home_screen(main_screen)
name_of_file_with_inventory = "Saves_inventory\inventory" + file_world
file_inventory = open(pathlib.Path(pathlib.Path.cwd(),
                                   "Saves_inventory", "inventory" + file_world), 'r')
inventory = inventoty.Inventory(file_inventory, main_screen)
block_in_hands = 0
massive_slov, map_types = file.load_map(file_world)
main_hero = mobs.Person(10, 2, person_images, main_screen)
massive_mobs = list()
massive_mobs.append(mobs.Zombie(20, 5, person_images, main_screen))
x_cam = -main_hero.x * SIZE_BLOCK + main_screen.get_size()[0] / 2
y_cam = -main_hero.y * SIZE_BLOCK + main_screen.get_size()[1] / 2
finished = False

clock = pygame.time.Clock()
time = 0
pygame.display.update()
while not finished:
    time += 1
    main_screen.fill((0, 0, 0))
    '''начало блока рисования'''
    x_cam, y_cam = veb_cam(main_screen, x_cam, y_cam)
    '''конец блока рисования'''
    for zombie in massive_mobs:
        zombie.strike = False
    dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.
    if time % 1000 == 0:
        massive_mobs.append(mobs.Zombie(20, 5, person_images, main_screen))
    for event in pygame.event.get():
        main_hero.angle(event, x_cam, y_cam)
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            main_hero.start_time = pygame.time.get_ticks()
            if event.button == 3:
                main_hero.build(block_in_hands, massive_slov,
                                inventory)
            main_hero.hit(event, massive_mobs)
        main_hero.angle(event, x_cam, y_cam)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        block_in_hands = inventoty.inventory_screen(
            main_screen, inventory, block_in_hands)
    """
    Обработка событий связанных с персонажем и зомби
    """
    main_hero.broke(massive_slov, inventory)
    main_hero.input()
    main_hero.update_frame_dependent()
    "Обработка событий связанных с зомби"
    for zombie in massive_mobs:
        zombie.input_zombie(main_hero)
        zombie.update_frame_dependent()
        finished = zombie.kick(main_hero, finished)
        zombie.control_collision(massive_slov)
        zombie.move()
    main_hero.control_collision(massive_slov)
    main_hero.move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        block_in_hands = inventoty.inventory_screen(
            main_screen, inventory, block_in_hands)
    pygame.display.update()
    pygame.display.flip()
    print(main_hero.life)
file.save_map(massive_slov, file_world)

inventory.save_inventory(name_of_file_with_inventory)
pygame.quit()
