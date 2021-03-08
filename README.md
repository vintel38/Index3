# Index3

Ce répertoire contient le code et les procédures pour le développement d'un index pour la qualité de vie dans les villes françaises sur des critères environnementaux en utilisant des techniques de télédétection (remote sensing). Alors que les villes françaises sont de plus en plus souvent soumises à des épisodes caniculaires en été ou à des inondations/glissements de terrain, planter des arbres et revégétaliser rapidement les agglomérations françaises apparaît aujourd'hui comme une solution de bon sens et abordable financièrement, socialement et écologiquement. Hors les chiffres manquent concernant de telles initiatives hormis des coups de communication des différents élus. 

Aussi, ce répertoire entend répondre à ce besoin de comptabilité des espaces végétalisés en zone urbaine. L'observation des sols par vues aériennes ou satellite est utilisé depuis des decennies pour évaluer l'évolution des sols. Associé à la puissance du Machine Learning qui peut maintenant traiter des volumes d'informations gigantesques, il devient possible d'évaluer les caractéristiques de ces territoires sur de grandes surfaces. La procédure de ce répertoire est simple :

- se familairiser avec la manipulation d'image satellite 
- entraîner une IA pour évaluer la couverture d'un territoire par des arbres suffisamment développés
- développer un indice pour résumer rapidement les caractéristiques de couverture végétale d'un territoire 

A terme, un indicateur de qualité de vie dans les grandes villes devrait être développé avec la forme suivante 

$$ \Psi : \Omega : \epsilon$$ où $\Psi$ représente le pourcentage de surface au sol visible recouvert par de la végétation (toute confondue : arbre, arbuste, pelouse), $\Omega$ représente le pourcentage de surface au sol visible recouvert par des arbres adultes, $\epsilon$ la quantité en équivalent carbone d'énergie menant à des émissions polluantes à l'intérieur de la ville durant son utilisation par habitant de l'agglomération. 

Après quelques recherches sur le net, le laboratoire [Earth Lab](https://www.earthdatascience.org/) de l'Université du Colorado Boulder a développé un package dans le langage de programmation Python nommé [Earthpy](https://earthpy.readthedocs.io/) pour faciliter le traitement de données de télédétection. Ainsi nous utiliserons ce package pour la manipulation des images de télédétection.   

Pour commencer, des notebooks sont disponibles pour démarrer dans ce langage avec des images du satellite Landsat8. Ils ont été traduits et implémentés en français:

- [Données Landsat](https://github.com/vintel38/Index3/blob/main/Landsat_CUBoulder.ipynb)
- [Ouvrir & Recadrer des données Landsat](https://github.com/vintel38/Index3/blob/main/Landsat_CUBoulder2.ipynb)
- [Nuages, Ombres et Masques](https://github.com/vintel38/Index3/blob/main/Landsat_CUBoulder3.ipynb)
- [Remplacer valeurs de cellules d'imagerie](https://github.com/vintel38/Index3/blob/main/Landsat_CUBoulder4.ipynb)
- [Landsat Exercices](https://github.com/vintel38/Index3/blob/main/Landsat_Exo.ipynb)
- [Indices Végétaux](https://github.com/vintel38/Index3/blob/main/VegIndex.ipynb)

Reste à faire : 

- Trouver une plateforme pour télécharger des données de télédétection hautes résolutions sur les agglomérations françaises 
- Importer ces images dans le framework earthpy si possible
- Assimiler les techniques de télédétection avec une recherche bibliographique
- Entraîner l'IA à exécuter le repérage des arbres
- Automatiser le tout avec l'utilisation d'un API de téléchargement
- Finir le développement de l'Index en contactant l'ADEME pour le calcul des ressources absorbées en hydrocarbures et énergie polluantes