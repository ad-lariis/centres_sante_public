#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:09:38 2024

@author: alexandre
"""



def main():

    apl_txt = '''*lecture: compte tenu de la structure par âge de la population,
    les habitants de Nice ont accès, en moyenne, à 3,8 consultations ou visites de
    médecins généralistes libéraux de moins de 65 ans en 2022.'''
    
    zonage_txt = '''**ce zonage identifie les zones où l’offre de soins est considérée
    comme insuffisante et où l’accès aux soins est plus difficile et donne accès aux
    médecins qui souhaitent exercer au sein de ces zones géographiques à des aides à l’installation.
    '''
    
    legende = f"""
    <div style="position: fixed; bottom: 50px; right: 10px; width: 300px;
                z-index: 1000; background-color: rgba(255, 255, 255, 0.8);
                border-radius: 5px; padding: 10px; font-size: 10px; line-height: 1.5; word-wrap: break-word;">
        
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin-bottom: 2px">{apl_txt}</li>
            <li style="margin-bottom: 2px">{zonage_txt}</li>
        </ul>
        
        
        <div id="legend_content" style="display: none; position: relative; bottom: 10px;">
            <p style="margin-top: 20px; "><b>Sources:</b></p>
            <ul>
                <li>APL: <i>Drees</i></li>
                <li>Zones en offre de soins insuffisante: <i>ARS PACA 02/2022</i></li>
                <li>Centres et maisons de santé: <i>FINESS 2022</i></li>
            </ul>
        </div>
        
        <button onclick="toggleLegend()" style="position: absolute; bottom: 2px; right: 10px">Sources</button>
        
    </div>
    
    
    <script>
    var isSourceVisible = false;
        function toggleLegend() {{
            var legendContent = document.getElementById("legend_content");
            var button = document.querySelector("button");
            
            if (!isSourceVisible) {{
                legendContent.style.display = "block";
                button.textContent = "Masquer les sources";
            }} else {{
                legendContent.style.display = "none";
                button.textContent = "Sources"
            }}
            
            isSourceVisible = !isSourceVisible;
        }}
                      
    </script>
    """

    return(legende)

