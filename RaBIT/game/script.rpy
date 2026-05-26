# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rb = Character("RaBIT")
define main_char = Character("Main Character")
define test_char = Character("Test Character")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rb
    # These display lines of dialogue.

    rb "We're here ..."
    rb "The hotel is right in front of us."
    rb "Do you want to go over the mission again, Alice?"
    menu:
        "Go over the mission again":
            jump info_dump_tuto
        "I'm fine":
            jump enter_hotel_begin
    
label info_dump_tuto:
    rb "The mission is simple, we need to get into the hotel to find and eliminate the target."
    rb "I already planted you in the hotel’s system as janitorial staff."
    rb "You are William Robertson, 26 years old. A temporary janitor, called in on short notice.."
    rb "Now all you need to do is walk in, check in as 'Robertson', and get to work."
    rb "We have to be careful though, there are some guards patrolling the Hotel."
    rb "So act carfully, and try not to raise any suspicion."
    rb "Everything clear?"
    menu:
        "can you repeat that?":
            rb "of course."
            jump info_dump_tuto 
            # counter for funny repeat after 3 times of asking to repeat, rb will say "I already told you that 3 times, maybe you should pay attention this time."
        "alrighgt, let's go":
            jump enter_hotel_begin


label enter_hotel_begin:

"Lets start"
    

    # This ends the game.
return
