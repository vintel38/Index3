# Index3

Ce répertoire contient le code et les procédures pour le développement d'un index pour la qualité de vie dans les villes françaises sur des critères environnementaux en utilisant des techniques de télédétection (remote sensing). Alors que les villes françaises sont de plus en plus souvent soumises à des épisodes caniculaires en été ou à des inondations/glissements de terrain, planter des arbres et revégétaliser rapidement les agglomérations françaises apparaît aujourd'hui comme une solution de bon sens et abordable financièrement, socialement et écologiquement. Hors les chiffres manquent concernant de telles initiatives hormis des coups de communication des différents élus. 

![maps_gre](https://user-images.githubusercontent.com/48808006/110324653-8f7e7f80-8016-11eb-9f4d-85936d7c6a87.png) 

Vue satellite de Grenoble, image de CNES, Airbus, Maxar Technologies par l'intermédiaire de Google Maps 

Aussi, ce répertoire entend répondre à ce besoin de comptabilité des espaces végétalisés en zone urbaine. L'observation des sols par vues aériennes ou satellite est utilisé depuis des decennies pour évaluer l'évolution des sols. Associé à la puissance du Machine Learning qui peut maintenant traiter des volumes d'informations importants, il devient possible d'évaluer les caractéristiques de ces territoires sur de grandes surfaces. La procédure de ce répertoire est simple :

- se familairiser avec la manipulation d'image satellite 
- entraîner une IA pour évaluer la couverture d'un territoire par des arbres suffisamment développés
- développer un indice pour résumer rapidement les caractéristiques de couverture végétale d'un territoire 

A terme, un indicateur de qualité de vie dans les grandes villes devrait être développé avec la forme suivante :

 θ : ψ : ε 

où 

Symbole | Signification
--- | --- 
θ | représente le pourcentage de surface au sol visible recouvert par de la végétation en bonne santé, 
ψ | représente le pourcentage de surface au sol visible recouvert par des arbres adultes, 
ε | la quantité en équivalent carbone d'énergie consommée à l'intérieur de l'agglomération par habitant. 

## I) University of Colorado Boulder EarthLab

Après quelques recherches sur le net, le laboratoire [Earth Lab](https://www.earthdatascience.org/) de l'Université du Colorado Boulder a développé un package dans le langage de programmation Python nommé [Earthpy](https://earthpy.readthedocs.io/) pour faciliter le traitement de données de télédétection. Ainsi nous utiliserons ce package pour la manipulation des images de télédétection. Parmi ces notebooks, on retrouve de façon intéressante l'indicateur NDVI qui calcule à partir des images spectrales dans le rouge pour RGB et dans le proche infrarouge NIR un ratio qui caractérise la présence et la santé de la végétation au sol. Ce ratio sera employé dans le futur pour générer des masques afin de s'intéresser uniquement aux zones végétalisées sur une image hyperspectrale d'origine.  

Pour commencer, des notebooks sont disponibles pour démarrer dans ce langage avec des images du satellite Landsat8. Ils ont été traduits et implémentés en français:

- [Données Landsat](https://github.com/vintel38/Index3/blob/main/Landsat_CUBoulder.ipynb)
- [Ouvrir & Recadrer des données Landsat](https://github.com/vintel38/Index3/blob/main/Landsat_CUBoulder2.ipynb)
- [Nuages, Ombres et Masques](https://github.com/vintel38/Index3/blob/main/Landsat_CUBoulder3.ipynb)
- [Remplacer valeurs de cellules d'imagerie](https://github.com/vintel38/Index3/blob/main/Landsat_CUBoulder4.ipynb)
- [Landsat Exercices](https://github.com/vintel38/Index3/blob/main/Landsat_Exo.ipynb)
- [Indices Végétaux](https://github.com/vintel38/Index3/blob/main/VegIndex.ipynb)

## II) Recherche Bibliographique 

La recherche bibliographique s'avère utile pour mettre à jour les techniques de post-traitement des données de télédétection collectées. Les articles cités dans cette partie proviennent majoritairement de recherches Google avec les mots-clés : `detect tree in remote imaging` ou encore `tree segmentation in remote imaging`. En effet, avec un peu de connaissances en traitement de l'image par des systèmes intelligents, on s'aperçoit rapidement que la tâche demandée dans le contexte de cette étude est la segmentation qui va permettre d'associer le statut d'arbre à tous les pixels sur une carte qui auront l'aspect d'arbre. Cette technique est répandue dans le secteur de la télédétection et beaucoup de publication en témoignent. Cependant, la localisation des arbres sur une carte n'est souvent pas le seul objectif de ces travaux. En effet, les chercheurs souhaitent également caractériser la distribution et la nature des différents arbres en utilisant un pipeline qui commence par de la segmentation et finit par de la classification après un recalage du jeu de données sur les sommets d'arbres. D'autres études basent également leur travail sur le post-traitement de nuages de points assemblés avec des observations de type [ALS](https://www.sciencedirect.com/science/article/abs/pii/S0924271699000118) ou [LIDAR](https://en.wikipedia.org/wiki/Lidar) mais il est très incertain d'avoir accès à ce genre données pour les besoins de cette étude. Ainsi, un travail supplémentaire est nécessaire sur ces articles pour déterminer quels procédures sont intéressantes pour ce projet. 

- Maschler, J.; Atzberger, C.; Immitzer, M. Individual Tree Crown Segmentation and Classification of 13 Tree Species Using Airborne Hyperspectral Data. Remote Sens. 2018, 10, 1218. https://doi.org/10.3390/rs10081218
- McMahon CA. 2019. Remote sensing pipeline for tree segmentation and classification in a mixed softwood and hardwood system. PeerJ 6:e5837 DOI 10.7717/peerj.5837
- S N H Syed Hanapi et al 2019 IOP Conf. Ser.: Mater. Sci. Eng. 705 012024
- Nevalainen, O.; Honkavaara, E.; Tuominen, S.; Viljanen, N.; Hakala, T.; Yu, X.; Hyyppä, J.; Saari, H.; Pölönen, I.; Imai, N.N.; Tommaselli, A.M.G. Individual Tree Detection and Classification with UAV-Based Photogrammetric Point Clouds and Hyperspectral Imaging. Remote Sens. 2017, 9, 185. https://doi.org/10.3390/rs9030185
- Itakura, K.; Hosoi, F. Automatic Tree Detection from Three-Dimensional Images Reconstructed from 360° Spherical Camera Using YOLO v2. Remote Sens. 2020, 12, 988. https://doi.org/10.3390/rs12060988


## Reste à faire : 

- Trouver une plateforme pour télécharger des données de télédétection hautes résolutions sur les agglomérations françaises -> Done : Google Earth Engine 
- Importer ces images dans le framework earthpy si possible
- Assimiler les techniques de télédétection avec une recherche bibliographique -> In the process : des articles ont été trouvés mais nécessitent encore des éclaircissements sur le sujet 
- Entraîner l'IA à exécuter le repérage des arbres
- Automatiser le tout avec l'utilisation d'un API de téléchargement
- Finir le développement de l'Index en contactant l'ADEME pour le calcul des ressources absorbées en hydrocarbures et énergie polluantes
