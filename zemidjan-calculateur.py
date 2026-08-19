# Calculateur de trajet zemidjan ou taxi

# Informations à propos des moyens de transport
TRANSPORTS = {
    "1": {
        "nom": "zemidjan (taxi-moto)",
        "tarif_base": 150,
        "prix_km": 75,
        "majoration": 0.15,
    },
    "2": {
        "nom": "voiture",
        "tarif_base": 200,
        "prix_km": 100,
        "majoration": 0.25,
    },
}

# Les heures de pointe sont exprimées en minutes depuis minuit
PLAGES_HEURE_POINTE = [
    (7 * 60, 8 * 60 + 45),
    (11 * 60 + 45, 13 * 60),
    (17 * 60, 19 * 60),
]


def choisir_transport():
    print("\n Moyens de transport :")
    print(" 1. zemidjan (taxi-moto)")
    print(" 2. voiture")

    while True:
        choix = input(" Choisissez un moyen de transport : ").strip()
        if choix in TRANSPORTS:
            return TRANSPORTS[choix]
        print(" Erreur : choisissez 1 ou 2.")


def demander_distance():
    while True:
        try:
            distance = float(input(" Veuillez entrer la distance en kilomètres : ").strip().replace(",", "."))
            if distance > 0:
                return distance
            print(" Erreur : la distance doit être positive.")
        except ValueError:
            print(" Erreur : entrez un nombre valide.")


def demander_heure():
    while True:
        heure = input(" Veuillez entrer l'heure du trajet au format HH:MM : ").strip()
        morceaux = heure.split(":")

        if len(morceaux) == 2:
            try:
                heures = int(morceaux[0])
                minutes = int(morceaux[1])
                if 0 <= heures <= 23 and 0 <= minutes <= 59:
                    total_minutes = heures * 60 + minutes
                    return heure, total_minutes
            except ValueError:
                pass

        print(" Erreur : veuillez respecter le format HH:MM, par exemple 07:30.")


def trouver_heure_de_pointe(total_minutes):
    for debut, fin in PLAGES_HEURE_POINTE:
        if debut <= total_minutes <= fin:
            return True
    return False


def demander_arrondi():
    while True:
        choix = input(" Arrondir au multiple de 25 FCFA ? (o/n) : ").strip().lower()
        if choix in ("o", "oui"):
            return True
        if choix in ("n", "non"):
            return False
        print(" Erreur : veuillez répondre par o ou n.")


def calculer_prix(transport, distance, heure_pointe, arrondir):
    prix_base = transport["tarif_base"] + transport["prix_km"] * distance

    if heure_pointe:
        prix_final = prix_base * (1 + transport["majoration"])
    else:
        prix_final = prix_base

    if arrondir:
        prix_final = round(prix_final / 25) * 25

    return prix_base, prix_final


def afficher_resultat(transport, distance, heure, heure_pointe, prix_base, prix_final, arrondi):
    print("\n =========== RECAPITULATIF ===========")
    print(f" Moyen de transport : {transport['nom']}")
    print(f" Distance           : {distance:.2f} km")
    print(f" Heure              : {heure}")
    print(f" Heure de pointe    : {'Oui' if heure_pointe else 'Non'}")
    print(f" Prix avant majoration : {prix_base:.2f} FCFA")

    if arrondi:
        print(f" Prix final         : {prix_final:.0f} FCFA")
    else:
        print(f" Prix final         : {prix_final:.2f} FCFA")

    print(" ================================")


def afficher_historique(historique):
    if len(historique) == 0:
        print("\n Aucun trajet enregistré.")
        return

    print("\n ========== HISTORIQUE ==========")
    for numero, trajet in enumerate(historique, start=1):
        pointe = "Oui" if trajet["heure_pointe"] else "Non"
        print(
            f"{numero}. {trajet['transport']} | {trajet['distance']:.2f} km | "
            f"{trajet['heure']} | Pointe: {pointe} | {trajet['prix_final']:.2f} FCFA"
        )
    print(" ================================")


def main():
    historique = []

    print(" ------------------------------------------------")
    print(" CALCULATEUR DE TRAJET")
    print(" ------------------------------------------------")

    while True:
        transport = choisir_transport()
        distance = demander_distance()
        heure, total_minutes = demander_heure()
        arrondir = demander_arrondi()

        heure_pointe = trouver_heure_de_pointe(total_minutes)
        prix_base, prix_final = calculer_prix(transport, distance, heure_pointe, arrondir)

        afficher_resultat(
            transport,
            distance,
            heure,
            heure_pointe,
            prix_base,
            prix_final,
            arrondir,
        )

        historique.append({
            "transport": transport["nom"],
            "distance": distance,
            "heure": heure,
            "heure_pointe": heure_pointe,
            "prix_final": prix_final,
        })

        while True:
            print("\n 1. Calculer un autre trajet")
            print(" 2. Afficher l'historique")
            print(" 3. Quitter")
            choix = input(" Votre choix : ").strip()

            if choix == "1":
                break
            elif choix == "2":
                afficher_historique(historique)
            elif choix == "3":
                print(" Merci d'avoir utilisé le calculateur.")
                return
            else:
                print(" Erreur : choisissez 1, 2 ou 3.")


if __name__ == "__main__":
    main()