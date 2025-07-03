import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"  # Correction ici
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Nom complet : {data.get('name')}")
        print(f"Bio : {data.get('bio')}")
        print(f"Localisation : {data.get('location')}")
        print(f"Blog : {data.get('blog')}")
        print(f"Public repos : {data.get('public_repos')}")
        print(f"Followers : {data.get('followers')}")
        print(f"Compte créé le : {data.get('created_at')}")
    else:
        print("Utilisateur non trouvé ou erreur.")

# Exemple d'utilisation
get_user_info("usershhh")
