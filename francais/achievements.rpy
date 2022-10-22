init python:
    achievements = []


    class Achievement:
        """
        Achievement data class for storing and managing the creation, syncing and managing of in-game achievements

        Args:
            _achievement (str): Programic name for the achievement
            text (str): Short description of achievement
        """

        def __init__(self, _achievement, text):
            self.achievement = _achievement
            self.text = text

            self.display_name = _achievement.replace("_", " ")

            achievements.append(self)

            # Add achievements to renpy/steam
            achievement.register(_achievement)
            achievement.sync()

        def checkCondition(self):
            return getattr(store, self.condition)


    def grant_achievement(_achievement):
        if path_builder or _in_replay:
            return

        try:
            renpy.show(_achievement, [achievementShow])
        except TypeError: pass
        achievement.grant(_achievement)
        achievement.sync()


# ACHIEVEMENT ITEMS HERE

    # v1
    if renpy.loadable("v1/v1.rpy"):
        Achievement("plaie_ouverte", "Dégage Emily")
        Achievement("pas_de_mauvais_sentiments", "Sois gentil avec Emily")
        Achievement("reste_dans_le_mouv'", "Lance-toi sur Nora")
        Achievement("romeo", "Embrasse Lauren")
        Achievement("grande_gueule", "Menace Cameron")

    # v2
    if renpy.loadable("v2/v2.rpy"):
        Achievement("sentiments_mitiges", "Décline Lauren")
        Achievement("la_celebrite", "Gagne ton premier combat")
        Achievement("un_nouveau_depart", "Lauren t'aime bien")
        Achievement("il_en_fait_trop", "Laisse Benjamin agir")

    # v3
    if renpy.loadable("v3/v3.rpy"):
        Achievement("pas_maintenant_maman", "Refuse l'appel de Julia")
        Achievement("les_levres_ne_mentent_pas", "Embrasse Riley dans le parc")
        Achievement("verite_qui_fait_mal", "Dis à Lauren à propos d'Aubrey")

    # v4
    if renpy.loadable("v4/v4.rpy"):
        Achievement("raviver_le_feu", "Raconte Julia à propos d'Emily")
        Achievement("revanche", "Achète le ballon de volley-ball à Chloé")
        Achievement("l'oeil_vif", "Choisis le muffin")

    # v5
    if renpy.loadable("v5/v5.rpy"):
        Achievement("touche_le_fond", "Refuse le contact avec Lauren")
        Achievement("ennemi_public_peta", "Tue le chien en tant qu'amoureux des animaux")
        Achievement("balance", "Préviens l'école")

    # v6
    if renpy.loadable("v6/v6.rpy"):
        Achievement("des_freres_pas_des_putes", "Aide Imre")
        Achievement("affaire_de_singes", "Rejoins les Apes")
        Achievement("pas_mes_affaires", "Ne dérange pas Mme Rose")
        Achievement("reunification", "Embrasse Emily en retour")
        Achievement("credule", "Fais confiance en Chloé")
        Achievement("suspect", "Ne rejoins pas Grayson")
        Achievement("strike", "Embrasse Pénélope")

    # v7
    if renpy.loadable("v7/v7.rpy"):
        Achievement("fidele_a_toi_meme", "Rentre avec Riley")
        Achievement("gorille_dos_argente", "Engage-toi chez les Apes")
        Achievement("meute_de_loups", "Engage-toi chez les Wolves")
        Achievement("la_voie_de_lee", "Baisse le pantalon de Mr Lee")
        Achievement("extatique", "Homecoming chez Amber")
        Achievement("lent_et_stable", "Finis le homecoming avec Lauren")
        Achievement("joue_avec_le_feu", "Finis le homecoming avec Riley")
        Achievement("homecoming_avec_la_reine", "Finis le homecoming avec Chloé")

    # v8
    if renpy.loadable("v8/scene1.rpy"):
        Achievement("epais_et_fin", "Aide Pénélope")
        Achievement("texte_avec_un_s", "Retour à l'expéditeur")
        Achievement("le_7_chanceux", "Les lumières scintillantes de l'arcade")
        Achievement("garde_du_corps", "Gagne le combat de ruelle")
        Achievement("prenez_une_chambre", "Reste avec Amber chez Josh")
        Achievement("coup_de_main", "Aide Nora à distribuer des prospectus pour le voyage")
        Achievement("pour_en_savoir_plus", "Flirte avec Chloé au Steakhouse")

    # v9
    if renpy.loadable("v9/scene01.rpy"):
        Achievement("jour_de_detente", "Amuse-toi avec Aubrey au lac")
        Achievement("le_roi_du_nord", "Le Roi se dirige vers le Nord")
        Achievement("rentre_chez_toi", "Frappe le gars dans le couloir")
        Achievement("deuxieme_rendez-vous", "Obtiens un deuxième rendez-vous avec Evelyn")
        Achievement("tricherie", "Oublie la salle de gym et va avec Riley")
        Achievement("mauvais_moment", "N'embrasse pas Lindsey")

    # v10
    if renpy.loadable("v10/scene1.rpy"):
        Achievement("extinction_des_feux", "Bats Ryan en difficulté difficile au Brawl")
        Achievement("club_de_la_peur", "Ne te bats pas contre Ryan au Brawl")
        Achievement("golden_boy", "Bats Imre en difficulté difficile au Brawl")
        Achievement("freres_avant_les_coups", "Ne te bats pas contre Imre au Brawl")
        Achievement("groar_je_suis_un_lion", "Dis à Lauren que tu aimes les Lions")
        Achievement("nettoyage", "Amuse-toi dans la salle de bain")
        Achievement("romance_interdite", "Embrasse Mme Rose")
        Achievement("figures_rudes", "Amuse-toi au skatepark")
        Achievement("secret_de_famille", "Découvre que Nora et Mme Rose sont de la même famille")
        Achievement("sur_le_terrain", "Fais la revanche avec Chloé")
        Achievement("decisions_difficiles", "Dis à Chloé ce qu'a dit Nora")

    #v11
    if renpy.loadable("v11/scene1.rpy"):
        Achievement("perry_mason", "Défends Pénélope avec succès")
        Achievement("casse-bonbons", "Scène de sexe avec Candy")
        Achievement("tiens_ton_cheval", "Équilibre le cheval à la fin de la chasse à l'homme")
        Achievement("descends de ton haut cheval", "N'équilibre pas le cheval à la fin de la chasse à l'homme")
        Achievement("croise_ton_cœur", "Embrasse Pénélope à l'aéroport")
        Achievement("pleine_visee", "Fais mouche chez Duncan")
        Achievement("juste_une_theorie", "Dis à Riley que les dinosaures n'ont pas existé")
        Achievement("fruite", "Prendre un cocktail au bar")
        Achievement("gagne_ton_hibou", "Obtiens toutes les bonnes réponses HP")
        Achievement("stratege_politique", "Dis à Autumn que tu t'intéresses à la politique et encourage Lindsey à se présenter.")
        Achievement("deux_temps", "Sors avec Lauren et Chloé")
        Achievement("ne_reste_pas_plante_la", "Sépare Imre et Ryan")
        Achievement("jolie_en_rose", "Nora achète le soutien-gorge rose")

    #v12
    if renpy.loadable("v12/scene1.rpy"):
        Achievement("bon_vs_mal", "Pénélope te comprend")
        Achievement("une_personne_comme_moi", "Tu te vois comme le mari de Pénélope.")
        Achievement("de_zero_en_heros", "Dis à Riley que tu es pauvre")
        Achievement("ordonnances du medecin", "Accepte les avances d'Aubrey, l'infirmière")
        Achievement("meurtre_par_pitie", "Tue Imre")
        Achievement("parle-moi_d'assassinat", "Tue Samantha")
        Achievement("le_meilleur_pour_la_fin", "Charli est ta dernière victime")
        Achievement("armes_abaissees", "Ne tue personne")
        Achievement("folie_meurtrière", "Tue suffisamment de monde pour gagner le jeu")
        Achievement("assurances_collectives", "Tue tout le monde (y compris les personnages optionnels)")
        Achievement("jetee_aux_lionnes", "Encourage Lindsey à se présenter mais parle en ensuite à Aubrey et Chloé.")
        Achievement("vous_pouvez_embrasser_la_mariée.", "Embrasse Nora devant l'autel")
        Achievement("un_pari_est_un_pari", "Photo embarrassante sur Kiwii après avoir perdu la course")
        Achievement("fraternite_d'hommes", "Défends Chris à chaque fois en tant que Wolf")
        Achievement("meilleurs_frenemies", "Défends Chris à chaque fois en tant que Ape")
        Achievement("L'attente_vaut_le_coup", "Vis une relation exclusive avec Lauren")
        Achievement("amour_au_boulot", "Faire l'amour avec Nora en tant que Wolf")
        Achievement("tout_est_juste_dans_l'amour_et_la_guerre", "Faire l'amour avec Nora en tant que Ape")
        Achievement("ville_de_l'amour", "Fais l'amour avec Lauren, Nora, Mme Rose et Lindsey")

    #v13
    if renpy.loadable("v13/scene1.rpy"):
        Achievement("indecis", "N'aide ni Chloé, ni Lindsey")
        Achievement("nuit_amusante", "Oui Pénélope, tu voles")
        Achievement("Les_gentlemen_preferent_les_homos", "Renonce aux câlins de Lauren")
        Achievement("chasse_d'eau", "Rince la brosse à dents de Charli")
        Achievement("il_est_foutu", "Dénonce Charli")
        Achievement("urbain_a_femmes", "Dis à Emmy et Lauren que tu es un mec de la ville.")
        Achievement("cœur_romantique", "Obtiens un rencart avec Kourtney")
        Achievement("instant_de_freres", "Cameron reconnaît tes pures intentions")
        Achievement("un_menteur_honete", "Découvre Clipps")
        Achievement("nous_les_aimons_sauvages", "Révèle une nouvelle facette de Chloé")
        Achievement("voyeur", "Qu'est-ce qu'ils font là-bas ?")
        Achievement("maudite_emily", "Sexe dans les toilettes en colère")
        Achievement("reste_tranquille_mon_gars", "Respecte Nora")

    #v14
    if renpy.loadable("v14/scene1.rpy"):
        Achievement("troisieme_joueur_pret", "Trio avec Riley et Aubrey")
        Achievement("sauver_le_soldat_ryan", "Ne laisse pas Ryan attraper une MST")
        Achievement("beastie_boy", "Sabote la vente de pâtisseries")
        Achievement("agent_double", "Aide les campagnes de Chloé et de Lindsey")
        Achievement("accepte_de_ne_pas_etre_d'accord", "Chris n'aide pas Chloé")
        Achievement("comment_t'as_su", "Achète à Amber ses bonbons préférés")
        Achievement("confiance_fondee", "Fais confiance à ta petite amie Chloé avec son ex")
        Achievement("colere_de_pen", "Pénélope fait un scandale au restaurant")
        Achievement("tes_paupieres_sont_lourdes", "Lauren utilise ses pouvoirs d'hypnose pour faire le bien")
        Achievement("dis_cuicui", "Prends une photo avec l'oiseau")
        Achievement("grand_theft_chloe", "Vole le journal intime et tout l'argent")
        Achievement("nettoie-les", "Avoir une influence positive sur Amber et Samantha")

    #v15
    if renpy.loadable("v15/scene1.rpy"):
        Achievement("en_rut", "Coup d'œil sur Autumn") #s4
        Achievement("da_ba_dee_da_ba_dai", "I'm Blue") #s4
        Achievement("contre-espionnage", "Lindsey s'attendait à cette stratégie") #s12
        Achievement("huumm_un_donut", "Mange le donut") #s13
        Achievement("ours_a_miel", "Lèche les pancakes de Mme Rose") #s15
        Achievement("saison_des_citrouilles", "Tu aimes vraiment cette citrouille, hein ?") #s18
        Achievement("souvenirs_d'enfance", "Surprends la fille qui fête son anniversaire") #s18
        Achievement("maitre_d'oeuvre", "termine la checklist") #s18
        Achievement("trop_d'informations", "Vérifie souvent tes notes de réunion") #s21
        Achievement("chantage_emotionnel", "Menace Mme Rose") #s21
        Achievement("karen", "Où est votre responsable ?!") #s24
        Achievement("polycurieux", "La monogamie est surfaite") #s26
        Achievement("fromage_bleu_et_sambuca", "Le pire traiteur de mariage de tous les temps") #s33
        Achievement("qu'est-ce_qui_se_passe", "Aubrey goûte à sa propre médecine au mariage") #s33
        Achievement("encore_une_chose", "Découvre toutes les pistes et résous l'affaire") #s46
