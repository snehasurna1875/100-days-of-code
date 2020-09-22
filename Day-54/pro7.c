










#include <stdio.h>
#include<GL/glut.h>
#include <math.h>
float xc,yc,r;
void Draw(void)
{
 int x=0,y=r,d=3-(2*r);  
   glBegin(GL_POINTS);
                                                                                               
		glVertex2f(x+xc,y+yc);
		glVertex2f(x+xc,-y+yc);
		glVertex2f(-x+xc,-y+yc);
		glVertex2f(-x+xc,y+yc);
		glVertex2f(y+xc,x+yc);
		glVertex2f(y+xc,-x+yc);
		glVertex2f(-y+xc,-x+yc);
		glVertex2f(-y+xc,x+yc);
              glEnd();  
  
    while(x<=y)  
     {  
      if(d<=0)  
             {  
        d=d+(4*x)+6;  
      }  
     else  
      {  
        d=d+(4*x)-(4*y)+10;  
        y=y-1;  
      }  
       x=x+1;  
         glBegin(GL_POINTS);
      
		glVertex2f(x+xc,y+yc);
		glVertex2f(x+xc,-y+yc);
		glVertex2f(-x+xc,-y+yc);
		glVertex2f(-x+xc,y+yc);
		glVertex2f(y+xc,x+yc);
		glVertex2f(y+xc,-x+yc);
		glVertex2f(-y+xc,-x+yc);
		glVertex2f(-y+xc,x+yc);
              glEnd();   
      }  

glFlush();
}




void init(void)
{
	//glClearColor(0.7,0.7,0.7,0.7);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0,500,0,500);
}


int main(int argc, char** argv) {
printf("Enter first point co-ordinates\n");
	printf("xc: ");
	scanf("%f",&xc);
	
	printf("Enter second point co-ordinates\n");
	printf("yc: ");
	scanf("%f",&yc);
	printf("Enter the radius");
	printf("Y1: ");
	scanf("%f",&r);	

glutInit(&argc, argv);
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
glutInitWindowSize (500, 500);
glutInitWindowPosition (100,100);
glutCreateWindow ("Bresenham");
init();
glutDisplayFunc(Draw);
glutMainLoop();

return 0;
}
