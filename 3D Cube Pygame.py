import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
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
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0,0, -10)

    r=1
    rx=0
    ry=0
    rz=0
    glRotatef(r, rx, ry, rz)
    K=None
    p=0.2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if K==event.key:
                    p+=1.1*p
                else:
                    p=0.2
                if event.key == pygame.K_LEFT:
                    glTranslatef(-p,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(p,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,p,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-p,0)
                K=event.key
                
                if event.key == pygame.K_v:
                    rx+=1
                if event.key == pygame.K_b:
                    ry+=1
                if event.key == pygame.K_n:
                    rz+=1
                if event.key == pygame.K_w:
                    rx-=1
                if event.key == pygame.K_x:
                    ry-=1
                if event.key == pygame.K_c:
                    rz-=1
                if event.key == pygame.K_r:
                    r+=1
                if event.key == pygame.K_RETURN:
                    rx=0
                    ry=0
                    rz=0
                    r=0


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)

        glRotatef(r, rx, ry, rz)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
