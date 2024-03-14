import re
import matplotlib.pyplot as plt
import spacy

nlp = spacy.load("fr_core_news_sm")

#Pour decomposer le texte en liste de phrase 
def analyse_texte(fichier_input):
    with open(fichier_input, "r", encoding="utf-8") as fichier_analyse:
        texte_analyse = fichier_analyse.read()
    
    #on cree les regles
    liste_phrases = re.findall("[A-Z\"«»“”].*?[.?!]+", texte_analyse, flags=re.DOTALL)
    return liste_phrases

#Pour avoir le nombre de mots moyen par phrases
def nombre_mots_moyen_par_phrase(liste_phrases):
    nombre_phrases = len(liste_phrases)
    total_mots = sum(len(phrase.split()) for phrase in liste_phrases)
    moyenne_mot = total_mots / nombre_phrases 
    return moyenne_mot


#Pour trouver le nombre de mot le plus frequent  en fonction de ce quon lui donne
def mots_frequents(liste_phrases, nb_frequent):
    mots_comptes = {}

    for phrase in liste_phrases:
        mots = re.findall(r"\w+(?:-\w+|'\w+)?", phrase, flags=re.DOTALL)
        for mot in mots:
            if mot in mots_comptes:
                mots_comptes[mot] += 1
            else:
                mots_comptes[mot] = 1

    
    #Apres avoir compté le mot maintenant on trouve l'occurence max des mots
    mots_frequents = []
    compteur = 0
    while compteur < nb_frequent:
        mot_max_occurrences = ""
        max_occurrences = 0
        for mot, occurrences in mots_comptes.items():
            if occurrences > max_occurrences and mot not in [mot_occur[0] for mot_occur in mots_frequents]:
                mot_max_occurrences = mot
                max_occurrences = occurrences
        if mot_max_occurrences:
            mots_frequents.append((mot_max_occurrences, max_occurrences))
            compteur += 1
        else:
            break
    
    return mots_frequents


#Compteur des type de mot donc Singulier , Pluriel , Masculin , Feminin Pronom et si cest un Verbe
def compteur_type_mot(liste_phrases , nb_mots_singulier, nb_mots_pluriel, nb_mots_masculin, nb_mots_feminin, nb_pronom, nb_verbes):

    for phrase in liste_phrases:
        doc = nlp(phrase)
        for mot in doc:

            #Compteur de mots singulier et  pluriel
            #print(mot.morph.get("Number")[0])
            mot_nombre= mot.morph.get("Number")
            if mot_nombre :
                if mot_nombre[0] == "Sing":
                    nb_mots_singulier += 1
                elif mot_nombre[0] == "Plur":
                    nb_mots_pluriel += 1
            
            
            #print(mot.morph.get("Gender"))
                
            mot_genre= mot.morph.get("Gender")
            #print(mot_genre)
            if mot_genre :
                if mot_genre[0] == "Masc":
                    nb_mots_masculin += 1
                elif mot_genre[0] == "Fem":
                    nb_mots_feminin += 1
            
            #Compteur d'articles
            # print(mot.tag_)
            if mot.tag_ == "PRON":
                nb_pronom += 1
            
            #Compteur de verbes
            if mot.morph.get("VerbForm"):
                nb_verbes += 1
    
    return nb_mots_singulier, nb_mots_pluriel, nb_mots_masculin, nb_mots_feminin, nb_pronom, nb_verbes



