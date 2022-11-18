from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'Veiculo_P2'
especularidade = [1.0,1.0,1.0,1.0] 
especMaterial = 60
px = 0
py = 0
pz = 0
distancia = 10 # Mudar para altera a distancia do obijeto.

def drawC():
    
    glRotatef(px, 1, 0, 0) # Rotaciona em relação ao eixo X (Setas cima e baixo)
    glRotatef(py, 0, 1, 0) # Rotaciona em relação ao eixo Y (Setas direita e esquerda)
    glRotatef(pz, 0, 0, 1) # Rotaciona em relação ao eixo Z (teclas PgUp e PgDn)
    
    glBegin(GL_QUADS)
    
    # FRENTE DO CARRO (VERMELHO)
    #Vidro
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1,1,1)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1, -0.2, 2.0)
    glVertex3f(1, -0.2, 2.0)
    
    # Capo
    glVertex3f(1, -0.2, 2.0)
    glVertex3f(-1, -0.2, 2.0)
    glVertex3f(-1, -0.2, 3.5)
    glVertex3f(1, -0.2, 3.5)
    
    #Farois
    glVertex3f(1, -0.2, 3.5)
    glVertex3f(-1, -0.2, 3.5)
    glVertex3f(-1, -0.5, 3.7)
    glVertex3f(1, -0.5, 3.7)
    
    #Parachoque 
    glVertex3f(1, -0.5, 3.7)
    glVertex3f(-1, -0.5, 3.7)  
    glVertex3f(-1, -0.8, 3.7)
    glVertex3f(1, -0.8, 3.7)
    
    # metal
    glVertex3f(1, -0.5, 3.8)
    glVertex3f(-1, -0.5, 3.8)  
    glVertex3f(-1, -0.8, 3.8)
    glVertex3f(1, -0.8, 3.8)
    
    glVertex3f(-1, -0.5, 3.8)
    glVertex3f(-1.1, -0.5, 3.7)
    glVertex3f(-1.1, -0.8, 3.7)
    glVertex3f(-1, -0.8, 3.8)
    
    glVertex3f(1, -0.5, 3.8)
    glVertex3f(1.1, -0.5, 3.7)
    glVertex3f(1.1, -0.8, 3.7)
    glVertex3f(1, -0.8, 3.8)
    ############################
    
    
    # TETO DO CARRO (VERDE)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    ############################
    
    
    # PARTE DE BAIXO DO CARRO (LARANJA)
    glColor3f(1.0, 0.5, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    ############################
    
    
    # TRAZEIRA DO CARRO (AMARELA) 
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    ############################
    
    
    # LATERAL ESQUERDA DO CARRO (AZUL)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    ############################
    
    
    # LATERAL DIREITA DO CARRO (ROSA)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    ############################
    
    glEnd() 
    
    
    # Coordenadas
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(1000, 0, 0)
    glVertex3f(-1000, 0, 0)
    glColor3f(0, 1, 0)
    glVertex3f(0, 1000, 0)
    glVertex3f(0, -1000, 0)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 1000)
    glVertex3f(0, 0, -1000)
    glEnd()
    
    glFlush()                

def buttons(key,x,y):
    global px, py, pz
    if key == GLUT_KEY_LEFT:
        py -= 1
        
    elif key == GLUT_KEY_RIGHT:
        py += 1
        
    elif key == GLUT_KEY_UP:
        px += 1
        
    elif key == GLUT_KEY_DOWN:
        px -= 1
    
    elif key == GLUT_KEY_PAGE_UP:
        pz -= 1
    
    elif key == GLUT_KEY_PAGE_DOWN:
        pz += 1
    
    elif key == GLUT_KEY_HOME: # # Voltar para a vista frental (tecla Home)
        px = 0
        py = 0
        pz = 0
        
    elif key == GLUT_KEY_END: # Vista em perspectiva (tecla End)
        px = 25
        py = 40
        pz = 0
        
    glutPostRedisplay()

def main():
    global distancia
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700,700)
    glutCreateWindow(name)

    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_LIGHTING)
    lightZeroPosition = [1.,4.,50.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glutSpecialFunc(buttons)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50,(1/1),1,50)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(4.083,-4.083,distancia,
                0,0,0,
                -0.07,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(30,1,1,0);
    drawC()
    #glutSolidTeapot(1.0);
    #glutSolidSphere(2,20,20)
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()