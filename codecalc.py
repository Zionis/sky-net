import time
finished = 0
print ""
print "You have executed the integrator code calculator."
print ""
print "This code is protected by sutax network encryption"
print ""
print "Illegal access is strictly prohibited"
print ""
print "If you are not authorized, please exit the program (Ctrl-C)"
time.sleep(10)
print ""
print ""
print "Program not aborted, continuing execution"
print ""
while finished < 1:
    print ""
    print ""
    name = raw_input("What is your name? ")
    print ""
    first = raw_input("Enter the first coordinate: ")
    print ""
    second = raw_input("Enter the second coordinate: ")
    first = int(first)
    second = int(second)
    time.sleep(1)
    print ""
    print "Calculating your answer..."
    time.sleep(1)
    for i in range(10, 0,-1):
        print i
        time.sleep(2)
    if ((first == 300) and (second == 10)):
        print ""
        print ""
        print "Congratulations %s, You cracked the code!!!" %name
        print ""
        print ""
        time.sleep(2)
        print "Please wait while we generate the combination"
        time.sleep(5)
        print ""
        print ""
        print "Combination = 12, 6, 3"
        print ""
        print ""
        print "Exiting Integrator Code"
        finished = 1
    else:
        print "Sorry %s, try again" %name
        print ""
        print "Resetting Integrator"
        print "."
        time.sleep(1)
        print ".."
        time.sleep(2)
        print "..."
        time.sleep(3)
        print ""
        print ""
        finished = 0
