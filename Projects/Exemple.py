from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpa a tela

    glBegin(GL_TRIANGLES)  # começa a desenhar triângulos

    # Vértices do triângulo com cores diferentes
    glColor3f(1.0, 0.0, 0.0)  # vermelho
    glVertex2f(-0.5, -0.5)

    glColor3f(0.0, 1.0, 0.0)  # verde
    glVertex2f(0.5, -0.5)

    glColor3f(0.0, 0.0, 1.0)  # azul
    glVertex2f(0.0, 0.5)

    glEnd()

    glutSwapBuffers()  # troca o buffer para exibir o desenho

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)  # tamanho da janela
    glutInitWindowPosition(100, 100)
    glutCreateWindow("PyOpenGL - Triângulo colorido")
    glutDisplayFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
    main()
