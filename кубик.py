import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)


edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def Cube(): # никогда не здавайся говорил мне [ДАННЫЕ УДАЛЕНЫ]
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)  
    for i in [0, 1, 2, 3]:
        glVertex3fv(vertices[i])
    glEnd()
    
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)  
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_text(text, position, font_size):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, (255, 0, 0))  
    pygame_screen = pygame.display.get_surface()  
    pygame_screen.blit(text_surface, position)  

def main(): # хуиня
    pygame.init()
    display = (1280, 720)  
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()
    show_text = True
    last_switch_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        current_time = pygame.time.get_ticks()
        if current_time - last_switch_time > 1000:  
            show_text = not show_text 
            last_switch_time = current_time

        glRotatef(1, 1, 1, 0)  # РАБОТАЕТ И РАБОТАЕТ. НЕ ТРОЖЬ
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  

        Cube()  
        
        if show_text:
            draw_text("ВРАЩАЮЩИЙСЯ КУУУУУУУУУУУУУУУУУУУУУУУУБ!!1!11!!", (50, 20), 40)  # бляд не работает хуиня

        pygame.display.flip()  
        clock.tick(60)  
main()
