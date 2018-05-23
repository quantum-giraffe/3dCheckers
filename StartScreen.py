import pygame
import Values as v
import Graphic_2d as gr

class Key:
    number = -1
    def __init__(self, x, y, text:str, lenght):
        self.x=x
        self.y=y
        self.text=text
        self.lenght=lenght
        self.size=((self.x, self.y), (self.lenght, self.lenght//5))
#        print(self.x, self.y, self.x+self.lenght, self.y+self.lenght//5)
#        print(self.size)
        self.color1=(255,215,0)
        self.color2=(205,155,29)
        self.color_font=(205,155,29)
        self.is_pressed=False
        self.number=self.item()

    def item(self):
        Key.number += 1
        return Key.number

    def __cmp__(self, other):
        if self.number > other.number:
            return True
        return False

        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color1, pygame.Rect(self.size))
        pygame.draw.rect(screen, self.color2, self.size, 2)
        pygame.draw.rect(screen, self.color2, self.size, 2)
        Text = pygame.font.Font(None, 30).render(self.text, True, self.color_font)
        screen.blit(Text, (self.x+self.lenght//20, self.y+self.lenght//30))
    
    def pressed_key(self):
        self.color1=(238,201,0)
    def unpressed_key(self):
        self.color1 = (255, 215, 0)

    def cursor(self):
        pos = (pygame.mouse.get_pos())
#        print(pos)
        if self.size[0][0] < pos[0] < self.x + self.size[1][0] and self.size[0][1] < pos[1] < self.y + self.size[1][1]:
            self.color_font=(204,173,0)
        else:
            self.color_font=(205,155,29)

    def is_pressed_f(self, screen):
        if pygame.mouse.get_pressed()[0]:
            pos = (pygame.mouse.get_pos())
            if self.size[0][0] < pos[0] < self.x + self.size[1][0] and self.size[0][1] < pos[1] < self.y + self.size[1][1]:
                self.pressed_key()
                self.is_pressed=True
        return self.is_pressed


class Menu:
    def __init__(self, screen, widht, points:list, background = v.background_image):

        self.widht=widht
        self.lenght=widht//2
        self.key_widht = self.lenght // 5
        self.points=points
        self.screen=screen
        self.keys=self.keys()
        self.bc = background

    def keys(self):
        n=len(self.points)
#        print (n)
        keys=[]
        for i, point in enumerate(self.points):
            keys.append(Key((int(self.widht//4)), int((self.widht/2 - (n-i+0.5)*self.key_widht)), point, self.lenght))
#            print(i)
        return keys

    def key_processing(self, text):
        if text == v.KEY_PLAY or text == v.KEY_RESTART:
#            print('b')
            Menu(self.screen, self.widht, [v.KEY_SINGLE, v.KEY_DOUBLE]).menu()
        elif text == v.KEY_CONTINUE:
            pass
        elif text == v.KEY_EXIT:
            v.done = False
        elif text == v.KEY_SINGLE:
            Menu(self.screen, self.widht, [v.KEY_SIMPLE, v.KEY_DIFFICULT]).menu()
        elif text == v.KEY_DOUBLE:
            gr.graph(0)
        elif text == v.KEY_SIMPLE:
            gr.graph(1)
        elif text == v.KEY_DIFFICULT:
            gr.graph(2)

    def menu(self):
#        print('asa')
        pygame.init()
        clock = pygame.time.Clock()

        done = True
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    v.done = False
                    done = False

                pygame.display.update()
                clock.tick(60)
                self.screen.blit(self.bc, (0, 0))
                for key in self.keys:
                    key.cursor()
                    press = key.is_pressed_f(self.screen)
                    key.draw(self.screen)
                    if press:
#                        print('a')
                        self.key_processing(key.text)
                        done=False
                        break

            pygame.display.flip()







