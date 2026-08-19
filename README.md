# Calculateur de trajet Zemidjan / Taxi

Ce projet est un programme Python en ligne de commande qui permet de calculer le prix d’un trajet à Lomé en fonction du moyen de transport choisi, de la distance parcourue et de l’heure du trajet.

Le programme prend en charge deux moyens de transport : le **zemidjan**, qui correspond au taxi-moto, et la **voiture**, qui correspond au taxi classique.

## Fonctionnalités

Le programme permet de choisir un moyen de transport, de saisir une distance en kilomètres et d’indiquer l’heure du trajet au format `HH:MM`. Il détecte automatiquement si le trajet est effectué pendant une période d’heure de pointe.

Il applique ensuite la formule officielle suivante :

```text
prix avant majoration = tarif de base + prix au kilomètre × distance
```

Lorsque le trajet est effectué à une heure de pointe, une majoration est appliquée au prix total du trajet. Le programme permet également d’arrondir le prix final au multiple de 25 FCFA le plus proche, de calculer plusieurs trajets pendant la même session et de consulter l’historique des trajets calculés.

## Tarifs utilisés

| Moyen de transport | Tarif de base | Prix au kilomètre | Majoration heure de pointe |
|---|---:|---:|---:|
| Zemidjan (taxi-moto) | 150 FCFA | 75 FCFA/km | 15 % |
| Voiture | 200 FCFA | 100 FCFA/km | 25 % |

Les plages horaires considérées comme des heures de pointe sont les suivantes :

| Période | Horaire |
|---|---|
| Matin | 07h00 à 08h45 |
| Déjeuner | 11h45 à 13h00 |
| Soir | 17h00 à 19h00 |

## Prérequis

Pour exécuter ce projet, il faut disposer de **Python 3** installé sur l’ordinateur. Le programme utilise uniquement des fonctionnalités intégrées à Python et ne nécessite aucune bibliothèque externe.

Pour vérifier l’installation de Python sous Windows, ouvrir PowerShell et exécuter :

```powershell
python --version
```

Si cette commande ne fonctionne pas, essayer :

```powershell
py --version
```

## Installation

Cloner le dépôt avec la commande suivante :

```powershell
git clone https://github.com/theophiledounon-dotcom/zemidjan-calculator.git
```

Entrer ensuite dans le dossier du projet :

```powershell
cd zemidjan-calculator
```

## Exécution

Lancer le programme avec :

```powershell
python zemidjan-calculateur.py
```

## Utilisation

Au démarrage, le programme affiche un menu permettant de choisir le moyen de transport :

```text
Moyens de transport :
1. zemidjan (taxi-moto)
2. voiture
Choisissez un moyen de transport :
```

Il demande ensuite la distance, l’heure du trajet et si l’utilisateur souhaite arrondir le prix au multiple de 25 FCFA le plus proche.

Après le calcul, un récapitulatif est affiché avec le moyen de transport, la distance, l’heure, le statut d’heure de pointe, le prix avant majoration et le prix final.

## Exemple d’exécution

Pour un trajet en zemidjan de **5 km** à **07:20**, l’heure est considérée comme une heure de pointe.

Le calcul est le suivant :

```text
Prix avant majoration = 150 + (75 × 5)
Prix avant majoration = 525 FCFA

Prix final = 525 × 1,15
Prix final = 603,75 FCFA
```

Le résultat affiché par le programme est similaire à :

```text
========== RECAPITULATIF ==========
Moyen de transport : zemidjan (taxi-moto)
Distance           : 5.00 km
Heure              : 07:20
Heure de pointe    : Oui
Prix avant majoration : 525.00 FCFA
Prix final         : 603.75 FCFA
================================
```

## Historique des trajets

Après chaque calcul, le programme propose trois choix :

```text
1. Calculer un autre trajet
2. Afficher l'historique
3. Quitter
```

L’historique est conservé uniquement pendant l’exécution du programme. Il contient les trajets calculés pendant la session en cours.

Exemple :

```text
========== HISTORIQUE ==========
1. zemidjan (taxi-moto) | 5.00 km | 07:20 | Pointe: Oui | 603.75 FCFA
================================
```

## Vérification de la syntaxe

Avant d’exécuter le programme, il est possible de vérifier uniquement la syntaxe du fichier avec :

```powershell
python -m py_compile zemidjan-calculateur.py
```

Si aucune erreur ne s’affiche, la syntaxe Python est correcte.

## Structure recommandée du dépôt


```text
zemidjan-calculator/
├── zemidjan-calculateur.py
└── README.md
```

## Technologies utilisées

Le projet utilise Python 3, les dictionnaires, les fonctions, les boucles `while`, les conditions `if`, la gestion des erreurs avec `try/except`, les listes, les f-strings et la conversion d’une heure en minutes pour comparer les plages horaires.

## Auteur

Projet réalisé par **Theophile Sèdonou DOUNON** dans le cadre du challenge **30 Days of Python — Python Togo**.

Dépôt GitHub : [theophiledounon-dotcom/zemidjan-calculator](https://github.com/theophiledounon-dotcom/zemidjan-calculator)
