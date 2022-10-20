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
