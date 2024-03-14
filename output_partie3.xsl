<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #eeee;
                    }
                    h1{
                        text-align: center;
                        color: #eeee;
                        background-color: #4650D6;
                        padding:10px;
                        border-top-right-radius : 5px;
                        border-top-left-radius : 5px;
                        margin: 0px;
                    }
                    h3{
                        text-align: center;
                        color: #eeee;
                        background-color: purple;
                        border-bottom-right-radius : 5px;
                        border-bottom-left-radius : 5px;
                        margin: 0px;
                    }
                    .paire {
                        background-color: lightblue;
                    }
                    .impaire {
                        background-color: lightgreen;
                    }
                    .mot:hover {
                        background-color: yellow; 
                    }

                    .masculin {
                        color: blue;
                    }
                    .feminin {
                        color: red;
                    }
                    .pluriel {
                        background-color: orange;
                    }
                    .singulier {
                        background-color: lightgrey;
                    }
                    .article {
                        text-decoration: underline;
                        text-decoration-color: pink;
                        text-decoration-thickness: 2px; 
                    }
                    .infinitif {
                        background-color: green;
                    }

                    .legende {
                        padding-left:20px;
                        border: 2px dashed black; 
                        padding-top: 10px; 
                        padding-bottom: 10px;
                        padding-right: 20px;
                        margin-bottom: 30px;
                        width: fit-content;
                        
                    }
                    .legende p {
                        margin: 0; 
                    }
                </style>
            </head>
            <body>
                <h1>Tokeniseur Spacy Custom</h1>
                <h3>Modification du tokeniseur ajout de la gestion des "#" et apostrophes et autre </h3>
                <h3>Et attribution de couleur en fonction de l'Annotation morphosyntaxique </h3>
                
                <h2></h2>
                <div class="legende">
                    <p>Légendes :</p>

                    <p>-<span class="masculin">Masculin</span>: texte de couleur bleu</p>
                    <p>-<span class="feminin">Feminin</span>: texte de couleur rouge</p>
                    <p>-<span class="pluriel">Mot Pluriel</span>: fond de mot de couleur orange</p>
                    <p>-<span class="singulier">Mot Singulier</span>: fond de mot de couleur gris clair</p>
                    <p>-<span class="infinitif">Verbe à l'infinitif </span>: fond de mot de couleur verte</p>
                    <p>-<span class="article">Article</span>: mot souligné en rose</p>
                </div>
                <xsl:apply-templates select="//sentence"/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="sentence">
        <p>
            <xsl:apply-templates select="mot"/>
        </p>
    </xsl:template>

    <xsl:template match="mot">
    <xsl:variable name="classes">
        <xsl:if test="contains(@Gender, 'Masc')">masculin </xsl:if>
        <xsl:if test="contains(@Gender, 'Fem')">feminin </xsl:if>
        <xsl:if test="contains(@Number, 'Plur')">pluriel </xsl:if>
        <xsl:if test="contains(@Number, 'Sing')">singulier </xsl:if>
        <xsl:if test="contains(@PronType, 'Art')">article </xsl:if>
        <xsl:if test="contains(@VerbForm, 'Inf')">infinitif </xsl:if>
    </xsl:variable>
    <xsl:choose>
        <xsl:when test="$classes">
            <span class="mot {$classes}">
                <xsl:value-of select="."/>
            </span>
        </xsl:when>
        <xsl:otherwise>
            <span class="mot">
                <xsl:value-of select="."/>
            </span>
        </xsl:otherwise>
    </xsl:choose>
    <!--Espace entre les mots-->
    <xsl:text> </xsl:text>
</xsl:template>
</xsl:stylesheet>
