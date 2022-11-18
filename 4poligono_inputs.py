import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def MoverEsquerda():
    glTranslatef(-1.01, 0, 0)

def MoverDireita():
    glTranslatef(1.01, 0, 0)

def Zerar():
    glTranslatef(0, 0, 0)

def AumentarEscala():
    glScalef(1.01, 1.01, 1.01)

def DiminuirEscala():
    glScalef(0.99, 0.99, 0.99)

def Rotacionar():
    glRotatef(5, 0, 0, 1) 

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
    
    x = 0

    while True:
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_LEFT :
                    x = 1

                if event.key == pg.K_RIGHT :
                    x = 2

                if event.key == pg.K_w :
                    x = 3

                if event.key == pg.K_s :
                    x = 4

                if event.key == pg.K_r :
                    x = 5

                if event.key == pg.K_g :
                    x = 6

            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(255, 255, 255, 255)

        #glTranslatef(0.1, 0, 0) 
        Desenha()

        if(x == 1):
            MoverEsquerda()
        if(x == 2):
            MoverDireita()
        if(x == 3):
            AumentarEscala()
        if(x == 4):
            DiminuirEscala()
        if(x == 5):
            Rotacionar()
        if(x == 6):
            Zerar()
            
        
        pg.display.flip()
        pg.time.wait(10)
    
    return
    
if __name__ == "__main__":
    main()