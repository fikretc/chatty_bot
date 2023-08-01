
import string

def print_hi(myname, year):
    # Use a breakpoint in the code line below to debug your script.
    my_template = string.Template("Hello! My name is $bot_name.")
    my_str = my_template.substitute(bot_name=myname)
    print(my_str)  # Press ⌘F8 to toggle the breakpoint.
    my_template = string.Template("I was created in $birth_year.")
    my_str = my_template.substitute(birth_year=year)
    print(my_str)  # Press ⌘F8 to toggle the breakpoint.

def print_user_name(user_name):
    my_template = string.Template("What a great name you have, $name!")
    reply = my_template.substitute(name=user_name)
    print(reply)

def guess_user_age(remainder3, remainder5, remainder7):
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    my_template = string.Template("Your age is $your_age; that's a good time to start programming!")
    age_guess = my_template.substitute(your_age=age)
    print(age_guess)

def count(countn):
    for i in range(countn + 1):
        print(str(i) + ' !')

def testknowledge():
    print("Let's test your programming knowledge.\n\
Why do we use methods?\n\
1. To repeat a statement multiple times.\n\
2. To decompose a program into several small subroutines.\n\
3. To determine the execution time of a program.\n\
4. To interrupt the execution of a program.")
    return 2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm', '2023')
    your_name = input("Please, remind me your name.\n")
    print_user_name(your_name)
    rem3 = input("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.\n") #.split("\n", 3)
    rem5 = input()
    rem7 = input()
    guess_user_age(int(rem3), int(rem5), int(rem7))
    countnum = input("Now I will prove to you that I can count to any number you want.\n")
    count(int(countnum))
    answer = testknowledge()
    while int(input()) != answer:
        print("Please, try again.")
    print('Congratulations, have a nice day!')

