num_of_labs = input("Enter the number of labs completed: ")
num_of_quizs = input("Enter the number of quizzes completed: ")
assignment_1 = input("Enter grade for Assignment 1: ")
assignment_2 = input("Enter grade for Assignment 2: ")
assignment_3 = input("Enter grade for Assignment 3: ")
assignment_4 = input("Enter grade for Assignment 4: ") 
midterm_1 = input("Enter grade for Midterm 1: ")
midterm_2 = input("Enter grade for Midterm 2: ")
final_grade = input("Enter grade for Final Exam: ") 
midterm_and_prep = input("Enter grade for Midterms and Final Preparation: ")
labs = 1000000000
if (float(num_of_labs) >=6): 
	labs = 100*0.2
else:
	labs = (float(num_of_labs)/6) * 0.20	
quizs = 1000000000
if (float(num_of_quizs) >= 6):
	quizs = 100 * 0.15
else: 
	quizs = (float(num_of_quizs)/6)*0.15
assignments = ((float(assignment_1) + float(assignment_2) + float(assignment_3) + float(assignment_4))/4)*0.16
midterms = ((float(midterm_1) + float(midterm_2))/2) *0.25
final = (float(final_grade) * 0.18)
midterm_prep = float(midterm_and_prep) * 0.06
grade = labs + quizs + assignments + midterms + final + midterm_prep
print("Your average is: "+ str(grade) + "%")

