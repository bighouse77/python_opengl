import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def Desenha():
    # Telhado
    glBegin(GL_TRIANGLES)
    glColor3f(255, 0, 0)
    glVertex2f(-10, 0)
    glVertex2f(10,0)
    glVertex2f(0, 10)
    glEnd()
    
    # Casa 
    glBegin(GL_QUADS)
    glColor3f(0, 0, 255)
    glVertex2f(-10, -25)
    glVertex2f(10, -25)
    glVertex2f(10, 0)
    glVertex2f(-10, 0)
    glEnd()
    
    # Porta
    glBegin(GL_QUADS)
    glColor3f(255, 255, 255)
    glVertex2f(-2.5, -24)
    glVertex2f(2.5, -24)
    glVertex2f(2.5, -9)
    glVertex2f(-2.5, -9)
    glEnd()
    
    # Janela
    glBegin(GL_QUADS)
    glColor3f(255, 255, 255)
    glVertex2f(3.5, -11)
    glVertex2f(5, -11)
    glVertex2f(5, -9)
    glVertex2f(3.5, -9)
    
    glColor3f(255, 255, 255)
    glVertex2f(5.5, -11)
    glVertex2f(7, -11)
    glVertex2f(7, -9)
    glVertex2f(5.5, -9)
    
    glColor3f(255, 255, 255)
    glVertex2f(5.5, -14)
    glVertex2f(7, -14)
    glVertex2f(7, -12)
    glVertex2f(5.5, -12)
    
    glColor3f(255, 255, 255)
    glVertex2f(3.5, -14)
    glVertex2f(5, -14)
    glVertex2f(5, -12)
    glVertex2f(3.5, -12)
    glEnd()
    
def main():  
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluOrtho2D(-50.0, 50.0, -50.0*800/600, 50.0*800/600);
    
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(255, 255, 255, 255)
        
        Desenha()
        
        pg.display.flip()
        pg.time.wait(10)
    
    return
    
if __name__ == "__main__":
    main()