from typing import Text
import pygame
import pygame.freetype


class Button():
    def __init__(self, x1, y1, x2, y2, function, option: tuple, color=(255, 255, 255), text="button"):
        """
        Создание кнопки
        x1,y1 - координаты левого вернего угла
        x2,y2 - координаты правого нижнего угла
        function - функция, которая должна выполнять кнопка при нажатии на неё, само название функции
        option - параметры, с которыми должна подаваться функция, подаются в виде кортежа 
        color - цвет кнопки
        text - надпись на кнопке
        """
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color
        self.text = text
        self.function = function
        self.option = option
        self.font = abs(self.x1 - self.x2)/len(text) * 2  # размер шрифта
        self.my_font = pygame.freetype.SysFont('Times New Roman', self.font)

    def tap(self, event):
        if event:
            if (self.x1 <= event.pos[0] <= self.x1 + self.x2) and (self.y1 <= event.pos[1] <= self.y1 + self.y2):
                y = self.function(*self.option)
                return y

    def drawing(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x1, self.y1, self.x2, self.y2))
        self.my_font.render_to(
            surface, (self.x1 + self.x2 / 4 , self.y1 + self.y2 /2 - self.font / 2), self.text, (0, 0, 0))


if __name__ == "__main__":
    pygame.init()
    button = Button(0, 0, 40,40, pygame.quit,
                    (), (255, 255, 255), "lmao0000")
    screen = pygame.display.set_mode((800, 800), pygame.FULLSCREEN)
    button.drawing(screen)
    pygame.display.update()
    finished = False
    while not finished:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button.tap(event)

    pygame.quit()
