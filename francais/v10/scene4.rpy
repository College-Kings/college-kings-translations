# SCENE 4: Ryan vs Perry
# Locations: Abandoned Warehouse
# Characters: Ryan (Outfit 2), Perry (Outfit ), Josh (Outfit 2), 
# Time: Saturday Night
label v9_ryan_v_perry_fight:
    play music "music/v10/Scene 4 & 5/Track Scene 4 & 5.mp3" fadein 3
    scene v10rpf1 # FPP. Show josh, in ring, excited look, mouth open
    with fade
    jo "Eh bien, le spectacle doit continuer."
    
    jo "Après ce petit retard, nous voilà enfin prêts pour le premier combat de la nuit."
    
    jo "Ryan contre Perry !"

    scene v10rpf2 # FPP. Show Ryan and Perry entering the ring, mouths closed
    with dissolve

    pause 0.75

    scene v10rpf3 # FPP. Show close up of josh, excited look, mouth open
    with dissolve
    jo "Ne vous entretuez pas, restez sur le ring, yada, yada, yada. Amusez-vous !"

    scene v10rpf4 # FPP. Show close up of josh exiting the ring, mouth closed
    with dissolve

    pause 0.75

    scene v10rpf2a # FPP. Same camera as v10rpf2, Show Ryan and Perry now in the ring, mouths closed
    with dissolve

    pause 0.75

    scene v10rpf5 # FPP. Show close up of perry, hand up gaurding face, mouth open
    with dissolve
    guyd "Dansons, Ape."

    scene v10rpf6 # FPP. Show close up of Ryan, hand up gaurding his CHEST, mouth open
    with dissolve
    ry "Les Apes ne dansent pas, salope. Nous nous battons."

    scene v10rpf7 # TPP. Show Perry and ryan squaring up to each other in the ring, mouths closed
    with dissolve

    pause 0.75

    scene v10rpf7a # TPP. Same camera as v10rpf7, show perry throwing a punch towards ryan (Not connected yet), mouths closed
    with dissolve

    pause 0.5

    scene v10rpf7b # TPP. Same camera as v10rpf7, Ryan ducking under perrys punch, mouths closed
    with dissolve

    pause 0.5

    scene v10rpf7c # TPP. Same camera as v10rpf7, Ryan gives perry an upper cut to the chin, mouths closed
    with dissolve

    pause 0.5

    scene v10rpf4a # FPP. Show close up of josh entering the ring, mouth closed
    with dissolve

    pause 0.5

    scene v10rpf8 # FPP. Show Josh, mouth open in ring, show perry on floor unconcious, show ryan holding hands in the air, mouth closed
    with dissolve
    jo "Il n'a pas l'air de se lever de sitôt ! Pas sûr que l'un d'entre nous s'attendait à ce que cela se produise si rapidement... Est-il vivant ?"

    jo "Ah, peu importe, c'est la nuit du combat."
    
    jo "Quoi qu'il en soit, on dirait que nous avons un gagnant tout le monde ! Très probablement en un temps record !"

    jo "Un mot à la foule après cette incroyable performance ?"

    scene v10rpf9 # FPP. Show close up of ryan in the ring, mouth open, happy look
    with dissolve

    ry "Je m'échauffe juste."

    scene v10rpf3
    with dissolve

    jo "Vous l'avez entendu ici en premier, Ryan est venu se battre !"
    stop music fadeout 3
    jump v10_mc_vs_ryan_fight

    # -Transition to Scene 6-
