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
def lab_programming_problems(num_of_labs):
	if (num_of_labs >= 6):
		return(100*0.2)
	else:
		return(((num_of_labs)/5)*0.2)
def quizzes (num_of_quizzes):
	if (num_of_quizzes < 6):
		return((num_of_quizzes / 6)*0.15)
	else:
		return(100 * 0.15)
def assignments(assignment_1, assignment_2, assignment_3, assignment_4):
	return(((assignment_1 + assignment_2 + assignment_3 + assignment_4)/ 4) * 0.16)
def midterms (midterm_1, midterm_2):
	return (((midterm_1+midterm_2)/2)*0.25)
def final (final_grade):
	return(final_grade*0.18)
def midterm_and_prep (midterm_and_prep_grade):
	return(midterm_and_prep_grade *0.06)
def grade (lab_programming_problems, quizzes, assignments, midterms, final, midterm_and_prep):
	return(lab_programming_problems + quizzes + assignments + midterms + final + midterm_and_prep)*100
print(grade + "%")
