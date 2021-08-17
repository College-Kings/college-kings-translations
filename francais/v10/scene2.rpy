# SCENE 2: Ryan vs Perry
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Chris (Outfit ), Perry (Outfit ), Josh (Outfit 2), 
# Time: Saturday Night

label v10_ryan_v_perry:
    play music "music/v10/Scene 2 & 3/Track Scene 2 & 3.mp3" fadein 3
    scene v10rvp1 # FPP. Show Josh in the ring walking around, taking the announcer role in his stride. Mouth open.
    with dissolve

    jo "Mesdames et Messieurs, le moment est venu de commencer notre premier match. Dans le coin des Wolves, nous avons Perry !"

    scene v10rvp2 # FPP. Show Perry stood next to Chris just outside the ring, perry looks super worried, Chris smile, Perry mouth open.
    with dissolve

    guyd "Je ne peux pas faire ça. Je vais être malade."

    scene v10rvp2a # FPP. Same as rvp2, Chris and Perry both looking at eachother, Chris smile, Perry worried, Chris mouth open.
    with dissolve

    ch "Bien sûr tu peux. Tu es un loup. Tu as ça ! Tu tu sentiras mieux une fois dedans."

    scene v10rvp2b # FPP. Same as rvp2, Chris no longer has his hand on perry, Chris looks slightly concerned, perry with his hand on his stomach as if he's about to puke, Perry mouth open.
    with dissolve

    guyd "J'y vais..."

    scene v10rvp3 # TPP. Show Josh now looking in the direction of Perry, josh looks a little confused.
    with dissolve

    pause 1

    stop music fadeout 3

    jump v9_ryan_v_perry_fight
