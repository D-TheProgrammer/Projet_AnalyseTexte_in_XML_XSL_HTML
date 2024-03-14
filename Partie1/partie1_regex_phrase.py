import re

#on charge et ouvre le texte 
fichier_analyse = open("input.txt", "r", encoding="utf-8")
texte_analyse = fichier_analyse.read()

#on cree les regles
liste_phrases = re.findall("[A-Z\"«»“”].*?[.?!]+", texte_analyse, flags=re.DOTALL)

# print(liste_phrases[0])

#on ecrit les phrase dans le fichier output.xml
with open("output.xml", "w", encoding="utf-8") as fichier_xml:
    fichier_xml.write('<?xml version="1.0" encoding="utf-8"?> \n')
    fichier_xml.write('<?xml-stylesheet type="text/xsl" href="output.xsl"?>\n')
    fichier_xml.write('<analyse>\n')
    fichier_xml.write('<text>\n')
    
    for i, phrase in enumerate(liste_phrases):
        fichier_xml.write(f'<sent id="{i + 1}">{phrase}</sent>\n')
        imax=i
    fichier_xml.write(f'<id_max>{i+1}</id_max>\n')
    fichier_xml.write('</text>\n')
