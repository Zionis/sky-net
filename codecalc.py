import time
finished = 0
answers = [300, 10, "25"]
first = "null"
second = "null"
third = "null"
inputs = []
print "\n\n"
print "You have executed the integrator code calculator. \n\n"

print "This code is protected by sutax network encryption.  \n\n"

print "Illegal access is strictly prohibited.  \n\n"

print "If you are not authorized, please exit the program (Ctrl-C) \n\n"
time.sleep(7)

print "Program not aborted, continuing execution \n\n"

while finished < 1:
    print "\n\n"

    name = raw_input("What is your name? ")
    print ""
    first = raw_input("Enter the first answer: ")
    print ""
    second = raw_input("Enter the second answer: ")
    print ""
    third = raw_input("Enter the third answer: ")

    first = int(first)
    second = int(second)
    third = str(third)
    inputs = [first, second, third]
    time.sleep(1)
    print answers
    print inputs
    print ""
    print "Calculating your answer... \n"
    time.sleep(1)
    for i in range(10, 0,-1):
        print i
        time.sleep(1)
    if answers == inputs:
        print "Congratulations %s, You cracked the code!!! \n\n" %name

        time.sleep(2)
        print "Please wait while we generate the combination \n\n"
        time.sleep(5)

        print "Combination = 12, 6, 3 \n\n"
        print " ^ > < < ^ "
        print "\n\n"
        print "Exiting Integrator Code \n\n"
        finished = 1
    else:
        print "Sorry %s, try again \n" %name

        print "Resetting Integrator"
        print "."
        time.sleep(1)
        print ".."
        time.sleep(2)
        print "... \n\n"
        time.sleep(3)

        finished = 0
