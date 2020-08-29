 
 
#include <GL/glut.h>  
void initGL() {
   
   glClearColor(1.0f, 0.5f, 0.0f, 0.0f);
   
}
 
void display() {
   glClear(GL_COLOR_BUFFER_BIT);   
 //code for left side grass
 
   glBegin(GL_QUADS);              
      glColor3f(0.0f, 1.0f, 0.0f); 
      glVertex2f(0.6f, 0.2f); 
      glVertex2f(-1.0f,0.2f);  
       glVertex2f(-1.0f, -1.0f);  
    glVertex2f(-0.2f, -1.0f);     
      glEnd();
      
   // code for river
   
   glBegin(GL_QUADS);              
      glColor3f(0.0f, 0.5f, 0.5f); 
      glVertex2f(0.6f, 0.2f);     
      glVertex2f(-0.2f, -1.0f);     
      glVertex2f(0.2f, -1.0f);
      glVertex2f(0.8f, 0.2f);
     glEnd();
      
      // code for right side grass
      
    glBegin(GL_QUADS);
      glColor3f(0.0f, 1.0f, 0.0f); 
      glVertex2f(1.0f,0.2f);
      glVertex2f(1.0f,-1.0f);
      glVertex2f(0.2f,-1.0f);
      glVertex2f(0.8f,0.2f);
     glEnd();
    
 // code for hut base
   glBegin(GL_QUADS);
    glColor3f(1.0f, 0.0f, 0.0f); 
    glVertex2f(-0.2f,-0.5f);
    glVertex2f(-0.2f,-0.8f);
    glVertex2f(-0.8f,-0.8f);
    glVertex2f(-0.8f,-0.5f);
   glEnd();
   
   // code for hut door
   glBegin(GL_QUADS);
     glColor3f(1.0f, 1.0f, 0.0f); 
     glVertex2f(-0.4f,-0.6f);
     glVertex2f(-0.4f,-0.75);
     glVertex2f(-0.6f,-0.75);
     glVertex2f(-0.6f,-0.6f);
   glEnd();
   

  
   // code for hut top
   glBegin(GL_TRIANGLES);          
      glColor3f(1.0f, 1.0f, 0.0f);   
      glVertex2f(-0.2f,-0.5f);
      glVertex2f(-0.5f,-0.2f);
      glVertex2f(-0.8f,-0.5f);
 
   glEnd();
    
 //code for mountains
   glBegin(GL_TRIANGLES);          
      glColor3f(0.5f, 0.0f, 0.0f); 
      glVertex2f(-1.0f, 0.2f);
      glVertex2f(-0.6f, 0.2f);
      glVertex2f(-0.8f, 0.6f);
 
   glEnd();
     glBegin(GL_TRIANGLES);          
      glColor3f(0.5f, 0.0f, 0.0f); 
      glVertex2f(-0.6f, 0.2f);
      glVertex2f(-0.2f, 0.2f);
      glVertex2f(-0.4f, 0.6f);
 
   glEnd();
     glBegin(GL_TRIANGLES);          
      glColor3f(0.5f, 0.0f, 0.0f); 
      glVertex2f(-0.2f, 0.2f);
      glVertex2f(0.2f, 0.2f);
      glVertex2f(0.0f, 0.6f);
 
   glEnd();
     glBegin(GL_TRIANGLES);          
      glColor3f(0.5f, 0.0f, 0.0f); 
      glVertex2f(0.2f, 0.2f);
      glVertex2f(0.6f, 0.2f);
      glVertex2f(0.4f, 0.6f);
 
   glEnd();
     glBegin(GL_TRIANGLES);          
      glColor3f(0.5f, 0.0f, 0.0f); 
      glVertex2f(0.6f, 0.2f);
      glVertex2f(1.0f, 0.2f);
      glVertex2f(0.8f, 0.6f);
 
   glEnd();
  
   glFlush();  
}
void onclick(int button, int state,int x,int y){
   if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN){            
      glClearColor(0,0,0,0);
      glutPostRedisplay();                                        //On clicking left mouse button at sky the day transform into night
    }
}
void onclick1(char key, int x, int y){
 if (key=='q'){                                                   //On pressing q the screen disappear
 exit(1);}
 
} 

int main(int argc, char** argv) {
   glutInit(&argc, argv);          
   glutCreateWindow("Landscape");  
   glutInitWindowSize(700, 700);   
   glutInitWindowPosition(50, 50); 
   //initGL();  
   glutDisplayFunc(display);       
           initGL();  
           glutMouseFunc(onclick);
           glutKeyboardFunc(onclick1);            
   glutMainLoop();                 
   return 0;
}
   

