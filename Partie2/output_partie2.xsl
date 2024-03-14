<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/analyse">
        <html>
             <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #eeee;
                    }
                    h1{
                        text-align: center;
                        background-color: #4650D6;
                        padding:10px;
                        border-radius : 5px;
                    }
                    .paire,
                    .impaire {
                        border: 1px solid #000;
                        border-radius: 7px;
                        padding: 5px;
                        margin: 5px;
                        display: inline-block;
                    }
                    .paire {
                        background-color: #f2f2f2;
                    }
                    .impaire {
                        background-color: #e6f7ff;
                    }
                    .paire:hover,
                    .impaire:hover {
                        background-color: yellow; 
                    }
                </style>
        </head>
        <body>
            <h1>Découpe de mots à base de règles</h1>
            <xsl:apply-templates select="//sent"/>
        </body>
    </html>
</xsl:template>


<xsl:template match="sent">
    <xsl:variable name="paire" select="@id mod 2 = 0"/>
    <div class="mot">
        <xsl:attribute name="class">
            <xsl:if test="$paire">paire</xsl:if>
            <xsl:if test="not($paire)">impaire</xsl:if>
        </xsl:attribute>
        <xsl:value-of select="@id"/>
        <xsl:text> : </xsl:text>
        <xsl:value-of select="."/>
    </div>
    </xsl:template>

</xsl:stylesheet>
