print('**** Welcome to  the LAB grade calculator!****')

entnamn = input("Who are we calculating the grades for? ==>")
entbetyg = int(input('Enter the Labs grade: ==>'))
#check if entered values are valid
if entbetyg > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    entbetyg = 100
elif entbetyg < 0:
    print('The lab value should have been 0 or greater. It has been changed to 0.')
    entbetyg = 0
entprov = int(input('Enter the EXAMS grade: ==>'))
#check if entered values are valid
if entprov > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    entprov = 100
elif entprov < 0:
    print('The exam value should have been 0 or greater. It has been changed to 0.')
    entprov = 0
entattend = int(input('Enter the Attendance grade: ==>'))
#calculating end total grade
sluttot=(entbetyg*.7)+(entprov*.2)+(entattend*.1)

#figuring correct letter grade
print("The weighted grade for",entnamn,"is",sluttot)
if 90<=sluttot<=100:
      letter='A'
elif 80<=sluttot<90:
      letter='B'
elif 70<=sluttot<80:
      letter='C'
elif 60<=sluttot<70:
      letter='D'
elif 0<=sluttot<60:
      letter='F'
print(entnamn,'has a letter grade of',letter)
