# **Projet Réel de la Semaine :** Gestionnaire de Contacts : Créer une application permettant d'ajouter, de supprimer, de rechercher et de modifier des contacts à l'aide de listes ou de dictionnaires.

def afficher_contacts(contacts): #methode pour afficher la liste de contact
    if not contacts:
        print("Aucun contact trouvé")
        return
    for i, contact in enumerate(contacts):
        print(f"{i + 1}. {contact['nom']} ({contact['telephone']}) - {contact['email']}")


def ajouter_contact(contacts): #methode pour ajouter un nouveau contact
    nouveau_contact = {
        "nom": input("Entrez le nom du contact : "),
        "telephone": (input("Entrez le numéro du contact : ")),
        "email": input("Entrez l'adresse mail du contact : ")
    }
    contacts.append(nouveau_contact)
    print(f"{nouveau_contact} a été ajouté a liste")


def supprimer_contact(contacts): #methode pour supprimer un contact
    if not contacts:
        print("Aucun contact trouvé")
        return
    afficher_contacts(contacts)
    index = int(input(f"Entrez le numero du contact a supprimer : ")) - 1
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact supprimé")
    else:
        print("Numéro invalide")


def rechercher_contact(contacts): #methode pour rechercher un nouveau contact
    if not contacts:
        print("Aucun contact trouvé")
        return
    nom_recherche = input("Entrez le nom du contact recherche : ")
    resultats = [contact for contact in contacts if nom_recherche.lower() in contact['nom'].lower()]
    if resultats:
        print(f'Contact trouvé pour {nom_recherche}')
        afficher_contacts(contacts)
    else:
        print(f"Contact non trouvé pour {nom_recherche}")


def modifier_contact(contacts): #methode pour modifier un nouveau contact
    if not contacts:
        print("Aucun contact trouvé")
        return
    afficher_contacts(contacts)
    index = int(input("Entrez le numéro du contact a modifier : ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        nouveau_nom = input(f'Entrez le nouveau nom du contact ({contact['nom']} : ) ' or contacts['nom'])
        nouveau_tel = input(f'Entrez le nouveau numéro du contact ({contact['telephone']} : )' or contacts['telephone'])
        nouveau_email = input(f'Entrez le nouveau nom du contact ({contact['email']} : )' or contacts['email'])
        contacts[index] = {
            "nom": nouveau_nom,
            "telephone": nouveau_tel,
            "email": nouveau_email
        }
        print("Contact modifié")
    else:
        print("Contact non trouvé()")


# contacts par defaut 
contacts = [
    {"nom": "Samuel", "telephone": "0123456789", "email": "sam@exemple.com"},
]

# Menu principal
while True:
    print("\n--- Gestionnaire de Contacts ---")
    print("\nQue souhaitez vous faire?\n")
    print("1. Afficher les contacts")
    print("2. Ajouter un contact")
    print("3. Supprimer un contact")
    print("4. Rechercher un contact")
    print("5. Modifier un contact")
    print("6. Quitter")

    choix = input("Entrez votre choix (1-6) :")

    if choix == '1':
        afficher_contacts(contacts)
    elif choix == '2':
        ajouter_contact(contacts)
    elif choix == '3':
        supprimer_contact(contacts)
    elif choix == '4':
        rechercher_contact(contacts)
    elif choix == '5':
        modifier_contact(contacts)
    elif choix == '6':
        break
    else:
        print("Choix invalide. Veuillez réessayer.")

print("Merci d'avoir utilisé le Gestionnaire de Contacts !\n")
