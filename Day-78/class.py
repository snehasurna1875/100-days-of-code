'''Calculate the percentage obtained by the student and grade A is obtained more than 2 sports, grade b obtained for 2 sports and C obtained for 1 sports)'''



class student:
    percentage=0.0
    @staticmethod
    def marks_calcultor(a,b,c,d,e):
        
        percentage=((a+b+c+d+e)/500)*100
        return percentage
class sports(student):
    @staticmethod
    def grade_computation(g):
        if(g<=1):
            print("Grade C")
        if(g==2):
            print("Grade B")
        if(g>2):
            print("Grade A")
f=student()
f.marks_calculator(50,20,30,50,60)
g=sports()
g.grade_computation(3)
