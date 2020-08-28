 
 
#include <GL/glut.h>  

  

void initGL() {
   
   glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
   
}
 

void display() {
   glClear(GL_COLOR_BUFFER_BIT);   
 
   

  
   
   /*glBegin(GL_TRIANGLES);          
      glColor3f(1.0f, 0.0f, 0.0f); 
      glVertex2f(-0.5f,-0.2f);
      glVertex2f(-0.2f,-0.5f);
      glVertex2f(-0.8f,-0.5f);
 
   glEnd();*/
   glBegin(GL_QUADS);              
      glColor3f(0.0f, 1.0f, 0.0f); 
      glVertex2f(0.6f, 0.2f); 
      //glVertex2f(-0.2f, -1.0f); 
      glVertex2f(-1.0f,0.2f);  
       glVertex2f(-1.0f, -1.0f);  
      glVertex2f(-0.2f, -1.0f);     
      
     // glVertex2f(-1.0f, -1.0f);
      glEnd();
   
   glBegin(GL_QUADS);              
      glColor3f(1.0f, 0.0f, 0.0f); 
      glVertex2f(0.6f, 0.2f);     
      glVertex2f(-0.2f, -1.0f);     
      glVertex2f(0.2f, -1.0f);
      glVertex2f(0.8f, 0.2f);
      glEnd();
      
    glBegin(GL_QUADS);
      glColor3f(0.0f, 1.0f, 0.0f); 
      glVertex2f(1.0f,0.2f);
      glVertex2f(1.0f,-1.0f);
      glVertex2f(0.2f,-1.0f);
      glVertex2f(0.8f,0.2f);
      glEnd();
    
 
  
    
 
   glBegin(GL_TRIANGLES);          
      glColor3f(1.0f, 1.0f, 0.0f); 
      glVertex2f(-1.0f, 0.2f);
      glVertex2f(-0.6f, 0.2f);
      glVertex2f(-0.8f, 0.6f);
 
   glEnd();
     glBegin(GL_TRIANGLES);          
      glColor3f(1.0f, 1.0f, 0.0f); 
      glVertex2f(-0.6f, 0.2f);
      glVertex2f(-0.2f, 0.2f);
      glVertex2f(-0.4f, 0.6f);
 
   glEnd();
     glBegin(GL_TRIANGLES);          
      glColor3f(1.0f, 1.0f, 0.0f); 
      glVertex2f(-0.2f, 0.2f);
      glVertex2f(0.2f, 0.2f);
      glVertex2f(0.0f, 0.6f);
 
   glEnd();
     glBegin(GL_TRIANGLES);          
      glColor3f(1.0f, 1.0f, 0.0f); 
      glVertex2f(0.2f, 0.2f);
      glVertex2f(0.6f, 0.2f);
      glVertex2f(0.4f, 0.6f);
 
   glEnd();
     glBegin(GL_TRIANGLES);          
      glColor3f(1.0f, 1.0f, 0.0f); 
      glVertex2f(0.6f, 0.2f);
      glVertex2f(1.0f, 0.2f);
      glVertex2f(0.8f, 0.6f);
 
   glEnd();
 
    
 
   

   
 
   glFlush();  
}
 

int main(int argc, char** argv) {
   glutInit(&argc, argv);          
   glutCreateWindow("Six Primitives in loop");  
   glutInitWindowSize(700, 700);   
   glutInitWindowPosition(50, 50); 
   //initGL();  
   glutDisplayFunc(display);       
           initGL();              
   glutMainLoop();                 
   return 0;
}
   

