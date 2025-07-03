import subprocess
import os
import shutil

def extract_emails_from_repo(github_url):
    repo_name = github_url.split("/")[-1]
    
    # Cloner le repo
    subprocess.run(["git", "clone", github_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if not os.path.isdir(repo_name):
        print("Échec du clonage du dépôt.")
        return

    os.chdir(repo_name)
    
    # Extraire les emails uniques
    result = subprocess.run(
        ["git", "log", "--pretty=format:%ae"], capture_output=True, text=True
    )
    
    emails = set(result.stdout.splitlines())
    print("📧 E-mails trouvés :")
    for email in sorted(emails):
        print(email)
    
    # Nettoyage : revenir en arrière et supprimer le repo cloné
    os.chdir("..")
    shutil.rmtree(repo_name)

# Exemple d'utilisation
extract_emails_from_repo("")
