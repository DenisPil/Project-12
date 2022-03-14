# Programme LitReview.

<p align="center">
<img src="https://user.oc-static.com/upload/2020/09/22/16007804386673_P10.png" width="25%"></img>
</p>

## Conditions d'utilisation:
* Utiliser Python version 3.0 ou +
* Utiliser Django version 3.0 ou +
* La base de données PostgreSQL version 12.0 ou +

## Pour utiliser ce programme il faut commencer par télécharger le dépôt GitHub.

### Copier le dépôt (repository) GitHub :
* Pour cela lancer un terminal, déplacer vous dans le dossier voulue. 
* créer un nouveau dossier
````
$ mkdir epic-event
````
* télécharger le dépôt 
````
$ git clone https://github.com/DenisPil/Project-12
````


## La prochaine étape est d'installer l'environnement virtuel.

### Créér l'environnement virtuel :
*  Lancer un terminal et rentrer les commandes suivantes : 

````
$ python -m venv <le nom de l'environnement> (création de l'environnement)    
````

### Pour activer l'environnement sur windows :
````
$ <le nom de l'environnement>/Scripts/activate 
````

### OU

### Pour activer l'environnement sur linux :

````
$ source <le nom de l'environnement>/bin/activate
````

### La dernière étape est l'installation des packages. Les packages sont référencés dans le fichier.
*  requirements.txt. Entrer la commande suivante pour installer tous les packages.
````
$ pip install -r requirements.txt
````


## La dernière étape est d'activer le serveur de développement.

### Une fois l'environnement créé et activé, il faut activer le serveur de développement.
*  À partir d'un terminal la première étape est d'exécuter le serveur.
*  Se rendre à la racine du projet et rentrer la commande suivante :
````
$ python manage.py runserver
````
* Le serveur est activé, se rendre à l'adresse suivante : http://127.0.0.1:8000/

### Se connecter avec le compte admin.
* se rendre à l'adresse : http://127.0.0.1:8000/admin
* Nom d'utilisateur : admin
* Mot de passe : admin1
* Permet de contrôler les informations de la base de donnée. Pouvoir effectuer les opérations CRUD sur les éléments suivants :
  * Staff : les équipes d'épic event
  * Customer : Les clients enregistré dans la base de données
  * Contract : Les contracts en relation avec les clients et les événements
  * Event : Les événements

## API :
La liste des endpoints avec leur autorisations pour accéder au différente fonctions de l'API.
````
POST : http://127.0.0.1:8000/login/
````
Permet aux utilisateurs de ce connecter avec leur identifiant. Pour accéder aux prochain endpoint il est nécessaire d'être identifier.
Autorisation : Aucune.

````
POST : http://127.0.0.1:8000/staff/
````
* Permet de créer un un membre de l'équipe d'Epic Event.
  * les informations requise :
  * username : Le nom d'utilisateur
  * email : L'email de l'utilisateur (il doit petre unique)
  * password : Le mot de passe
  * role : Le role du collaborateur il peut être, "sales team", "support team" ou "management team"
  * Autorisation : Seul un membre de l'équipe de management peut créer un collaborateur.
