class Students():
    # Properties/Attributes

    Age = 10
    Name = ""
    Grade = "4th"
    Teacher = "Bethany"
    Fav_Color = ""

    # Constructor

    def __init__(self):
        print ("making_a_new_student")

    # Another function

    def show_details(self):
        print ("The details of the student are:")
        print(self.Name)
        print(self.Age)
        print(self.Grade)
        print(self.Teacher)
        print(self.Fav_Color)

    # Change details
             
    def change_detail(self):
        print ("please enter your age:")
        self.Age = int(input())

        print ("please enter your name:")
        self.Name =input()

# Making objects/instance

George = Students()
Michael = Students()

George.show_details()
Michael.change_detail()
Michael.show_details()


