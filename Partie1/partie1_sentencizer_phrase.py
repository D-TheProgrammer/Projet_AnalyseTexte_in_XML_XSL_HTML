import spacy
from spacy.lang.fr import French

#on charge et ouvre le texte 
with open("input.txt", "r", encoding="utf-8") as fichier_analyse:
    texte_analyse = fichier_analyse.read()

#Utilisation de sencizer
module = French()
sentencizer = module.add_pipe('sentencizer')

#Analyse du texte
texte_analyser = module(texte_analyse)

#on ecrit les phrase dans le fichier output.xml
#On utilse sents pour avoir les phrases , on utilie "a" pour ajouter a la fin du fichier
with open("output.xml", "a", encoding="utf-8") as fichier_phrases:
    fichier_phrases.write('\n\n')
    fichier_phrases.write('<text_methode_sentencizer>\n')
    
    for i, phrase in enumerate(texte_analyser.sents):
        fichier_phrases.write(f'<sent id="{i + 1}">{phrase}</sent>\n')
        imax=i
        
    fichier_phrases.write(f'<id_max>{i+1}</id_max>\n')
    fichier_phrases.write('</text_methode_sentencizer>\n')
    fichier_phrases.write('</analyse>\n')
