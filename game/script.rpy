# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # scene waking up

    show eileen happy

    # These display lines of dialogue.

    e "You wake from a deep sleep to find yourself in a strange world."

    e "The colors seem off, distorted, unreal. You don't recognize the world around you."

    e "You look up to see a strange figure before you."

    # scene mushroom guy

    # show mushroom
    e "Oh! A visitor! Good, I was getting spored out of my mind!"

    e ""

    e "What role do mushrooms typically play in an ecosystem?"

    menu:
        
        "Decomposers":
            jump choice1_correct

        "Producers":
            jump choice_incorrect

        "Predators":
            jump choice_incorrect

    label choice1_correct:
        $ menu_flag = True
        e "You know quite a bit about fun guys like me it seems. I'd simply break down if you didn't get that one..."
        jump choice1_done

    label choice_incorrect:
        $ menu_flag = False
        scene wake up bad
        show eileen
        e "You open your eyes to see your own bedroom. The dream, which moments ago seemed so viscerally real quickly fades from your memory."
        return

    label choice1_done:
    
    e "Here's where shiitake gets real: what part of a mushroom is responsible for releasing spores?"

    menu:
        "Cap":
            jump choice_incorrect
        "Gills":
            jump choice2_correct
        "Stem":
            jump choice_incorrect

    label choice2_correct:
        $ menu_flag = True
        e "Yes, yes! It seems a bit fishy, but it's true!"
        jump choice2_done

    label choice2_done:

    e "Don't trip up now! This is the most crucial question of them all: what type of mushroom am I?"

    menu:
        "Fly agaric":
            jump choice3_correct
        "Panther cap":
            jump choice_incorrect
        "Blusher":
            jump choice_incorrect

    label choice3_correct:
        $ menu_flag = True
        e "Oh, marvelous! Certainly a morel victory! Time to cap off this visit."

    


    #menu:


    # scene TV Guy arcade

    # show TV Guy

    # scene Rainy girl hallway

    # show Rainy girl

    # scene Ending

    # show finish

    # scene wake up good

    # e "You open your eyes to see your own bedroom. Your "



    # This ends the game.

    return
