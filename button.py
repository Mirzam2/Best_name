import pygame
import pygame.freetype


class Button:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, function, option: tuple, color=(255, 255, 255),
                 text="button"):
        """
        Creating a button
        x1,y1 - coordinates of the upper-left corner
        x2,y2 are the coordinates of the lower right corner relative to x1,x2
        function is the function that the button should perform when you click on it, the name of the function itself
        option - the parameters with which the function should be served are served as a tuple
        color - button color
        text - the inscription on the button
        """
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color
        self.text = text
        self.function = function
        self.option = option
        self.font = self.x2 / len(self.text)  # font size
        self.my_font = pygame.freetype.SysFont('Times New Roman', int(self.font))

    def tap(self, event: pygame.event):
        """
        Event processing of type pygame.event.get()
        Returns the value that the button function returns
        """
        if event:
            if (self.x1 <= event.pos[0] <= self.x1 + self.x2) and (self.y1 <= event.pos[1] <= self.y1 + self.y2):
                y = self.function(*self.option)
                return y

    def drawing(self, surface: pygame.Surface):
        """
        Draws a button on the surface of the surface
        """
        pygame.draw.rect(surface, self.color,
                         (self.x1, self.y1, self.x2, self.y2))
        self.my_font.render_to(
            surface, (self.x1 + self.x2 // 4, self.y1 + self.y2 / 2 - self.font // 2), self.text, (0, 0, 0))
