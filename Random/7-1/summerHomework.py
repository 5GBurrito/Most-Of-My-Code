# Defnitions:
#     Variables:
#         values that can be changed throughout program's runtime
#     User Input:
#         Values or data inputed by the User of the program
#     If Statements:
#         A conditional statement that activates once if a condition is True
#     Loop:
#         Code that runs repeatdly for a  certian amount of time OR while a condition is true
#     Print Statement:
#         A statement that outputs data to the console

#Lucky Number Generator
print("welcome to the lucky number generator!")
value1 = int(input("What day of the month is your birthday?     "))
value2 = input("What did you eat for breakfast?     ")

for i in range(value1):
    value3 = len(value2) + value1

value4 = value1*value3

if value4 < 10000:
    print("Your lucky number is: ", value4)
else:
    print("Your lucky number is: ", value4%10000)