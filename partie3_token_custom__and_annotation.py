import spacy

nlp = spacy.load("fr_core_news_sm")

with open("conte.txt", "r", encoding="utf-8") as fichier_analyse:
    texte_analyse = fichier_analyse.read()

doc = nlp(texte_analyse)



with open("output_partie3.xml", "w", encoding="utf-8") as fichier_xml:
    fichier_xml.write('<?xml version="1.0" encoding="utf-8"?> \n')
    fichier_xml.write('<?xml-stylesheet type="text/xsl" href="output_partie3.xsl"?>\n')
    fichier_xml.write('<text>\n')
    
    for i, phrase in enumerate(doc.sents):

        fichier_xml.write(f'<sentence id="{i + 1}">\n')

        #un token pour les # car la methode utilisé est deja compétente
        mot_fusionner = "" 
        for j, mot in enumerate (phrase):

            #print(mot)
            #print(mot.morph)
            if mot.text.startswith("#"):
                mot_fusionner += mot.text

            else :
                if mot_fusionner != "":
                    fichier_xml.write(f'   <mot id="{j + 1}">{mot_fusionner}{mot.text}</mot>\n')
                    mot_fusionner= ""
                

                    #mot.morph.get("Gender")
                    #mot.morph.get("Number")
                    #mot.morph.get("Tense")
                    #mot.morph.get("Tense")
                    #mot.morph.get("VerbForm")
                
                #Ici on rccuperer les annotations afin de les afficher plus tard
                else:
                    fichier_xml.write(f'   <mot id="{j + 1}" text="{mot.text}" ')
                    if mot.morph.get("Gender"):
                        fichier_xml.write(f'Gender="{mot.morph.get("Gender")[0]}" ')
                    if mot.morph.get("Number"):
                        fichier_xml.write(f'Number="{mot.morph.get("Number")[0]}" ')
                    if mot.morph.get("Tense"):
                        fichier_xml.write(f'Tense="{mot.morph.get("Tense")[0]}" ')
                    if mot.morph.get("PronType"):
                        fichier_xml.write(f'PronType="{mot.morph.get("PronType")[0]}" ')
                    if mot.morph.get("VerbForm"):
                        fichier_xml.write(f'VerbForm="{mot.morph.get("VerbForm")[0]}" ')
                    
                    fichier_xml.write(f'>{mot.text}</mot>\n')


        fichier_xml.write(f'</sentence>\n')
    
    fichier_xml.write('</text>\n')