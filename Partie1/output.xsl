<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" omit-xml-declaration="yes" indent="yes"/>
  
  <xsl:template match="/analyse">
    <html>
        <head>
            <style>
                body{
                    font-family: 'Roboto', sans-serif;
                }
                .groupe {
                    display: flex;
                    flex-direction: row;
                    gap: 20px;
                }
                .colonne {
                    flex: 1;
                }
                .colonne:nth-child(even) {
                    background-color: #f2f2f2; 
                }
                .colonne:nth-child(odd) {
                    background-color: #e6f7ff; 
                }
                .resultat:hover {
                    background-color: yellow; 
                }
                h1{
                    text-align: center;
                    background-color: #4650D6;
                    margin-bottom: 0;
                    border-top-right-radius: 5px;
                    border-top-left-radius: 5px;
                }
                h2{
                    text-align: center;
                }
                
                .h2-groupe {
                    display: flex;
                    flex-direction: row;
                    justify-content: space-between;
                    gap: 20px;
                    position: relative;
                }
                .h2-center {
                    text-align: center;
                    margin-top: 0;
                    padding: 10px;
                    border-radius: 5px;
                    color: white;
                    position: relative; 
                    z-index: 1; 
                }

                .h2-center.vs {
                    background-color: white;
                    color: black;
                    border-radius: 50%;
                    width: 30px;
                    height: 30px;
                    display: flex;
                    position: absolute; 
                    left: 50%;
                    top: 50%;
                    transform: translate(-50%, -50%); 
                    z-index: 2;
                }
            

                .h2-gauche, 
                .h2-droite {
                    position: absolute; 
                    width: 50%; 
                    height: 100%;
                }

                .h2-gauche {
                    background-color: #56C0DC;
                    left: 0;
                    border-bottom-left-radius:5px;
                }

                .h2-droite {
                    background-color: #8F9CF7;
                    right: 0;
                    border-bottom-right-radius:5px;
                }
            </style>
        </head>
        <body>
            <h1>Comparaison des méthodes de découpage</h1>
            <div class="h2-groupe">
                <div class="h2-gauche"></div> 
                <h2 class="h2-center">
                    <xsl:value-of select="'A base de règle (regex) : '"/>
                    <xsl:value-of select="./text/id_max"/>

                </h2>
                <h2 class="h2-center vs">VS</h2>
                <div class="h2-droite"></div> 
                <h2 class="h2-center">
                    <xsl:value-of select="'Sentencizer: '"/>
                    <xsl:value-of select="./text_methode_sentencizer/id_max"/>
                </h2>
            </div>

            <div class="groupe">
            
                <div class="colonne">
                    <xsl:apply-templates select="./text/sent"/>
                </div>

                <div class="colonne">
                    <xsl:apply-templates select="./text_methode_sentencizer/sent"/>
                </div>
            </div>
      </body>
    </html>
  </xsl:template>






  <xsl:template match="sent">
    <p class="resultat">
        <xsl:value-of select="@id"/> 
        <xsl:text>: </xsl:text>
        <xsl:value-of select="."/>
    </p>
  </xsl:template>

</xsl:stylesheet>
