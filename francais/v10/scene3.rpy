# SCENE 3: First Matchup - Imre vs Caleb (Apes)
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Grayson (Outfit 3), Josh (Outfit 2), 
# Time: Saturday Night

label v10_imre_vs_caleb:
    scene v10ivc1 # TPP. Show MC walking towards the ring, Josh in ring in tux, mouths closed, nerutal expressions-
    with fade
    play music "music/v10/Scene 2 & 3/Track Scene 2 & 3.mp3" fadein 3
    pause 0.5

    scene v10ivc2 # FPP. Show Josh in the ring, mouth closed, slight smile
    with dissolve
    u "(Voyons qui est debout en premier)"

    scene v10ivc2a # FPP. Same Camera as v10ivc2, Show josh with his left hand held up pointing to Imre, neutral expression, josh mouth open
    with dissolve
    jo "Mesdames et Messieurs, le moment est venu de commencer notre premier match. Dans le coin des Wolves, nous avons Imre !"

    scene v10ivc2b # FPP. Same Camera as v10ivc2, Show josh with his left hand held up pointing to Imre, neutral expression, josh mouth closed
    with dissolve
    u "Bouhhh!"

    scene v10ivc2c # FPP. Same Camera as v10ivc2, Show josh with his right other hand held up pointing to Caleb, neutral expression, josh mouth open
    with dissolve
    jo "Et pour les Apes, nous avons Caleb !"

    scene v10ivc2d # FPP. Same Camera as v10ivc2, Show josh with his right other hand held up pointing to Caleb, neutral expression, josh mouth closed
    with dissolve
    u "Wouhhhh!"

    scene v10ivc3 # FPP. Show Caleb, hand over his mouth looking like he's going to be sick, mouth closed
    with dissolve
    # -MC turns to Caleb to cheer him on and sees Caleb clutching his stomach-
    u "Oh non ! Qu'est-ce qui ne va pas ?"

    scene v10ivc3a # FPP. Same Camera as v10ivc3, Show Caleb, hand now slightly lowered looking like he's going to be sick, mouth open
    with dissolve
    cal "Je ne pense pas pouvoir faire ?a. Je me sens...malade."

    scene v10ivc4 # FPP. Show Grayson, pointing at caleb, slight angry face, caleb hand over mouth, Grayson mouh open
    with dissolve
    gr "Putain, mec. Rien de cette merde ! Suce-le et monte dans ce ring !"

    scene v10ivc5 # FPP. Show Caleb running for the door to go puke
    with dissolve

    pause 0.5

    scene v10ivc2e # FPP. Same Camera as v10ivc2,Show Josh in the ring, mouth open, slight smile
    with dissolve
    jo "Bien, maintenant..."
    
    stop music fadeout 3

    jump v10_imre_vs_caleb_fight
