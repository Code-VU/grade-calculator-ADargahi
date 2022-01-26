def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    grade = ""
    hrs = input("Enter score: ")

    try:
        hrs = float(hrs)
        if hrs >=0.9:
            grade = "A"
        elif hrs >=0.8:
            grade = "B"
        elif hrs >=0.7:
            grade = "C"
        elif hrs >=0.6:
            grade = "D"
        else:
            grade = "Bad score"

    except:
        print("Bad score")

    print(grade)


    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateGrade()