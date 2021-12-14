import pygame
import button
import json
import block
import pygame.freetype
from constans import *
pygame.font.init()
FPS = 60
clock = pygame.time.Clock()

def new_file(file):
    """
    Заполняет новый файл для сохранения инвентаря
    """
    tmp_block = {}
    result = {}
    block.types(tmp_block, {})
    for i in tmp_block:
        result[i] = 0
    json.dump(result,file)


class Inventory:
    """
    Инвентарь
    Требуется подать фаил с инветарём
    И Pygame.Surface
    """
    def __init__(self, file, screen):
        self.file = file
        self.blocks = {}
        block.types(self.blocks, {})
        self.reverseblock = {}
        for i in self.blocks:
            self.reverseblock[self.blocks[i]] = int(i)
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.main_massive = json.load(file)
        self.massiv_of_buttons = []
        create_buttons(self.main_massive,self.massiv_of_buttons,self.blocks,
            self.width,self.height)
        
    def draw(self, screen):
        """
        Принимает pygame.Surface
        Рискет на нём инвентарь
        """
        f1 = pygame.font.SysFont('arial', 36)
        pygame.draw.rect(screen, (128, 128, 128), (self.width - 3 * self.width // 4,
            self.height - 3 * self.height // 4, self.width // 2, self.height // 2))
        j = 0
        k = 1
        for i in self.main_massive:
            if (j + 1) * 3/2 * 48 + 48 > self.width // 2:
                k = k + 1
                j = 0
            self.blocks[int(i)].draw((self.width - 3 * self.width // 4)/48 + j * 3/2 + 1,
               (self.height - 3 * self.height // 4)/48 + k * 3/2, screen)
            tmp_text = f1.render(str(self.main_massive.get(str(i))), False,
                  (255, 255, 255))
            screen.blit(tmp_text, (self.width - 3 * self.width // 4 + 48 * j * 3/2 + 48,
                      self.height - 3 * self.height // 4 + 48 * k * 3/2))        
            j = j + 1
        self.massiv_of_buttons[0].drawing(screen)


    def add_or_delete_block(self, number_of_block, num):
        """
        Принимает Number_of_block - номер блока и изменяет количество блоков в инвентаре
        Num - количство блоков, которые надо добавить или убрать
        Если Num < 0, то блоки убираются из инвентаря
        Если Num > 0, то блоки добовляются
        Возвращает тот же блок, если они ещё есть
        Если блоки этого типа закончились, то возвращает None
        """
        tmp = self.main_massive.get(str(number_of_block))
        if tmp + num > 0:
            self.main_massive[str(number_of_block)] = tmp + num
            return number_of_block
        else:
            return 0
        

    def event_(self, event):
        """
        Принимает event из pygame.event.get()
        И возвращает тип блока, если блоков не 0
        Возвращает False, если нажали на кнопку выхода
        Возвращает None во всех остальных случаях,
        даже если блоков 0
        """
        for i in self.massiv_of_buttons:
            result = i.tap(event)
            if result != None:
                return result

    def save_inventory(self, file):
        """
        Сохраняет инвентарь в фаил
        Откройте фаил с инвентарём для записи и запустите эту функцию
        """
        json.dump(self.main_massive, file)


def create_buttons(main_massive, massiv_of_buttons, blocks, width, height):
    """
    Создаёт кнопки в инвентаре
    """
    j = 0
    k = 1
    for i in blocks:
        if (j + 1) * 3/2 * 48 + 48 > width // 2:
            k = k + 1
            j = 0
        tmp = button.Button(width - 3 * width // 4 + 48 * j * 3/2 + 48,
           height - 3 * height // 4 + 48 * k * 3/2, 48, 48, return_button,
           (main_massive, i))
        j = j + 1
        massiv_of_buttons.append(tmp)

def return_button(main_massive, i):
    """
    Возвращает блок при нажатии на него,
    если блоков не 0
    В остальных случаях возвращает 0
    """
    print(i)
    if main_massive.get(str(i)) != 0:
        return int(i)
    else: return 0


def inventoryfunction(screen, inventory, block_in_hands):
    finished = False
    result = block_in_hands
    while not finished:
        inventory.draw(screen)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 finished = True
             elif event.type == pygame.MOUSEBUTTONDOWN:
                 preresult = inventory.event_(event)
                 if type(preresult) == int:
                     result = preresult
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            finished = True
        pygame.display.update()
    print(result)
    return result




if __name__ == "__main__":
    screen = pygame.display.set_mode((1000, 1000))
    pygame.init()
    with open ("Saves_inventory\\tmp_invent.json", 'w') as file:
        new_file(file)
    file = open ("Saves_inventory\\tmp_invent.json", 'r')
    m = Inventory(file, screen) 
    finished = False
    while not finished:
        m.draw(screen)
        for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     finished = True
                 elif event.type == pygame.MOUSEBUTTONDOWN:
                     y = m.event_(event)
                     if type(y) == bool:
                         if y == False:
                             finished = y
        pygame.display.update()
