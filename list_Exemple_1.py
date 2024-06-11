# exemple1: Créer un programme qui gère une liste de courses et permet d'ajouter, supprimer et marquer des articles comme achetés.


def afficher_liste(liste_articles):
    if not liste_articles:
        print("\nLa liste de articles est vide.")
    else:
        for item in liste_articles:
            print(f"- {item}")


def ajouter_article(liste_articles):
    article = input("Quel article souhaitez-vous ajouter ? : ")
    liste_articles.append(article)
    print(f"{article} ajouté à la liste.")


def supprimer_article(liste_articles):
    if not liste_articles:
        print("\nLa liste de articles est vide.")
    afficher_liste(liste_articles)
    index = int(input("Entrez le numéro de l'article à supprimer : ")) - 1

    if 0 <= index < len(liste_articles):
        article_supprime = liste_articles.pop(index)
        print(f"{article_supprime} supprimé de la liste.")
    else:
        print("Numéro d'article invalide.")


def marquer_achete(liste_articles):
    if not liste_articles:
        print("La liste de articles est vide.")
    afficher_liste(liste_articles)
    index = int(input("Entrez le numéro de l'article à marquer comme acheté : ")) - 1

    if 0 <= index < len(liste_articles):
        liste_articles[index] = f"{liste_articles[index]} (acheté)"
        print(f"Article marqué comme acheté.")
    else:
        print("Numéro d'article invalide.")


def main():
    # Fonction principale.
    liste_articles = []

    while True:
        print("\n\t MENU ")
        print("1. Afficher la liste")
        print("2. Ajouter un article")
        print("3. Supprimer un article")
        print("4. Marquer un article comme acheté")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            afficher_liste(liste_articles)
        elif choix == "2":
            ajouter_article(liste_articles)
        elif choix == "3":
            supprimer_article(liste_articles)
        elif choix == "4":
            marquer_achete(liste_articles)
        elif choix == "5":
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()