from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        connects buttons to their respective functions
        """
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton_2.clicked.connect(lambda: self.view())
        self.pushButton_3.clicked.connect(lambda: self.clear())

    def submit(self) -> None:
        """
        writes student data to file as long as their name
        has only letters and their grade has only numbers
        writes to Excel file
        :return: None
        """
        try:
            first = str(self.first_name.text())
            last = str(self.last_name.text())
            score = str(self.score.text())
            firstname = first.replace(" ", "")
            lastname = last.replace(" ", "")
            new_score = score.replace(" ", "")
            final_score = float(new_score)
            if (firstname.isalpha() == False) or (lastname.isalpha == False):
                raise Exception
            if final_score < 0:
                raise Exception
            with open('data.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile)
                content.writerow([firstname, lastname, final_score])
            self.final_result.setText("Student data successfully uploaded.")
        except:
            self.final_result.setText("Student's score must be numeric and positive.\n"
                                      "Student's first and last name may only include letters")
        finally:
            self.first_name.setText("")
            self.last_name.setText("")
            self.score.setText("")

    def view(self) -> None:
        """
        displays all student data including name, score, and final grade
        :return: None
        """
        total_list = []
        score_list = []
        with open('data.csv', 'r') as datafile:
            for row in datafile:
                total_list.append(row.split(','))
        try:
            for student_list in total_list:
                score_list.append(float(student_list[2].strip('\n')))
            top_student_index = self.top_score(score_list)
            best = score_list[top_student_index]
            grade_list = []
            for score in score_list:
                if score >= (best - 10):
                    grade_list.append('A')
                elif score >= (best - 20):
                    grade_list.append('B')
                elif score >= (best - 30):
                    grade_list.append('C')
                elif score >= (best - 40):
                    grade_list.append('D')
                else:
                    grade_list.append('F')
            final = ""
            count = 0
            for student in total_list:
                final += f'Name: {student[0]} {student[1]} | Score: {score_list[count]} | Final Grade: {grade_list[count]}\n'
                count += 1
            final += f'The highest scorer was {total_list[top_student_index][0]} with a score of {score_list[top_student_index]}'
            self.final_result.setText(final)


        except:
            self.final_result.setText("No data to display.")

    def top_score(self, scores) -> int:
        """
        cycles through all scores to find the highest
        :return: index of the highest score
        """
        try:
            highest_score = scores[0]
            highest_score_index = 0
            for i in range(len(scores)):
                if scores[i] > highest_score:
                    highest_score = scores[i]
                    highest_score_index = i
                else:
                    continue
            return highest_score_index
        except:
            raise Exception


    def clear(self) -> None:
        with open('data.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile)
        self.final_result.setText("All student data successfully cleared.")
