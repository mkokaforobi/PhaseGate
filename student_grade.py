
def ask_number_of_students(number):

	student_number = input("Enter the number of students: ")

	student_number_list = []

	student_number_list.append(student_number)

	return student_number_list



def ask_number_of_subjects(number):

	subject_number = input("Enter the number of subjects: ")

	subject_number_list = []

	subject_number_list.append(subject_number)

	return subject_number_list



def ask_student_score_and_subject(subject):

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

			elif(score >= 85):

				print("A")

			elif(score >= 70):

				print("B")

			elif(score >= 60):

				print("C")
			
			eliif(score >= 50):

				print("D")
			else
				print("F")
		
		score_list.append(subject_score)
		
		total_score = 

		next_entry = input("Do you want to enter another subject? Yes / No : ").lower()

		Print(f"{student_name}" + score + )



check_number_of_student = ask_number_of_students(0);
check_number_of_subjects = ask_number_of_subjects(0);


print(check_number_of_student)
print(check_number_of_subjects)
