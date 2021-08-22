# SCENE 1: Outside Scuffle
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7),Imre (Outfit 4), Sebastian (Outfit 1), Cameron (Outfit 3), Ryan (Outfit 2)
# Time: Saturday Night
 
label v10start:
   scene v10sta1 # FPP. Show Imre and ryan on the floor fighting, imre on bottom, ryan on top, angry faces, mouths closed
   with dissolve
   u "Qu'est ce que vous faites les gars !?"

   play music "music/v10/Scene 1/Track Scene 1.mp3" fadein 3

   scene v10sta2 # FPP. Show MC trying to pull Ryan and imre apart, imre/ryan angry, mc worried look, mouths closed
   with dissolve
 
   pause 0.75
 
   if joinwolves:

        scene v10sta2 # FPP. Show Imre and ryan now standing in fighting stances both with fists raised, angry look on imre/ryan, ryan mouth closed, imre mouth open
        with dissolve

        imre "Reste à ta putin de place [name]! C'est mon combat."

        scene v10sta2       
        with dissolve

        ry "Vous allez regretter de ne pas avoir rappelé votre remplaçant."

   else:
        scene v10sta2
        with dissolve
  
        ry "Non ! C'est mon combat ! N'interfère pas putain !"
 
        scene v10sta3
        with dissolve

        imre "Je vais te défoncer la tête tout de suite."

        scene v10sta3a # FPP. Same camera as v10sta3, angry look on imre/ryan, ryan mouth open, imre mouth closed

        with dissolve

        ry "Vous ne pouvez pas cogner la tête de quelqu'un s'il vous donne une putain de machine à cogner la tête !"

        scene v10sta3b # FPP. Same camera as v10sta3, Imre and ryan grappling each other, sebastian pulling away imre, cameron pulling away ryan, angry faces, imre/ryan/cameron closed mouths, Sebastian mouth open.
        with dissolve
 
        se "D'accord les gars, mieux vaut s'arrêter ici avant que ça devienne embarrassant."
 
        scene v10sta3c
        with dissolve
 
        ca "Pourquoi putain le combattrais-tu ?! Va pour un putain de punch si tu le penses vraiment !"

   stop music fadeout 3

   if joinwolves:
       scene v10sta4a # FPP. Same Camera as v10sta4, imre now left scene, Show Sebastian near the warehouse doors facing camera, neutral look, mouth open
       with dissolve
 
       se "Pourquoi putain le combattrais-tu ?! Va pour un putain de punch si tu le penses vraiment !"
 
       jump v10_ryan_v_perry
   else:
       scene v10sta5 # FPP. Show Cameron Facing Camera, neutral look, mouth open
       with dissolve
 
       ca "Vous n'avez pas un combat à préparer ?"
 
       scene v10sta5a # FPP. Same camera as v10sta5,Show Cameron Facing Camera, neutral look, mouth closed
       with dissolve
 
       u "(Cela devrait être un putain de spectacle.)"
 
       scene v10sta6 # TPP. Show MC back to camera heading towards warehouse
       with dissolve

       jump v10_imre_vs_caleb
