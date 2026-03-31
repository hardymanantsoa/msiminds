Examen ML // Nom du groupe : MSI MINDS

Membre du groupe :

RAKOTONIAINA Mbolatiana Joëllah ESIIA 4 N°13

RAVELOMANANTSOA Hardy Christel ESIIA 4 N°14

RAKOTONARIVO Jonah Harivelona ESIIA 4 N°06

RAKOTOARISOA Heriniaina Steve ESIIA 4 N°15

RAVELONJATOVOARIJAONA Zo Noary Fitahiana ESIIA 4 N°29

ANDRIAMASY Marc Athanase ESIIA 4 N°28

FANOMEZANTSOA Edilson Jean Taylor ESIIA 4 N°40

Q1 — Analyse des CoefficientsCoefficients les plus élevés : Pour le modèle x_wins, les coefficients les plus élevés en valeur absolue se trouvent généralement sur les colonnes correspondant à l'occupation de la case centrale ( c 4 x ) et des quatre coins ( c 0 x , c 2 x , c 6 x , c 8 x ). Pour le modèle is_draw, les coefficients élevés marquent souvent les positions de blocage où les pions X et O sont entremêlés.Influence de la case centrale : La case centrale ( c 4 x ) est mathématiquement la plus influente car elle appartient à 4 lignes de victoire possibles (horizontale, verticale et deux diagonales), contrairement aux bords qui n'en ont que 2.Cohérence stratégique : Cela est parfaitement cohérent avec la stratégie humaine : prendre le centre dès le premier coup est la règle de base pour maximiser ses chances de victoire ou forcer un nul.

Q2 — Déséquilibre des ClassesÉtat du Dataset : Le dataset de Morpion est naturellement déséquilibré. Le nombre d'états menant à une victoire de X (x_wins = 1) est généralement supérieur au nombre d'états menant à un match nul (is_draw = 1), car le jeu parfait entre deux experts finit toujours en nul, mais le dataset explore toutes les branches, y compris les erreurs.Métrique privilégiée : En raison de ce déséquilibre, l'Accuracy est trompeuse. Nous privilégions le F1-Score ou l'AUC (Area Under the Curve). Le F1-Score est crucial ici car il combine la précision et le rappel, assurant que l'IA ne se contente pas de prédire "victoire" par défaut parce que c'est la classe majoritaire.

Q3 — Comparaison des deux ModèlesMeilleur score : Le classificateur x_wins obtient généralement un meilleur score que is_draw.Complexité d'apprentissage : Le modèle is_draw est plus difficile à apprendre car un match nul est le résultat d'une série de coups précis de "non-victoire" des deux côtés. C'est un concept plus subtil que la victoire directe, qui repose sur des alignements géométriques simples que la Régression Logistique capture facilement.Erreurs types : Les modèles se trompent le plus souvent sur les positions de "fin de partie" où un seul coup change radicalement l'issue (pièges à double menace), car la régression traite les cases de manière trop indépendante.

Q4 — Mode HybrideDifférence de comportement : Le mode Hybride est nettement plus robuste que le mode IA-ML pur. Là où l'IA-ML peut faire une erreur de lecture sur un état spécifique, l'Hybride utilise le Minimax pour "voir" les conséquences immédiates à profondeur 3 avant de consulter le modèle ML.Évitement des pièges : Le joueur hybride évite mieux les pièges tactiques immédiats (comme une fourchette) car le calcul algorithmique sécurise les coups prochains, tandis que le modèle ML fournit une évaluation globale de la qualité de la position finale. Qualitativement, l'IA Hybride semble avoir une "vision de jeu" à long terme tout en restant tactiquement prudente

lien video: https://drive.google.com/file/d/1xBBa0hWgoKUeaoq--kfJP8TGc047hjbJ/view?usp=sharing