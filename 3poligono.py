import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def Desenha():
# Poígono
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 255)
    glVertex2f(-6, -5)
    glVertex2f(-8, -3)
    glVertex2f(-8, 0)
    glVertex2f(-8, 3)
    glVertex2f(-6, 5)
    glVertex2f(6, 5)
    glVertex2f(8, 3)
    glVertex2f(8, 0)
    glVertex2f(8, -3)
    glVertex2f(6, -5)
    glEnd()
    
def main():  
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    glTranslatef(0.0, 0.0, 0.0)

    gluOrtho2D(-50.0, 50.0, -50.0*800/600, 50.0*800/600);
    
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(255, 255, 255, 255)

        #glTranslatef(0.1, 0, 0) 
        glRotatef(5, 0, 0, 1) 
        Desenha()        
        
        pg.display.flip()
        pg.time.wait(10)
    
    return
    
if __name__ == "__main__":
    main()