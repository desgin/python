import numpy as np

NUMBER = np.random.randint(low=1, high=100)

GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True

print "Alright..."

while RUNNING:
    GUESS = raw_input("What is your lucky number? ")
    if int(GUESS) < NUMBER:
        print "Wrong, too low."
    elif int(GUESS) > NUMBER:
        print "Wrong, too high."
    elif GUESS.lower() == "exit":
        print "Better luck next time."
        RUNNING = False
    TRY += 1
