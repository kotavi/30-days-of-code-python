class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, first_name, last_name, id_number, scores):
        super().__init__(first_name, last_name, id_number)
        self.scores = scores

    def get_scores(self):
        return self.scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        scores = self.get_scores()
        score = sum([score for score in self.get_scores()]) / len(scores)
        if score >= 90 and score <= 100:
            grade = 'O'
        elif score >= 80 and score < 90:
            grade = 'E'
        elif score >= 70 and score < 80:
            grade = 'A'
        elif score >= 55 and score < 70:
            grade = 'P'
        elif score >= 40 and score < 55:
            grade = 'D'
        else:
            grade = 'T'
        return grade

"""
Example of input:
Heraldo Memelli 8135627
2
100 80 90 45
"""
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
