# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("...")
define y = Character("You")
define m = Character("Mushroom Guy")
define t = Character("TV Guy")
define r = Character("Rainy Girl")

# The game starts here.

label start:

    
    scene black
    

    e "You wake from a deep sleep to find yourself in a strange world."
    scene bg forest with Dissolve(2.0)
    e "The colors seem off, distorted, unreal. You don't recognize the world around you."

    e "You look up to see a strange figure before you."

    show mushroom_1 with moveinright:
        xalign 1.0
        yalign 0.5
        

    m "Oh! A visitor! Good, I was getting spored out of my mind!"

    m "I hope you're having a pleasent trip. We could use more visitors like you. To stay here, you'll need to pass a little test. Don't worry, it won't be too punishing!"

    m "What role do mushrooms typically play in an ecosystem?"

    menu:
        
        "Decomposers":
            jump choice1_correct

        "Producers":
            jump choice_incorrect

        "Predators":
            jump choice_incorrect

    label choice1_correct:
        $ menu_flag = True
        m "You know quite a bit about fun guys like me it seems. I'd simply break down if you didn't get that one..."
        jump choice1_done

    label choice_incorrect:
        $ menu_flag = False
        scene wake up bad
        show eileen
        e "You open your eyes to see your own bedroom. The dream, which moments ago seemed so viscerally real quickly fades from your memory."
        return

    label choice1_done:
    
    m "Here's where shiitake gets real: what part of a mushroom is responsible for releasing spores?"

    menu:
        "Cap":
            jump choice_incorrect
        "Gills":
            jump choice2_correct
        "Stem":
            jump choice_incorrect

    label choice2_correct:
        $ menu_flag = True
        m "Yes, yes! It seems a bit fishy, but it's true!"
        jump choice2_done

    label choice2_done:

    m "Don't trip up now! This is the most crucial question of them all: what type of mushroom am I?"

    menu:
        "Fly agaric":
            jump choice3_correct
        "Panther cap":
            jump choice_incorrect
        "Blusher":
            jump choice_incorrect

    label choice3_correct:
        $ menu_flag = True
        m "Oh, marvelous! Certainly a morel victory! Time to cap off this visit."
        hide mushroom_1 

        show mushroomspores:
            xalign 0.5
            yalign 0.5
            zoom 2.0


        e "He holds up his hand and blows toward you emitting a dense cloud of spores."
        scene black with Dissolve(1.5)
        e "For a moment, you can't see anything."
        
        jump choice3_done

    label choice3_done:

    
    e "As the cloud disperses, blinking lights emerge all around you. It looks like flashbulbs at a sporting event, but as the room resolves itself around you... "
    scene bg arcade with Dissolve(1.5)

    

    e "...you see that you are in the middle of an old arcade."

    e "In front of you stands another strange figure..."

    show TVmanconfused with moveinright:
        xalign 1.0




    t "WELCOME! To the GREATEST SHOW YOU EVER IMAGINED!"



    


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
