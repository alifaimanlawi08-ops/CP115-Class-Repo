#Programmer's name : Alif Aiman
'''problem description : this program must use an appropriate escape characters
 and aritmetic expression to produce the desired output '''
name="Ahmad bin Abu"
matric_no="MS2025123499"
assignment_marks=10

#CALCULATE
assignment_total_marks=assignment_marks * 2

#PRINT HEADER
print(f"Name:{name}\t\t\tMatric.No:{matric_no}\n"
#PRINT PATTERN USING ESCAPE CHARACTERS
      "*\t\t\t*\n"
      "**\t\t**\n"
      "***\t***\n"
      "********\n"
      "***\t***\n"
      "*\t\t\t*\n"
#PRINT TEXT WITH ESCAPE CHARACTERS AND APPROPRIATE ARITHMETIC EXPRESSION
       "This is my\n\tsecond\n\t\tassignment\n"
        f"I want 2x10 marks, which is {assignment_total_marks} full marks"
)