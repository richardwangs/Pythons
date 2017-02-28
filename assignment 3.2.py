def grade ():
    for i in range(5):
        grade = int(input("Enter a numeric grade:"))
        
        if grade >= 90 and grade<= 100:
            print("letter grade is A")
            
        elif grade >= 80 and grade < 90:
            print("letter grade is B")

        elif grade >= 70 and grade < 80:
            print("letter grade is C")

        elif grade >= 60 and grade< 70:
            print("letter grade is D")
        else :
            print("letter grade is F")
grade()
