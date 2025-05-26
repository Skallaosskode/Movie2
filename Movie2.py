repeat = "yes"
while repeat.lower() == "yes":

    name = input("What is your name? ").title()
    age = int(input("What is your age? "))
    genre = input("What is your favorite movie genre? ")
    # ask about drinks
    thirsty = input("Are you thirsty? (yes/no) ")

    if genre == 'horror':
        print(f"""
        {name.title()} at {age} you're so brave!  Aren't you scared you won't be 
        able to sleep tonight?  For a snack, I've heard the mummified brain cakes
        are delicious!
        """)

    elif genre == 'thriller':
        print(f"""
        {name.title()} put your seatbelt on, we are about to see if the the bus
        has a bomb on it, hotshot...  Oh by the way, the spicy tamales are also
        a thrilling snack for a {age} year old!
        """)

    elif genre == 'mystery':
        print(f"""
        Gas up the Mystery Machine Fred, its time for {name.title()} to go
        on an adventure!  {age} year olds and of course Scoob and Shagg love the scooby
        snacks btw!
        """)

    elif genre == 'comedy':
        print(f"""
        At {age}, laughing is the best medicine {name.title()}!  Lord Business
        approves of your choice.  Why not enjoy some chocolate doo doo cookies with your comedy?
        """)

    elif genre == 'romance':
        print(f"""
        I wonder the princess is gonna turn into an ogre, {name.title()}?
        Why not indulge in some triple dipped ice cream bites
        for this lovey dovey tale? {age} year olds love them!
        """)

    elif genre == 'western':
        print(f"""
        Well giddyup {name.title()}! At {age} you must be great with a lasso!
        Why not lasso some beef jerky for the perfect pairing?
        """)

    elif genre == 'action':
        print(f"""
        Well Yippie-ki-yay, if it isn't my fav genre, {name.title()}!  Just 
        remember after flying to remove your footwear and scrunch your toes 
        in the carpet, BUT always put them back on, cause you never know when a
        Hans Gruber is gonna be crashing your party.  A smart {age} year old like 
        you would know that thou, as well as knowing the best snack from the
        snack bar according to all Diehard cops are the Twinkies.
        """)

    elif genre == 'sci-fi':
        print(f"""
        Get away from her you... nah just kidding {name.title()}!
        I really liked that one when i was {age} too.  Why not try the
        vanilla alien brains?
        """)

    else:
        print(f"""
        A great choice {name.title()}. I can dump some skittles in there for you
        too.  Good old popcorn with lots of butter is the obvious choice for this
        one.  So many {age} year olds say, its hard to beat!
        """)

    if thirsty == 'yes':
        print(f"""
        Here's a cold one for ya, with lots of ice!
        """)

    elif thirsty == 'perhaps':
        print(f"""
        Perhaps you're thirsty??!  Well make up your mind ya muggle!
        """)

    else:
        print(f"""
        Not thirsty?  No problem, less bathroom breaks for you!
        """)

        # Ask if they wanna do it again
    repeat = input("\nDo you wanna choose again? (yes/no) ")
