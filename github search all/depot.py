import requests


def list_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(f"- {repo['name']} (⭐ {repo['stargazers_count']}) - Langage : {repo['language']}")
    else:
        print("Erreur lors de la récupération des dépôts.")

# Exemple d'utilisation
list_repositories("usershhh")