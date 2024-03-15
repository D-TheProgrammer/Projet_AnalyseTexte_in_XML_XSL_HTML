# Projet_AnalyseTexte_in_XML_XSL_HTML
[French] Projet d'analyse de texte et de tokenisation  
[English] Project Text Analysis and Tokenization Project (First it will be the French README then the English README After)  

#### SOMMAIRE / SUMMARY
- [Présentation en francais / Presentation in French](#presentation-en-francais)
- [Présentation en anglais / Presentation in English](#english-presentation)
- [Tutoriel dans les deux langues / Tutorial in both languages](#tutoriel--tutorial)


#### Test Online
> https://d-theprogrammer.github.io/Projet_AnalyseTexte_in_XML_XSL_HTML/


## [PRESENTATION EN FRANCAIS]
### 1.  <ins>[Information]</ins>

Projet réalisé par D-TheProgrammer

Ce projet mélange du code Python, XML, XSL voici la liste des fichiers qui se trouvent dans ce répertoire. 

- Il y a pour les fichier python (je vais les décrire plus tard) :
  -  partie1_regex_phrase.py  
  -  partie1_sentencizer_phrase.py 
  -  partie2_decoupeMot.py
  -  partie3_token_custom__and_annotation.py
  -  partie4_visualisation.py

- Il y a pour les fichier .txt :
	-  README.txt (document que vous lisez)
	-  conte.txt
	-  input.txt (il s'agit d'un copier coller de conte.txt mais tout autre texte fonctionne)
	-  input_partie2.txt (contient le texte de la partie 2)
	-  texte_auteur1.txt (pour le test de la partie 4)
	-  texte_auteur2.txt (pour le test de la partie 4)


- Il y a pour les fichier .xml:  
	-  output.xml (qui contient le resultat sous forme xml de `partie1_regex_phrase.py`
		et `partie1_sentencizer_phrase.py` donc 2 DOCUMENTS )

	-  output_partie2.xml (contient les résultat de partie2_decoupeMot.py)
	-  output_partie3.xml ( contient les résultat de partie3_token_custom__and_annotation.py)
  
- Il y a pour les fichier .xsl:  
	- output.xsl (qui transforme output.xml)
	- output_partie2.xsl ( qui transforme  output_partie2.xml)
	- output_partie3.xsl (qui transforme output_partie3.xml)


### 2.  <ins>[Utilisation et explication de la realisation]</ins>
#### PARTIE 1 : Comparaison des méthodes de découpage

- Il faut savoir que dans le dossier  **Partie 1** j'ai créé un code .xml en 2 parties qui sera **généré à partir de 2 codes Python**. Ainsi, pour obtenir `output.xml`, il faudra d'abord lancer simplement `partie1_regex_phrase.py` , qui va écrire (dans le sens "write") des informations et qui va donc supprimer pour remplacer par de nouvelles informations, puis lancer `partie1_sentencizer_phrase.py"`, qui lui va ajouter (dans le sens "add") à la fin du fichier `output.xml`. En faisant ça, vous aurez le fichier .xml complet (sinon il marchera pas)! Il suffira par la suite de générer le fichier HTML (qui est fourni malgré tout) avec la ligne de commande : 

> [!WARNING]
> D'abord faire :
> ```bash
> python3 partie1_regex_phrase.py
> ````
> puis faire 
> ```bash
> python3 partie1_sentencizer_phrase.py
> ````

> [!TIP]
> Avec cela vous obtiendrez le fichier .xml complet il faudra alors créer l'html à partir du .xsl et du .xml comme ceci :
> ```bash
> xsltproc output.xml output.xsl -o output.html
> ````

Ce fichier HTML permet de voir les phrases générées via un surlignement.


#### PARTIE 2 : Découpe de mots à base de règles  

- La Partie 2 qui utilise `partie2_decoupeMot.py` ,fait une découpe de mots à partir d'une tokenisation , ce fichier python fait une sortie vers un document .xml `output_partie2.xml`. Fichier qui se transformera avec son fichier xsl correspondant en .html 

> [!WARNING]
> D'abord faire :
> ```bash
> python3 partie2_decoupeMot.py
> ````

> [!TIP]
> Avec cela vous obtiendrez le fichier .xml complet il faudra alors créer l'html à partir du .xsl et du .xml comme ceci :
> ```bash
> xsltproc output_partie2.xml output_partie2.xsl -o output_partie2.html
> ````


#### PARTIE 3 : Annotation de mots d'une phrase en fonction de leur type 
- Utilise le code `partie3_token_custom__and_annotation.py` pour produire le .xml nommé `output_partie3.xml` et l'xsl et html 

> [!WARNING]
> D'abord faire :
> ```bash
> python3 partie3_token_custom__and_annotation.py
> ````

> [!TIP]
> Avec cela vous obtiendrez le fichier .xml complet il faudra alors créer l'html à partir du .xsl et du .xml comme ceci :
> ```bash
> xsltproc output_partie3.xml output_partie3.xsl -o index.html
> ````


#### PARTIE 4 : Visualisation 

- Cette partie utilise la librairie  mathplotlib pour pouvoir afficher des graphes. Ainsi le programme python `partie4_visualisation.py` compare les deux textes contenu dans `texte_auteur1.txt` et `texte_auteur2.txt` et affiche des resultats sur le terminal après avoir suivi les indications du terminal plusieurs graphes s'afficheront . 

> [!NOTE]
> Pour installer matplotlib :
> ```bash
> pip install matplotlib
> ```

> [!WARNING]
> D'abord faire :
> ```bash
> python3 partie4_visualisation.py
> ````

> [!TIP]
> Pour effectuer d'autre test il suffit de modifier les fichiers .txt en modifiant les texte

___
## [ENGLSIH PRESENTATION]
### 1. <ins>[Information]</ins>

Project created by D-TheProgrammer

This project mixes Python, XML, XSL code here is the list of files located in this directory.

- There are python files (I will describe them later):
  -  partie1_regex_phrase.py  
  -  partie1_sentencizer_phrase.py 
  -  partie2_decoupeMot.py
  -  partie3_token_custom__and_annotation.py
  -  partie4_visualisation.py

- There are for .txt files:
  - README.txt (document you are reading)
  - conte.txt
  - input.txt (this is a copy and paste of conte.txt but any other text works)
  - input_partie2.txt (contains the text of part 2)
  - texte_auteur1.txt (for the test of part 4)
  - texte_auteur2.txt (for the test of part 4)

- There are for .xml files:
  - output.xml (which contains the result in xml form of `part1_regex_phrase.py`
  and `part1_sentencizer_phrase.py` so 2 DOCUMENTS)
  
  - output_partie2.xml (contains the results of part2_decoupeMot.py)
  - output_partie3.xml (contains the results of part3_token_custom__and_annotation.py)
    
- There is for .xsl files:
  - output.xsl (which transforms output.xml)
  - output_partie2.xsl (which transforms output_partie2.xml)
  - output_partie3.xsl (which transforms output_partie3.xml)


### 2. <ins>[Use and explanation of the achievement]</ins>
#### PART 1: Comparison of slicing methods

- You should know that in the **Part 1** folder I created an .xml code in 2 parts which will be **generated from 2 Python codes**. Thus, to obtain `output.xml`, it will first be necessary to simply launch `partie1_regex_phrase.py`, which will write (in the "write" sense) information and which will therefore delete to replace with new information, then launch `partie1_sentencizer_phrase.py`, which will add (in the "add" sense) at the end of the `output.xml` file. By doing this, you will have the complete .xml file (otherwise it will not work)! It will be enough then generate the HTML file (which is provided regardless) with the command line:

> [!WARNING]
> First do:
> ```bash
> python3 partie1_regex_phrase.py
> ````
> then do
> ```bash
> python3 partie1_sentencizer_phrase.py
> ````

> [!TIP]
> With this you will obtain the complete .xml file you will then have to create the html from the .xsl and the .xml like this:
> ```bash
> xsltproc output.xml output.xsl -o output.html
> ````

This HTML file allows you to see the sentences generated via highlighting.


#### PART 2: Rule-based word splitting

- Part 2 which uses `partie2_decoupeMot.py`, cuts words from a tokenization, this python file outputs to an .xml document `output_partie2.xml`. File which will be transformed with its corresponding xsl file into .html

> [!WARNING]
> First do:
> ```bash
> python3 partie2_decoupeMot.py
> ````

> [!TIP]
> With this you will obtain the complete .xml file you will then have to create the html from the .xsl and the .xml like this:
> ```bash
> xsltproc output_partie2.xml output_partie2.xsl -o output_partie2.html
> ````


#### PART 3: Annotating words in a sentence based on their type
- Uses the `partie3_token_custom__and_annotation.py` code to produce the .xml named `output_partie3.xml` and the xsl and html

> [!WARNING]
> First do:
> ```bash
> python3 partie3_token_custom__and_annotation.py
> ````

> [!TIP]
> With this you will obtain the complete .xml file you will then have to create the html from the .xsl and the .xml like this:
> ```bash
> xsltproc output_partie3.xml output_partie3.xsl -o index.html
> ````


#### PART 4: Visualization

- This part uses the mathplotlib library to be able to display graphs. Thus the python program `partie4_visualisation.py` compares the two texts contained in `texte_auteur1.txt` and `texte_auteur2.txt` and displays results on the terminal after having followed the instructions of the terminal several graphs will be displayed.

> [!NOTE]
> To install matplotlib:
> ```bash
> pip install matplotlib
> ```

> [!WARNING]
> First do:
> ```bash
> python3 partie4_visualisation.py
> ````

> [!TIP]
> To carry out another test, simply modify the .txt files by modifying the text


## [Tutoriel / Tutorial]
#### Résultat de la Partie 1 (après avoir lancer le .py et créer l'HTML) / Result of Part 1 (after launching the .py and creating the HTML)

<div align="center">
  <img width="946" alt="image" src="https://github.com/D-TheProgrammer/Projet_AnalyseTexte_in_XML_XSL_HTML/assets/151149998/a22ec535-14bc-4c93-a5b9-b2fc9cfc3c7e">
</div>

#### Résultat de la Partie 2 (après avoir lancer le .py et créer l'HTML) / Result of Part 2 (after launching the .py and creating the HTML)
<div align="center">
  <img width="950" alt="image" src="https://github.com/D-TheProgrammer/Projet_AnalyseTexte_in_XML_XSL_HTML/assets/151149998/9625505d-c99d-4801-b4d0-2ed906a556dd">
</div>

#### Résultat de la Partie 3 (après avoir lancer le .py et créer l'HTML) / Result of Part 3 (after launching the .py and creating the HTML)
[FRANCAIS] Tokeniseur la découpe de mots est en meme temps annoter (en francais) et chaque mots possède une couleur afin de voir visuellement leur classe voici la légende :  
- Masculin: texte de couleur bleu  
- Feminin: texte de couleur rouge  
- Mot Pluriel: fond de mot de couleur orange  
- Mot Singulier: fond de mot de couleur gris clair  
- Verbe à l'infinitif : fond de mot de couleur verte  
- Article: mot souligné en rose  

[ENGLISH] Tokenizer: Word segmentation is annotated simultaneously (in French), and each word is colored to visually represent its class. Here is the legend:  
- Masculine: text in blue  
- Feminine: text in red  
- Plural word: word background in orange  
- Singular word: word background in light gray  
- Infinitive verb: word background in green  
- Article: word underlined in pink  
  
<div align="center">
  <img width="940" alt="image" src="https://github.com/D-TheProgrammer/Projet_AnalyseTexte_in_XML_XSL_HTML/assets/151149998/cd0062d5-26e9-4edc-ba43-bf2ddf1003da">
  <img width="941" alt="image" src="https://github.com/D-TheProgrammer/Projet_AnalyseTexte_in_XML_XSL_HTML/assets/151149998/fe47c6b2-94fd-4ab1-9b00-3da32a01f8d9">
</div>


#### Résultat de la Partie 4 (après avoir lancer le .py ) / Result of Part 4 (after launching the .py )
[FRANÇAIS] Dans la partie 4, le terminal fournit des informations. Tout d'abord, il était possible de nommer l'auteur ou l'autrice du texte 1 et du texte 2 (car il est possible de modifier les fichiers .txt qui seront analysés, ainsi, si on veut mettre le script d'un film, il est possible de le nommer).  
[ENGLISH] In part 4, the terminal provides information. First, it was possible to name the author of text 1 and text 2 (because it is possible to modify the .txt files that will be analyzed, so if you want to put a movie script, it is possible to name it).  

<div align="center">
  <img width="631" alt="image" src="https://github.com/D-TheProgrammer/Projet_AnalyseTexte_in_XML_XSL_HTML/assets/151149998/9a0bdbc2-d8e7-4675-bb2e-65281b93566d">
</div>

[FRANÇAIS] Après cela, le programme va calculer le nombre moyen de mots par phrase et afficher un certain nombre de mots les plus répandus en fonction de ce qu'a indiqué l'utilisateur.  
[ENGLISH] After that, the program will calculate the average number of words per sentence and display a certain number of the most common words based on what the user has indicated.  
<div align="center">
  <img width="187" alt="image" src="https://github.com/D-TheProgrammer/Projet_AnalyseTexte_in_XML_XSL_HTML/assets/151149998/c86586d5-0659-45f7-8aa9-7eb2ddd4a56c">
</div>

[FRANÇAIS] Ensuite, le programme affiche les différents types de mots et leur occurrence.    
[ENGLISH] Then, the program displays the different types of words and their occurrences.  

<div align="center">
  <img width="220" alt="image" src="https://github.com/D-TheProgrammer/Projet_AnalyseTexte_in_XML_XSL_HTML/assets/151149998/96102142-156c-40ec-ac22-cae768bd5320">
</div>

[FRANÇAIS] Enfin, voici l'ensemble des analyses affichées via un graphique matplotlib.  
[ENGLISH] Finally, here is the set of analyses displayed via a matplotlib graph.  

<div align="center">
  <img width="574" alt="image" src="https://github.com/D-TheProgrammer/Projet_AnalyseTexte_in_XML_XSL_HTML/assets/151149998/dc68a0ba-5877-46dd-9f3f-b835d4ffa85b">
</div>

