print("Car Game")

command = ""
started = False
run = False

while True:
    command = input("< ").lower()
    if command == "start":
        if started :
            print("ENGINE IS ALREADY STARTED...!")
        else:
            started = True
        print("Engine started........")
    elif command == "stop":
        print("Engine Stopped.....!!!")
    elif command == "help":
        print("""
         1. start = Engine start
         2. stop = Engine stop
         3. run = Run Car
         4. slow = Slow down
         5. quit = Quit game
         """)
    elif command == "run":
        if started:
            print("Car is running")
            run = True
        else:
            print("AT FIRST START THE ENGINE...!!")
    elif command == "slow":
        if run:
            print("Slowing down car..")
        else:
            print("RUN The car asshole....!")
    elif command == "quit":
         break
    else:
        print("Wrong command")
