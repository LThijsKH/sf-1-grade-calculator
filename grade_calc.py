num_of_labs = input("Enter the number of labs completed: ")
num_of_quizs = input("Enter the number of quizzes completed: ")
assignment_1 = input("Enter grade for Assignment 1: ")
assignment_2 = input("Enter grade for Assignment 2: ")
assignment_3 = input("Enter grade for Assignment 3: ")
assignment_4 = input("Enter grade for Assignment 4: ") 
midterm_1 = input("Enter grade for Midterm 1: ")
midterm_2 = input("Enter grade for Midterm 2: ")
final_grade = input("Enter grade for Final Exam: ") 
midterm_and_prep_grade = input("Enter grade for Midterms and Final Preparation: ")
labs = 0
if (num_of_labs >=6): 
	labs = 100*0.2
else:
	labs = (num_of_labs/6) * 0.20	
quizs = 0
if (num_of_quizs >= 6):
	quizs = 100 * 0.15
else: 
	quizs = (num_of_quizs/6)*0.15
assignments = ((assignment_1 + assignment_2 + assignment_3 + assignment_4)/4)*0.16
midterms = ((midterm_1 + midterm_2)/2) *0.25
final = final_grade * 0.18
midterm_prep = midterm_and_prep * 0.06
grade = labs + quizs + assignments + midterms + final + midterm_prep
print("Your average is: "+ grade + "%")