# TODO: Translation updated at 2022-10-22 12:20

translate francais strings:

    # game/achievements.rpy:40
    old "Tell off Emily"
    new "Tell off Emily"

    # game/achievements.rpy:41
    old "Play nice with Emily"
    new "Play nice with Emily"

    # game/achievements.rpy:42
    old "Hit on Nora"
    new "Hit on Nora"

    # game/achievements.rpy:44
    old "Threaten Cameron"
    new "Threaten Cameron"

    # game/achievements.rpy:48
    old "Decline Lauren"
    new "Decline Lauren"

    # game/achievements.rpy:49
    old "Win your first fight"
    new "Win your first fight"

    # game/achievements.rpy:50
    old "Lauren likes you"
    new "Lauren likes you"

    # game/achievements.rpy:51
    old "Let Benjamin make a move"
    new "Let Benjamin make a move"

    # game/achievements.rpy:55
    old "Decline Julia's call"
    new "Decline Julia's call"

    # game/achievements.rpy:56
    old "Kiss Riley at the Park"
    new "Kiss Riley at the Park"

    # game/achievements.rpy:57
    old "Tell Lauren about Aubrey"
    new "Tell Lauren about Aubrey"

    # game/achievements.rpy:61
    old "Tell Julia about Emily"
    new "Tell Julia about Emily"

    # game/achievements.rpy:62
    old "Buy Chloe the volleyball"
    new "Buy Chloe the volleyball"

    # game/achievements.rpy:63
    old "Pick the muffin"
    new "Pick the muffin"

    # game/achievements.rpy:67
    old "Deny PDA with Lauren"
    new "Deny PDA with Lauren"

    # game/achievements.rpy:68
    old "Kill dog as animal lover"
    new "Kill dog as animal lover"

    # game/achievements.rpy:74
    old "Join the Apes"
    new "Join the Apes"

    # game/achievements.rpy:75
    old "Don't disturb Ms. Rose"
    new "Don't disturb Ms. Rose"

    # game/achievements.rpy:76
    old "Kiss Emily back"
    new "Kiss Emily back"

    # game/achievements.rpy:77
    old "Trust Chloe"
    new "Trust Chloe"

    # game/achievements.rpy:78
    old "Don't meet Grayson"
    new "Don't meet Grayson"

    # game/achievements.rpy:79
    old "Kiss Penelope"
    new "Kiss Penelope"

    # game/achievements.rpy:83
    old "Walk home with Riley"
    new "Walk home with Riley"

    # game/achievements.rpy:86
    old "Pull down Mr. Lee's pants"
    new "Pull down Mr. Lee's pants"

    # game/achievements.rpy:87
    old "Bunk homecoming with Amber"
    new "Bunk homecoming with Amber"

    # game/achievements.rpy:88
    old "End homecoming with Lauren"
    new "End homecoming with Lauren"

    # game/achievements.rpy:89
    old "End homecoming with Riley"
    new "End homecoming with Riley"

    # game/achievements.rpy:90
    old "End homecoming with Chloe"
    new "End homecoming with Chloe"

    # game/achievements.rpy:95
    old "Return to sender"
    new "Return to sender"

    # game/achievements.rpy:96
    old "Flashing lights at the arcade"
    new "Flashing lights at the arcade"

    # game/achievements.rpy:97
    old "Win the alley fight"
    new "Win the alley fight"

    # game/achievements.rpy:98
    old "Stay with Amber at Josh's"
    new "Stay with Amber at Josh's"

    # game/achievements.rpy:99
    old "Help Nora hand out flyers for the trip"
    new "Help Nora hand out flyers for the trip"

    # game/achievements.rpy:100
    old "Flirt with Chloe at the Steakhouse"
    new "Flirt with Chloe at the Steakhouse"

    # game/achievements.rpy:104
    old "Have fun with Aubrey at the lake"
    new "Have fun with Aubrey at the lake"

    # game/achievements.rpy:105
    old "The King is heading North"
    new "The King is heading North"

    # game/achievements.rpy:106
    old "Punch the guy in the hallway"
    new "Punch the guy in the hallway"

    # game/achievements.rpy:107
    old "Get a second date with Evelyn"
    new "Get a second date with Evelyn"

    # game/achievements.rpy:108
    old "Skip the gym and get with Riley"
    new "Skip the gym and get with Riley"

    # game/achievements.rpy:109
    old "Don't kiss Lindsey"
    new "Don't kiss Lindsey"

    # game/achievements.rpy:113
    old "Beat Ryan on Hard difficulty at the Brawl"
    new "Beat Ryan on Hard difficulty at the Brawl"

    # game/achievements.rpy:114
    old "Don't fight Ryan at the Brawl"
    new "Don't fight Ryan at the Brawl"

    # game/achievements.rpy:115
    old "Beat Imre on Hard difficulty at the Brawl"
    new "Beat Imre on Hard difficulty at the Brawl"

    # game/achievements.rpy:116
    old "Don't fight Imre at the Brawl"
    new "Don't fight Imre at the Brawl"

    # game/achievements.rpy:117
    old "Tell Lauren you like Lions"
    new "Tell Lauren you like Lions"

    # game/achievements.rpy:118
    old "Have fun in the bathroom"
    new "Have fun in the bathroom"

    # game/achievements.rpy:119
    old "Kiss Ms. Rose"
    new "Kiss Ms. Rose"

    # game/achievements.rpy:120
    old "Have fun at the skatepark"
    new "Have fun at the skatepark"

    # game/achievements.rpy:121
    old "Find out Nora and Ms. Rose are family"
    new "Find out Nora and Ms. Rose are family"

    # game/achievements.rpy:122
    old "Have a rematch with Chloe"
    new "Have a rematch with Chloe"

    # game/achievements.rpy:123
    old "Tell Chloe what Nora said"
    new "Tell Chloe what Nora said"

    # game/achievements.rpy:127
    old "Successfully defend Penelope"
    new "Successfully defend Penelope"

    # game/achievements.rpy:128
    old "Have fun with Candy"
    new "Have fun with Candy"

    # game/achievements.rpy:129
    old "Balance the horse at the end of the manhunt"
    new "Balance the horse at the end of the manhunt"

    # game/achievements.rpy:130
    old "Don't balance the horse at the end of the manhunt"
    new "Don't balance the horse at the end of the manhunt"

    # game/achievements.rpy:131
    old "Kiss Penelope at the airport"
    new "Kiss Penelope at the airport"

    # game/achievements.rpy:132
    old "Hit a bullseye at Duncan's"
    new "Hit a bullseye at Duncan's"

    # game/achievements.rpy:133
    old "Tell Riley dinosaurs aren't real"
    new "Tell Riley dinosaurs aren't real"

    # game/achievements.rpy:134
    old "Have a cocktail at the bar"
    new "Have a cocktail at the bar"

    # game/achievements.rpy:135
    old "Get all the HP answers right"
    new "Get all the HP answers right"

    # game/achievements.rpy:136
    old "Tell Autumn you're into politics and encourage Lindsey to run"
    new "Tell Autumn you're into politics and encourage Lindsey to run"

    # game/achievements.rpy:137
    old "Date both Lauren and Chloe"
    new "Date both Lauren and Chloe"

    # game/achievements.rpy:138
    old "Break Imre and Ryan apart"
    new "Break Imre and Ryan apart"

    # game/achievements.rpy:139
    old "Nora buys the pink bra"
    new "Nora buys the pink bra"

    # game/achievements.rpy:143
    old "Penelope understands you"
    new "Penelope understands you"

    # game/achievements.rpy:144
    old "You see yourself as Penelope's husband material"
    new "You see yourself as Penelope's husband material"

    # game/achievements.rpy:145
    old "Tell Riley you are poor"
    new "Tell Riley you are poor"

    # game/achievements.rpy:146
    old "Accept Nurse Aubrey's advances"
    new "Accept Nurse Aubrey's advances"

    # game/achievements.rpy:147
    old "Kill Imre"
    new "Kill Imre"

    # game/achievements.rpy:148
    old "Kill Samantha"
    new "Kill Samantha"

    # game/achievements.rpy:149
    old "Charli is your final kill"
    new "Charli is your final kill"

    # game/achievements.rpy:150
    old "Don't kill anyone"
    new "Don't kill anyone"

    # game/achievements.rpy:151
    old "Kill enough people to win the game"
    new "Kill enough people to win the game"

    # game/achievements.rpy:152
    old "Kill everyone (including optional characters)"
    new "Kill everyone (including optional characters)"

    # game/achievements.rpy:153
    old "Encourage Lindsey to run but then tell Aubrey and Chloe about it"
    new "Encourage Lindsey to run but then tell Aubrey and Chloe about it"

    # game/achievements.rpy:154
    old "Kiss Nora at the altar"
    new "Kiss Nora at the altar"

    # game/achievements.rpy:155
    old "Embarrassing Kiwii picture for losing the race"
    new "Embarrassing Kiwii picture for losing the race"

    # game/achievements.rpy:156
    old "Defend Chris every time as a Wolf"
    new "Defend Chris every time as a Wolf"

    # game/achievements.rpy:157
    old "Defend Chris every time as an Ape"
    new "Defend Chris every time as an Ape"

    # game/achievements.rpy:158
    old "Consummate an exclusive relationship with Lauren"
    new "Consummate an exclusive relationship with Lauren"

    # game/achievements.rpy:159
    old "Have sex with Nora as a Wolf"
    new "Have sex with Nora as a Wolf"

    # game/achievements.rpy:160
    old "Have sex with Nora as an Ape"
    new "Have sex with Nora as an Ape"

    # game/achievements.rpy:161
    old "Have sex with Lauren, Nora, Ms. Rose and Lindsey"
    new "Have sex with Lauren, Nora, Ms. Rose and Lindsey"

    # game/achievements.rpy:165
    old "Help neither Chloe nor Lindsey"
    new "Help neither Chloe nor Lindsey"

    # game/achievements.rpy:166
    old "Yes Penelope, you're flying"
    new "Yes Penelope, you're flying"

    # game/achievements.rpy:167
    old "Bail on Lauren's cuddles"
    new "Bail on Lauren's cuddles"

    # game/achievements.rpy:168
    old "Flush Charli's toothbrush"
    new "Flush Charli's toothbrush"

    # game/achievements.rpy:169
    old "Expose Charli"
    new "Expose Charli"

    # game/achievements.rpy:170
    old "Tell Emmy and Lauren you're a city man"
    new "Tell Emmy and Lauren you're a city man"

    # game/achievements.rpy:171
    old "Score a date with Kourtney"
    new "Score a date with Kourtney"

    # game/achievements.rpy:172
    old "Cameron recognizes your pure intentions"
    new "Cameron recognizes your pure intentions"

    # game/achievements.rpy:173
    old "Own up to Clipps"
    new "Own up to Clipps"

    # game/achievements.rpy:174
    old "Reveal a new side of Chloe"
    new "Reveal a new side of Chloe"

    # game/achievements.rpy:175
    old "What are they doing over there?"
    new "What are they doing over there?"

    # game/achievements.rpy:176
    old "Angry bathroom sex"
    new "Angry bathroom sex"

    # game/achievements.rpy:177
    old "Respect Nora"
    new "Respect Nora"

    # game/achievements.rpy:181
    old "Three-way with Riley and Aubrey"
    new "Three-way with Riley and Aubrey"

    # game/achievements.rpy:182
    old "Don't let Ryan catch an STD"
    new "Don't let Ryan catch an STD"

