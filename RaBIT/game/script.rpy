# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rb = Character("RaBIT")


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

    rb "We're here =D"
    rb "Do you want to go over the mission again?"
    menu:
         "Go over the mission again":
          jump info_dump_tuto
         "I'm fine":
          jump enter_hotel_begin
    
label info_dump_tuto:

rb "into text"

label enter_hotel_begin:

"Lets start"
    

    # This ends the game.

    return
