# Index3 : Développement d'un indicateur pour la qualité de vie urbaine (télédétection)

Ce répertoire contient le code et les procédures pour le développement d'un index pour la qualité de vie dans les villes françaises sur des critères environnementaux en utilisant des techniques de télédétection (remote sensing). Alors que les villes françaises sont de plus en plus souvent soumises à des épisodes caniculaires en été, des épisodes de pollution intenses ou bien encore à des inondations/glissements de terrain, planter des arbres et revégétaliser rapidement les agglomérations françaises apparaît aujourd'hui comme une solution de bon sens et abordable financièrement, socialement et écologiquement. Hors les chiffres manquent concernant de telles initiatives hormis des coups de communication des différents élus. 

![maps_gre](https://github.com/vintel38/Index3/blob/main/images/maps_grenoble.PNG) 

Vue satellite de Grenoble, image de CNES, Airbus, Maxar Technologies par l'intermédiaire de Google Maps 

Aussi, ce répertoire entend répondre à ce besoin de comptabilité des espaces végétalisés en zone urbaine. L'observation des sols par vues aériennes ou satellite est utilisé depuis des decennies pour évaluer l'évolution des sols à grandes échelles. Les progrès techniques effectués sur les capteurs embarqués et la mise à disposition grand public des données permet aujourd'hui de nouvelles approches. Associé à la puissance du Machine Learning qui peut maintenant traiter des volumes d'informations conséquents, il devient possible d'évaluer les caractéristiques de ces territoires sur de grandes surfaces. A terme, un indicateur de qualité de vie dans les grandes villes devrait être développé avec la forme suivante :

 θ : ψ : ε 

où 

Symbole | Signification
--- | --- 
θ | le pourcentage de surface au sol visible recouvert par de la végétation en bonne santé, 
ψ | le pourcentage de surface au sol visible recouvert par des arbres adultes, 
ε | la quantité en équivalent carbone d'énergie consommée à l'intérieur de l'agglomération par habitant. 

La procédure de ce répertoire est linéaire : on commencera par se familiariser avec la manipulation d'image satellite en Python (1.), puis on importera des données réelles et d'actualité sur les zones qui seraient intéressantes (2.). Une recherche bibliographique (3.) sur l'état de l'art permettra de lister avant de choisir les techniques les plus adaptées pour les besoins spécifiés. Enfin, un code développé spécialement (4.) permettra d'établir un classement des villes en fonction de leur degré de végétation.

## Table des matières
1. University of Colorado Boulder EarthLab
2. QGIS with Earth Engine Plugin
3. Recherche Bibliographique
4. Index3 architecture


## 1. University of Colorado Boulder EarthLab

Après quelques recherches sur le net, le laboratoire [Earth Lab](https://www.earthdatascience.org/) de l'Université du Colorado Boulder a développé un package dans le langage de programmation Python nommé [Earthpy](https://earthpy.readthedocs.io/) pour faciliter le traitement de données de télédétection. Ainsi on utilisera ce package pour la manipulation des images de télédétection. Parmi ces notebooks, on retrouve de façon intéressante l'indicateur NDVI qui calcule à partir des images spectrales dans le rouge pour RGB et dans le proche infrarouge NIR un ratio qui caractérise la présence et la santé de la végétation au sol. Ce ratio sera employé dans le futur pour générer des masques afin de s'intéresser uniquement aux zones végétalisées sur une image hyperspectrale d'origine. Largement utilisé dans le secteur de la télédétection, ce ratio permet de caractériser précisément l'état de la végétation sans pour autant se limiter à un simple seuillage sur la composante verte de l'image : un stade de foot synthétique serait capable de berner le seuillage avec sa couleur apparente.   

Pour commencer, des notebooks sont disponibles pour démarrer dans ce langage avec des images du satellite Landsat8. Ils ont été traduits et implémentés en français:

- [Données Landsat](https://github.com/vintel38/Index3/blob/main/UCB_notebooks/Landsat_CUBoulder.ipynb)
- [Ouvrir & Recadrer des données Landsat](https://github.com/vintel38/Index3/blob/main/UCB_notebooks/Landsat_CUBoulder2.ipynb)
- [Nuages, Ombres et Masques](https://github.com/vintel38/Index3/blob/main/UCB_notebooks/Landsat_CUBoulder3.ipynb)
- [Remplacer valeurs de cellules d'imagerie](https://github.com/vintel38/Index3/blob/main/UCB_notebooks/Landsat_CUBoulder4.ipynb)
- [Landsat Exercices](https://github.com/vintel38/Index3/blob/main/UCB_notebooks/Landsat_Exo.ipynb)
- [Indices Végétaux](https://github.com/vintel38/Index3/blob/main/UCB_notebooks/VegIndex.ipynb)


## 2. QGIS with Earth Engine Plugin

Le problème général du Machine Learning s'applique également à ce projet. Comment rassembler assez de données pour entraîner et mettre au point une application telle qu'Index3 dans un domaine aussi discret que la télédétection ? Heureusement, un des géants d'Internet s'est attelé à la tâche : Google. Il propose avec son moteur de recherche dans le cloud [Google Earth Engine](https:,,earthengine.google.com,) de développer des applications à distance en utilisant à la fois les pétaflops de données qu'il détient, mais également la puissance de calcul de ses datacenters. La capture d'écran suivante présente une utilisation possible du [Code Editor](https:,,code.earthengine.google.com,) de la plateforme proposée dans les docs. Le script de la fenêtre centrale haute est compilé en ligne pour tracer l'indicateur NDVI sur la côte californienne en appliquant en masque au champ de valeurs pour deux images accolées.

![EEcode_editor](https://github.com/vintel38/Index3/blob/main/images/EEcode_editor.PNG)

Cependant, comme vous pouvez le voir dans la fenêtre script du Code Editor, Google Earth Engine utilise le langage JavaScript pour éditer le code à compiler. Pour garder une cohérence avec les autres projets, seul le langage Python sera utilisé dans ce projet. On utilisera donc une autre interface que le Code Editor pour bénéficier de la puissance logicielle de Google Earth Engine.

Il existe également des plateformes open-source pour faire de la télédétection directement sur son ordinateur personnel. C'est le cas de [QGIS](https:,,qgis.org,fr,site,) qui est un peu l'avatar gratuit du logiciel propriétaire ArcGIS. Ce logiciel est particulièrement intéressant comme il est codé en Python et possède un large panel de plug-in avec fort heureusement un plug-in Google Earth Engine. Ce plug-in va donc permettre de faire le pont entre les serveurs de Google pour y télécharger les données et le logiciel QGIS installé sur notre ordinateur. Dans la partie dédié aux codes du laboratoire EarthLab, on a utilisé abondamment la bibliothèque EarthPy pour effectuer des opérations de télédétection. Cependant, compte tenu de l'incroyable effort de développement de Google, on utilisera le package EarthEngine dans les futures lignes de code avec l'abréviation de package `ee`. Il existe quelque vidéo sur Youtube pour installer rapidement le plug-in sur votre logiciel QGIS mais le tout ne pose pas de problème particulier. Il suffit d'aller dans l'onglet `Extension` de QGIS, sélectionner `Installer,Gérer les extensions` puis sélectionner,installer dans la liste les plug-in `Google Earth Engine` et `Google Earth Engine Data Catalog`. Les exemples de la [documentation](https:,,developers.google.com,earth-engine,guides,getstarted) sont majoritairement en JavaScript comme c'est le langage par défaut de Google Earth Engine Code Editor. Cependant, il existe un [répertoire](https:,,github.com,giswqs,qgis-earthengine-examples) GitHub qui rassemble une grande quantité de code de base pour Earth Engine entièrement traduits en Python. Les premières compilations sur QGIS exploitant le plug-in sont des exemples de répertoire.


## 3. Recherche Bibliographique 

La recherche bibliographique s'avère utile pour mettre à jour les techniques de post-traitement des données de télédétection collectées. Les articles cités dans cette partie proviennent majoritairement de recherches Google avec les mots-clés : `detect tree in remote imaging` ou encore `tree segmentation in remote imaging`. En effet, avec un peu de connaissances en traitement de l'image par des systèmes intelligents, on s'aperçoit rapidement que la tâche demandée dans le contexte de cette étude est la segmentation qui va permettre d'associer le statut d'arbre à tous les pixels sur une carte qui auront l'aspect d'arbre. Cette technique est répandue dans le secteur de la télédétection et beaucoup de publication en témoignent. 

Cependant, la localisation des arbres sur une carte n'est souvent pas le seul objectif de ces travaux. En effet, les chercheurs souhaitent également caractériser la distribution et la nature des différents arbres en utilisant un pipeline qui commence par de la segmentation et finit par de la classification après un recalage du jeu de données sur les sommets d'arbres. D'autres études basent également leur travail sur le post-traitement de nuages de points assemblés avec des observations de type [ALS](https://www.sciencedirect.com/science/article/abs/pii/S0924271699000118) ou [LIDAR](https://en.wikipedia.org/wiki/Lidar) mais il est très incertain d'avoir accès à ce genre données pour les besoins de cette étude. Ainsi, un travail supplémentaire est nécessaire sur ces articles pour déterminer quels procédures sont intéressantes pour ce projet. La liste suivante recense l'ensemble des articles qui ont été considérés dans le cadre de cette recherche 

- Maschler, J.; Atzberger, C.; Immitzer, M. Individual Tree Crown Segmentation and Classification of 13 Tree Species Using Airborne Hyperspectral Data. Remote Sens. 2018, 10, 1218. https://doi.org/10.3390/rs10081218
- McMahon CA. 2019. Remote sensing pipeline for tree segmentation and classification in a mixed softwood and hardwood system. PeerJ 6:e5837 https://doi.org/10.7717/peerj.5837
- S N H Syed Hanapi et al 2019 IOP Conf. Ser.: Mater. Sci. Eng. 705 012024
- Nevalainen, O.; Honkavaara, E.; Tuominen, S.; Viljanen, N.; Hakala, T.; Yu, X.; Hyyppä, J.; Saari, H.; Pölönen, I.; Imai, N.N.; Tommaselli, A.M.G. Individual Tree Detection and Classification with UAV-Based Photogrammetric Point Clouds and Hyperspectral Imaging. Remote Sens. 2017, 9, 185. https://doi.org/10.3390/rs9030185
- Itakura, K.; Hosoi, F. Automatic Tree Detection from Three-Dimensional Images Reconstructed from 360° Spherical Camera Using YOLO v2. Remote Sens. 2020, 12, 988. https://doi.org/10.3390/rs12060988
- Chemura, A., et al. Determination of the age of oil palm from crown projection area detected from WorldView-2 multispectral
remote sensing data: The case of Ejisu-Juaben district, Ghana. ISPRS J. Photogram. Remote Sensing (2014), http://dx.doi.org/10.1016/j.isprsjprs.2014.07.013
- Z. Roslan, Z. Awang, M. N. Husen, R. Ismail and R. Hamzah, "Deep Learning for Tree Crown Detection In Tropical Forest," 2020 14th International Conference on Ubiquitous Information Management and Communication (IMCOM), Taichung, Taiwan, 2020, pp. 1-7, https://doi.org/10.1109/IMCOM48794.2020.9001817.

Le but ici n'est pas de passer en revue et d'analyser chaque article. Nous dirons seulement que  l'article de MacMahon se sert de l'image hyperspectrale uniquement pour créer un masque de végétation en utilisant l'indicateur NDVI pour ensuite continuer avec une segmentation sur le modèle CHM qui exploite des données d'altitude LIDAR. Syed fournit seulement une liste de toutes les techniques à disposition, aussi bien éprouvées que récentes. Nevalainen et al utilisent des nuages de points issus de vols de drone pour de la classification (pas vraiment ce que l'on souhaite faire donc). Itakura utilise des données hyperspectrales 3D de caméra 360° pour faire de la détection d'objet en utilisant Yolov2. Chemura et al utilisent un logiciel propriétaire pour effectuer la segmentation. Roslan et al utilise aussi la détection d'objet sur des images aériennes de plantation de palme ce qui mène à des résultats assez approximatifs pour le détourage de la couronne des arbres. Finalement, le seul papier qui nous intéresse est celui de Maschler et al.

Maschler et al cherchent des informations sur la composition de terres autrichiennes qui font partie d'un parc classé au patrimoine mondial de l'UNESCO. Dans son cas, la segmentation pour trouver la couronne des arbres peut être plus ou moins efficace selon la nature des arbres. Donc il est nécessaire d'effectuer deux segmentations où la première sert à grouper les arbres avec les mêmes caractéristiques puis appliquer la vraie segmentation pour détourer la couronne de chaque arbre, mais avec des paramètres différents pour chaque espèce. La première segmentation qui nous intéresse est réalisée sur de grandes images de vues aériennes ou satellite via l'algorithme LSMS (Large Scale Mean Shift). Cet algorithme est implémenté dans la bibliothèque de remote sensing Orféo développé par le CNES (Centre National d'Etudes Spatiales). C'est cette bibliothèque disponible sur le langage Python via un API que l'on utilisera dans de futurs programmes.



## Reste à faire : 

- Trouver une plateforme pour télécharger des données de télédétection hautes résolutions sur les agglomérations françaises -> Done : Google Earth Engine 
- Importer ces images dans le framework earthpy si possible
- Assimiler les techniques de télédétection avec une recherche bibliographique -> In the process : des articles ont été trouvés mais nécessitent encore des éclaircissements sur le sujet 
- Entraîner l'IA à exécuter le repérage des arbres
- Automatiser le tout avec l'utilisation d'un API de téléchargement
- Finir le développement de l'Index en contactant l'ADEME pour le calcul des ressources absorbées en hydrocarbures et énergie polluantes
