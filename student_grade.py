
def ask_number_of_students(number):

	student_number = input("How many students do you have?  \n")

	return student_number



def ask_number_of_subjects(number):

	subject_number = input("How many subjects do they offer?  \n")

	print("Saving >>>>>>>>>>>>>>>>>>>>>")

	print("Saved successfully")

	return subject_number



def ask_student_score_and_subject_():

	for number in range(0, subject_number):

	student_name = input("Enter the name of the student: ")

	student_score = 0

	total_score = 0
	
	score_list = []

	next_entry ="yes"

	while next_entry == "yes":

		subject_name = input("Enter subject name : ")

		subject_score = float(input(f"Enter the score of {subject_name} :"))
			
		for score in subject_score(0, 100):

			if(score > 100):

				print("Invalid score")

		
		score_list.append(subject_score)
		
		total_score += subject_score

		next_entry = input("Do you want to enter another subject? Yes / No : ").lower()

		Print(f"{student_name} + score + ")




check_number_of_student = ask_number_of_students(0);
check_number_of_subjects = ask_number_of_subjects(0);
check_student_score_and_subject = ask_student_score_and_subject( )


print(check_number_of_student)
print(check_number_of_subjects)
