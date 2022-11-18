import pygame as pg
import math

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def MovimentoDireita():
    glRotate(5,0,0,-1)
    glTranslatef(1.01, 0, 0)

def MovimentoEsquerda():
    glRotate(5,0,0,1)
    glTranslatef(-1.01, 0, 0)

def Chassi():
# Chassi
    glBegin(GL_LINE_STRIP)
    glVertex2f(-10, -2)
    glVertex2f(-10, 5)
    glVertex2f(-5, 5)
    glVertex2f(-5, 10)
    glVertex2f(5, 10)
    glVertex2f(7, 5)
    glVertex2f(10, 5)
    glVertex2f(10, -2)
    glVertex2f(7, -2)
    glVertex2f(7, 2)
    glVertex2f(4, 2)
    glVertex2f(4, -2)
    glVertex2f(-6, -2)
    glVertex2f(-6, 2)
    glVertex2f(-9, 2)
    glVertex2f(-9, -2)
    glVertex2f(-10, -2)
    glEnd()

# Janela
    glBegin(GL_QUADS)
    glVertex2f(3.5, 8)
    glVertex2f(3.5, 5)
    glVertex2f(1.5, 5)
    glVertex2f(1.5, 8)
    glEnd()

# Antena
    glBegin(GL_LINE_STRIP)
    glVertex2f(2.5, 10)
    glVertex2f(-1, 15)
    glEnd()

    glRotatef(0,0,0,0)

def Rodas():
    glPointSize(1.0)
    
    glBegin(GL_POLYGON)
    glVertex2f(-9, -3)
    glVertex2f(-9, 1)
    glVertex2f(-7.5, 2)
    glVertex2f(-6, 1)
    glVertex2f(-6, -3)
    glVertex2f(-7.5, -5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4, -3)
    glVertex2f(4, 1)
    glVertex2f(5.5, 2)
    glVertex2f(7, 1)
    glVertex2f(7, -3)
    glVertex2f(5.5, -5)
    glEnd()
    
def main():  
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    glTranslatef(0.0, 0.0, 0.0)

    gluOrtho2D(-50.0, 50.0, -50.0*800/600, 50.0*800/600);
    
    x = 0

    while True:
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_RIGHT :
                    x = 1
                if event.key == pg.K_LEFT :
                    x = 2

            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Chassi()
        Rodas()

        if(x == 1):
            MovimentoDireita()
        if(x == 2):
            MovimentoEsquerda()
        
        pg.display.flip()
        pg.time.wait(10)
    
    return
    
if __name__ == "__main__":
    main()