#Pour afficher plusieurs graph en fonction des attributs quon veut
def afficher_attributs_graphes(auteurs,ensemble_mot_moyen, attributs, valeurs):
    nb_attributs = len(attributs)
    nb_auteurs = len(auteurs)
    nb_colonnes = 2
    nb_ligne  = (nb_attributs  // nb_colonnes) +1

    couleurs = ['red', 'blue', 'green', 'orange', 'purple', 'pink']


    fig, axes = plt.subplots(nb_ligne, nb_colonnes, figsize=(12, 8))

    indices = list(range(nb_auteurs))

    #Nombre moyen de mots par auteur
    for i, auteur in enumerate(auteurs):
        axes[0, 0].bar(indices[i], ensemble_mot_moyen[i],color=couleurs[i], label=auteur)
    axes[0, 0].set_title('Nombre moyen de mots par auteur')
    axes[0, 0].set_xticks(indices)
    axes[0, 0].set_xticklabels(auteurs)

    # affichage des autres attributs
    indice_attribut = 0
    for i in range(nb_ligne - 1):
        for j in range(nb_colonnes):
                
            if indice_attribut < nb_attributs:
                attribut = attributs[indice_attribut]

                for k, auteur in enumerate(auteurs):
                    axes[i + 1, j].bar(k, valeurs[k][indice_attribut], color=couleurs[k], label=auteur)

                axes[i+ 1, j].set_ylabel('Nombre')
                axes[i+ 1, j].set_title(f"{attribut} par auteur")
                axes[i+ 1, j].set_xticks(indices)
                axes[i+ 1, j].set_xticklabels(auteurs)

                indice_attribut += 1

    plt.xlabel('Auteur/Autrice')
    plt.tight_layout()
    plt.show()




#-------------------------------------
#-------------------------------------
#Information sur le terminal 
print("Lors de ce test plusieurs informations seront données , d'abord sur le terminal, puis sur un graphique , enfin un XML sera crée cela amenera à la création du XSL et du HTML")
print("Il vous sera demandé d'entrer n'importe quelle touche pour avancer")
auteur1=input("\nMais avant ca quel est le nom du premier Auteur / Autrice ? : ")
auteur2=input("Maintenant quel est le nom du second Auteur / Autrice ? :")

nb_mot_frequent= int(input("Quel est le nombre de mots le plus fréquent que vous voulez voir ? : "))


#analyse des textes des auteurs 
liste_phrases_auteur1 = analyse_texte("texte_auteur1.txt")
liste_phrases_auteur2 = analyse_texte("texte_auteur2.txt")

#calcul des mots moyen
mots_moyens_auteur1 = nombre_mots_moyen_par_phrase(liste_phrases_auteur1)
mots_moyens_auteur2 = nombre_mots_moyen_par_phrase(liste_phrases_auteur2)
ensemble_mot_moyen = [mots_moyens_auteur1,mots_moyens_auteur2]

#les mots les plus fréquents
mot_plus_frequent_auteur1 = mots_frequents(liste_phrases_auteur1, nb_mot_frequent)
mot_plus_frequent_auteur2  = mots_frequents(liste_phrases_auteur2, nb_mot_frequent)


#Affichage du nombre de mot moyen par phrase
print("\nNombre de mots moyen par phrase :")
print(auteur1, " : ", mots_moyens_auteur1)
print(auteur2, " : ",mots_moyens_auteur2)


input("\nVeuillez entrer n'importe quoi pour pouvoir affichier la suite : ")


#Affichage des mots les plus fréquents 
print("\nMots les plus fréquents :")
print("\n",auteur1)
for mot, occurences in mot_plus_frequent_auteur1:
    print(f"{mot} -> {occurences} occurrences")

print("\n",auteur2)
for mot, occurences in mot_plus_frequent_auteur2:
    print(f"{mot} -> {occurences} occurrences")

input("\nVeuillez entrer n'importe quoi pour pouvoir affichier la suite : ")


#affichage du nombre des type de mot 
ensemble_auteur=[auteur1,auteur2]
ensemble_phrase = [liste_phrases_auteur1 , liste_phrases_auteur2]
attributs = ["Nombre de mots Singuliers", "Nombre de mots Pluriels", "Nombre de mots Masculin", "Nombre de mots Féminins", "Nombre de PRonoms", "Nombre de Verbes"]

valeurs = []

for i, phrases_auteur in enumerate(ensemble_phrase):
    print("\n",ensemble_auteur[i])
    
    nb_mots_singulier, nb_mots_pluriel, nb_mots_masculin, nb_mots_feminin, nb_pronom, nb_verbes = 0, 0, 0, 0, 0, 0
    nb_mots_singulier, nb_mots_pluriel, nb_mots_masculin, nb_mots_feminin, nb_pronom, nb_verbes = compteur_type_mot(phrases_auteur, nb_mots_singulier, nb_mots_pluriel, nb_mots_masculin, nb_mots_feminin, nb_pronom, nb_verbes)
    valeurs.append([nb_mots_singulier, nb_mots_pluriel, nb_mots_masculin, nb_mots_feminin, nb_pronom, nb_verbes])

    for attribut, valeur in zip(attributs, [nb_mots_singulier, nb_mots_pluriel, nb_mots_masculin, nb_mots_feminin, nb_pronom, nb_verbes]):
        print(f"{attribut}: {valeur}")



#Graphique avec mathplot
validation=input("\nVeuillez entrer n'importe quoi pour pouvoir afficher le GRAPHIQUE : ")


#Affichage des attributs et du graphique
#print(valeurs)
#print(attributs)
afficher_attributs_graphes(ensemble_auteur, ensemble_mot_moyen,attributs, valeurs)
