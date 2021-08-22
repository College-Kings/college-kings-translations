# SCENE 5: Imre vs Caleb
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Josh (Outfit 2), Imre (Outfit 4), Caleb (Outfit 2)
# Time: Saturday Night

label v10_imre_vs_caleb_fight:
    play music "music/v10/Scene 4 & 5/Track Scene 4 & 5.mp3" fadein 3
    scene v10ivc3b # TPP. Show Josh in the ring strolling around as if he's adressing a crowd, mouth open.
    with fade

    jo "Eh bien, le spectacle doit continuer."
    
    jo "Après ce petit retard, nous voilà enfin prêts pour le premier combat de la nuit."
    
    jo "Imre contre Caleb !"

    scene v10ivc4b # TPP. Show Imre stepping into the ring.
    with dissolve

    pause 0.75

    scene v10ivc5b # TPP. Show Caleb stepping into the ring.
    with dissolve

    pause 0.75

    scene v10ivc6 # TPP. Show Josh addressing both Imre and Caleb who are stood in opposite corners of the ring, Caleb and Imre angrily starring at eachother, Josh mouth open.
    with dissolve

    jo "Ne vous entretuez pas, restez sur le ring, yada, yada, yada. Amusez-vous !"

    scene v10ivc7 # TPP. Show Josh leaving the ring, Imre and Caleb stepping up closer to eachother, guards up, starring angrilly, Caleb mouth open.
    with dissolve

    cal "Tu ferais mieux d'être prêt, parce que je suis sur le point de danser des cercles autour de toi."

    scene v10ivc8 # TPP. Show Imre, imre drops his guard and sarcastically laughs, mouth open.
    with dissolve 

    imre "J'espère que vous regardez mesdames !"

    scene v10ivc9 # TPP. Show Caleb swinging a punch at Imre, Imre dodges to the side easilly.
    with dissolve

    pause 0.75

    scene v10ivc9a # TPP. Same as ivc9, show Imre, returning from his dodge with a punch square to Caleb's jaw, Caleb in pain, begins to fall.
    with hpunch

    play sound "sounds/hs.mp3"

    pause 0.75

    scene v10ivc9b # TPP. Same as ivc9, Caleb now knocked out on the floor, Imre stood over him with a saractic smile.
    with dissolve

    play sound "sounds/fall.mp3"

    pause 1

    scene v10ivc10 # TPP. Show Josh climbing back into the ring, mouth open looking at Caleb on the floor.
    with dissolve

    jo "Il n'a pas l'air de se lever de sitôt ! Pas sûr que l'un d'entre nous s'attendait à ce que cela se produise si rapidement... Est-il vivant ?"

    scene v10ivc11 # TPP. Show Josh walking around the ring as if he's announcing again, Josh smile.
    with dissolve

    jo "Ah, peu importe, c'est la nuit du combat."

    scene v10ivc12 # TPP. Show Josh now stood with Imre, Josh looking at Imre, both smiling, Josh mouth open.
    with dissolve
    
    jo "Quoi qu'il en soit, on dirait que nous avons un gagnant tout le monde ! Très probablement en un temps record !"

    jo "Un mot à la foule après cette incroyable performance ?"

    scene v10ivc12a # TPP. Same as ivc12, Imre mouth open.
    with dissolve

    imre "À toutes les belles femmes au cul là-bas, c'était pour vous."

    scene v10ivc12
    with dissolve

    jo "On dirait que tu sais pourquoi tu es là !"
    stop music fadeout 3
    jump v10_mc_vs_imre_fight
