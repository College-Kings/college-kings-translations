# SCENE 13: MC at wolves house/redecorate
# Locations: Wolves house/MC Wolves Room/MC New Wolves Room
# Characters: MC (Outfit 1), Chris (Outfit 1), Perry (Outfit 1)
# Time: Sunday Morning
# If you need paint and brush use industrial clutter 2: https://mega.nz/file/4YgihJxL#CC_JVYehPM-krceVG1d7x-0K8MNhwfIAfwtLVDjrQ3I

label v10_wolves_redec:
    if v10s10_hangWLinds:
        scene v10swhr1 # TPP. Show MC walking through the front door of the Wolves house.
        with Fade(1, 0, 1)

        play sound "sounds/dooropen.mp3"

    else:
        scene v10swhr8 # TPP. Show MC walking down the stairs of the Wolves house.
        with Fade(1, 0, 1)

    pause 0.75

    play music "music/v10/Scene 13/Track Scene 13.mp3" fadein 3

    scene v10swhr2 # FPP. Show Chris stood in the Wolves hallway this angle must make sense for both whr1 & whr8, Chris neutral, mouth closed.
    with dissolve

    u "Hé Chris, j'apprécie vraiment la chambre et tout le reste, mais je n'ai pas encore eu l'occasion de la faire crier [name]. C'est cool si je l'améliore un peu ?"

    scene v10swhr2a # FPP. Same as whr2, Chris neutral, mouth open.
    with dissolve

    ch "Je me demandais quand tu en aurais assez des murs blancs. Il y a des fournitures dans le placard de ta chambre. En fait, on se prépare à décorer toute la maison."

    scene v10swhr2
    with dissolve

    u "Vraiment ! ? Bon timing haha. Vous avez un thème en tête ?"

    scene v10swhr2a
    with dissolve

    ch "Ouais, mec ! Fais en sorte que ça crie \"Wolves\", tu vois ?"

    scene v10swhr2
    with dissolve

    u "Oui, ça a l'air génial !"

    scene v10swhr2a
    with dissolve

    ch "Vas-y, mec ! Amuse-toi bien."

    scene v10swhr3 # TPP. Show MC looking for supplies in his closet in his room, in the closet there should be some tins of paint and brushes.
    with fade

    pause 0.75
    
    scene v10swhr4 # FPP. Show Perry stood at the door of MC's room, Perry neutral, mouth open.
    with dissolve

    guyd "Hé mec..."

    scene v10swhr4a # FPP. Same as whr4, Perry neutral, mouth closed.
    with dissolve

    u "Hé, on dirait que tu te caches depuis le combat.."

    scene v10swhr4
    with dissolve

    guyd "Oui, un peu. Qu'est-ce que tu fais dans le placard ?"

    scene v10swhr4a
    with dissolve

    u "Je me prépare à décorer ma chambre.."

    scene v10swhr4b # FPP. Same as whr4, Perry smile, mouth open.
    with dissolve

    guyd "Oh wow, tu veux de l'aide ?"

    scene v10swhr4c # FPP. Same as whr4, Perry smile, mouth closed.
    with dissolve

    menu:
        "Accepter l'aide":
            $ addPoint("bro", 1)

            $ v10_perry_help_room = True

            u "Oui, j'aimerais avoir de l'aide. Ça ira beaucoup plus vite, haha."

            scene v10swhr5 # TPP. Show Perry and MC stood near a wall both looking around thinking about where to start, paint brushes in hand and tins of white paint next to them on the floor.
            with fade

            pause 0.75

            scene v10swhr6 # FPP. Show Perry, neutral expression, mouth closed.
            with dissolve

            u "Hé mec, j'espère que ça ne te dérange pas que je demande, mais qu'est-ce qui t'a fait reculer à la bagarre ?"

            scene v10swhr6a # FPP. Same as whr6, slight embarrassed expression, mouth open.
            with dissolve

            guyd "J'attendais que tu en parles. C'est un peu embarrassant, mec."

            scene v10swhr6b # FPP. Same as whr6, slight embarrassed expression, mouth closed.
            with dissolve

            u "Embarrassant ? Qu'est-ce qu'il y a ?"

            scene v10swhr6a
            with dissolve

            guyd "Si j'ai fui et choisi de ne pas me battre, ce n'est pas parce que je ne voulais pas, c'est parce que je ne pouvais pas."

            scene v10swhr6b
            with dissolve

            u "Comment ça, tu ne pourrais pas ?"

            scene v10swhr6a
            with dissolve

            guyd "Mec, je suis malade..."

            scene v10swhr6b
            with dissolve

            u "Malade de quoi ?"

            scene v10swhr6a
            with dissolve

            guyd "Tu sais, les sushis qu'on avait dans le frigo depuis un moment ?"

            scene v10swhr6b
            with dissolve

            u "Ouai."

            scene v10swhr6a
            with dissolve

            guyd "Je l'ai mangé juste avant le combat parce que j'avais faim et que je n'avais jamais mangé de sushi avant. Il s'avère que je suis allergique."

            scene v10swhr6b
            with dissolve

            u "Tu es sérieux !?"

            scene v10swhr6a
            with dissolve

            guyd "Malheureusement, oui. Que je sois malade ou non, les gars n'étaient toujours pas contents."

            scene v10swhr6b
            with dissolve

            u "Au moins, tu avais une bonne raison."

            scene v10swhr6c # FPP. Same as whr6, smile, mouth open.
            with dissolve

            guyd "Ouais, la prochaine fois, j'y vais comme une bête."

            scene v10swhr6d # FPP. Same as whr6, smile, mouth closed.
            with dissolve

            u "Heureux de l'entendre."

            scene v10swhr7 # TPP. Show wide shot of MC's new wolves room.
            with Fade(1, 0, 1)

            guyd "La chambre a l'air plutôt bien."

            u "Oui, c'est beaucoup mieux, la moquette et les rideaux finissent vraiment le travail. Merci, mec !"

            guyd "Quand tu veux."

        "Refusez l'aide":
            u "J'apprécie, mais ça va. Cela va demander toute ma concentration."

            scene v10swhr4b
            with dissolve

            guyd "Très bien, mec."

            scene v10swhr3
            with dissolve

            pause 0.75

            scene v10swhr7 # TPP. Show wide shot of MC's new wolves room.
            with Fade(1, 0, 1)             

            u "(Voilà ce que je veux dire !)"          
    stop music fadeout 3  

    jump v10_call_with_lauren1