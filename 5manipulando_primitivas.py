import pygame as pg
from pygame.locals import *

import math

from OpenGL.GL import *
from OpenGL.GLU import *

def exPto2d():
    ang = 0
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    while (ang < 2 *math.pi):
        glVertex2f(20*math.cos(ang),20*math.sin(ang))
        ang = ang + math.pi/7.0
    glEnd()
    
def exLines2d():
    ang = 0
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_LINE_LOOP)
    while (ang < 2 *math.pi):
        glVertex2f(20*math.cos(ang),20*math.sin(ang))
        ang = ang + math.pi/7.0
    glEnd()

def main():
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluOrtho2D (-50.0, 50.0, -50.0*800/600, 50.0*800/600);

    glTranslatef(0.0, 0.0, 0.0)

    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        if event.type == pg.KEYDOWN:

                if event.key == pg.K_LEFT :
                    x = 1

                if event.key == pg.K_RIGHT :
                    x = 2

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        exPto2d()

        if(x==1) :
            exPto2d()
        if(x==2):
            exLines2d() 
        
        pg.display.flip()
        pg.time.wait(10)

if __name__ == "__main__":
    main()