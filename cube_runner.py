# Working 3D Cube Runner - Python + PyOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x_rotate = 0
y_rotate = 0

def init():
    glClearColor(0.1, 0.1, 0.1, 1)  # dark gray background
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 50.0)  # fov, aspect, near, far
    glMatrixMode(GL_MODELVIEW)

def draw_cube():
    glBegin(GL_QUADS)
    # Front face (red)
    glColor3f(1, 0, 0)
    glVertex3f( 1, 1,-1)
    glVertex3f(-1, 1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f( 1,-1,-1)
    # Back face (green)
    glColor3f(0,1,0)
    glVertex3f( 1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1,-1, 1)
    glVertex3f( 1,-1, 1)
    # Left face (blue)
    glColor3f(0,0,1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1, 1)
    # Right face (yellow)
    glColor3f(1,1,0)
    glVertex3f( 1, 1, 1)
    glVertex3f( 1, 1,-1)
    glVertex3f( 1,-1,-1)
    glVertex3f( 1,-1, 1)
    # Top face (cyan)
    glColor3f(0,1,1)
    glVertex3f( 1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1,-1)
    glVertex3f( 1, 1,-1)
    # Bottom face (magenta)
    glColor3f(1,0,1)
    glVertex3f( 1,-1, 1)
    glVertex3f(-1,-1, 1)
    glVertex3f(-1,-1,-1)
    glVertex3f( 1,-1,-1)
    glEnd()

def display():
    global x_rotate, y_rotate
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0,0,-7)
    glRotatef(x_rotate,1,0,0)
    glRotatef(y_rotate,0,1,0)
    draw_cube()
    glutSwapBuffers()

def keyboard(key, x, y):
    global x_rotate, y_rotate
    if key == b'a':
        y_rotate -= 5
    elif key == b'd':
        y_rotate += 5
    elif key == b'w':
        x_rotate -= 5
    elif key == b's':
        x_rotate += 5

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"3D Cube Runner")
init()
glutDisplayFunc(display)
glutIdleFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
