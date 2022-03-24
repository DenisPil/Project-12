# Programme Epic-Event.

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
  * Staff : les équipes d'épic event.
  * Customer : Les clients enregistré dans la base de données.
  * Contract : Les contracts en relation avec les clients et les événements.
  * Event : Les événements.

## API :
La liste des endpoints avec leur autorisations pour accéder au différente fonctions de l'API.

### LOGIN
````
POST : http://127.0.0.1:8000/login/
````
* Permet aux utilisateurs de ce connecter avec leur identifiant. Pour accéder aux prochains endpoints il est nécessaire d'être identifier.
* Autorisation : Aucune.

### STAFF 
````
POST : http://127.0.0.1:8000/staff/
````
* Permet de créer un membre de l'équipe d'Epic Event. Les informations requises :
  * username : Le nom d'utilisateur.
  * email : L'email de l'utilisateur (il doit petre unique).
  * password : Le mot de passe.
  * role : Le role du collaborateur il peut être, "sales team", "support team" ou "management team".
* Autorisation : Seul un membre de l'équipe de management peut créer un collaborateur.

````
GET : http://127.0.0.1:8000/staff/
````
* Permet de visualiser la liste de tous les collaborateurs.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.

````
GET : http://127.0.0.1:8000/staff/'l'ID-du-collaborateur'
````
* Permet de visualiser les informations d'un collaborateur.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.

````
PUT : http://127.0.0.1:8000/staff/'l'ID-du-collaborateur'
````
* Permet de modifier un un membre de l'équipe d'Epic Event. Les informations requises :
  * username : Le nom d'utilisateur.
  * email : L'email de l'utilisateur (il doit petre unique).
  * password : Le mot de passe.
  * role : Le role du collaborateur il peut être, "sales team", "support team" ou "management team".
* Authorisation : Seul un membre de l'équipe de management peut modifier un collaborateur.

````
DEL : http://127.0.0.1:8000/staff/'l'ID-du-collaborateur'
````
* Permet de supprimer un un membre de l'équipe d'Epic Event.
* Authorisation : Seul un membre de l'équipe de management peut supprimer un collaborateur.

### CUSTOMER

````
POST : http://127.0.0.1:8000/customer/
````
* Permet d'ajouter un client à la base de données. Les informations requises :
  * first_name : Le prénom du client.
  * last_name : Le nom du client.
  * email : L'email du client.
  * phone : Le numéro de téléphone du client.
  * mobile : Le numéro de mobile du client.
  * company_name : Le nom de l'entreprise du client.
  * sales_contact : L'ID (l'identifiant) d'un membre de l'équipe de vente d'Epic Event, il sera en charge du client.
* Authorisation : L'équipe de vente et l'équipe de management peuvent créer un client.


````
GET : http://127.0.0.1:8000/customer/
````
* Permet de visualiser la liste de tous les clients.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.
* Filtre : il est possible de filtrer les clients à partir de leur nom ou de leur email :
  * ```` GET : http://127.0.0.1:8000/event/?name="nom du client" ````
  * ```` GET : http://127.0.0.1:8000/event/?email="email du client" ````

````
GET : http://127.0.0.1:8000/customer/'ID-du-client'
````
* Permet de visualiser les informations détaillé d'un client.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.

````
PUT : http://127.0.0.1:8000/customer/'ID-du-client'
````
* Permet de modifier les informations d'un client. Les informations requises :
  * first_name : Le prénom du client.
  * last_name : Le nom du client.
  * email : L'email du client.
  * phone : Le numéro de téléphone du client.
  * mobile : Le numéro de mobile du client.
  * company_name : Le nom de l'entreprise du client.
  * sales_contact : L'ID (l'identifiant) d'un membre de l'équipe de vente d'Epic Event, il sera en charge du client.
* Permet de supprimer un un membre de l'équipe d'Epic Event.
* Authorisation : L'équipe de vente, l'équipe de management peuvent modifier les informations d'un client.

````
DEL : http://127.0.0.1:8000/customer/'ID-du-client'
````
* Permet de supprimer un client de la base de données.
* Authorisation : L'équipe de vente, l'équipe de management peuvent supprimé d'un client.

#### CONTRACT
````
POST : http://127.0.0.1:8000/contract/
````
* Permet de créer un contract qui lie un client à un futur événement. Les informations requises :
  * sales_contact : L'ID (l'identifiant) d'un membre de l'équipe de vente d'Epic Event, il sera en charge du client.
  * customer : L'ID (l'identifiant) du client pour qui est créer le contract.
  * status : Le Contract est t'il signé si oui "True", si il ne l'est pas "False".
  * amount : Le prix de l'événement.
* Authorisation : L'équipe de vente, l'équipe de management peuvent supprimé un contract.

````
GET : http://127.0.0.1:8000/contract/
````
* Permet de visualiser la liste de tous les contracts.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.
* Filtre : il est possible de filtrer les contract à partir du nom du client qui est lié au contract, l'email du client qui est lié au contract, la date du contract ou le montant du contract :
  * ````http://127.0.0.1:8000/contract/?name="nom du client"````
  * ````http://127.0.0.1:8000/contract/?email="email du client"````
  * ````http://127.0.0.1:8000/contract/?date contract="la date du contract"````
  * ````http://127.0.0.1:8000/contract/?prix contract="le montant du contract"````

````
GET : http://127.0.0.1:8000/contract/"ID-du-contract"
````
* Permet de visualiser les informations détaillé d'un contract.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.

````
PUT : http://127.0.0.1:8000/contract/"ID-du-contract"
````
* Permet de modifier un contract. Les informations requises :
  * sales_contact : L'ID (l'identifiant) d'un membre de l'équipe de vente d'Epic Event, il sera en charge du client.
  * customer : L'ID (l'identifiant) du client pour qui est créer le contract.
  * status : Le Contract est t'il signé si oui "True", si il ne l'est pas "False".
  * amount : Le prix de l'événement.
* Authorisation : L'équipe de vente et l'équipe de management peuvent créer un contract.

````
DEL : http://127.0.0.1:8000/contract/"ID-du-contract"
````
* Permet de supprimer un contract.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.

#### EVENT
````
POST : http://127.0.0.1:8000/event/
````
* Permet la création d'un événement.
  * contract_event : L'ID (l'identifiant) du contract pour lequel l'événement est créer.
  * event_date : La date de l'événment.
  * number_guests : Le nombre d'invité à l'événement.
  * commentary : Un commentaire sur l'événement (informations diverse sur l'événement).
  * support_contact : L'ID (l'identifiant) d'un membre de l'équipe de support qui aura en charge l'événement.
  * event_status : Les status : 'paiement en cours', 'payé', 'événement à venir', 'événement en cours', 'événement terminé'.
* Authorisation : L'équipe de vente et l'équipe de management peuvent créer un événement.

````
GET : http://127.0.0.1:8000/event/
````
* Permet de visualiser la liste de tous les événements.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.
* Filtre : Il est possible de filtrer les événement à partir du nom du client, l'email du client, la date de l'événement :
  * ```` GET : http://127.0.0.1:8000/event/?name="le nom du client"````
  * ```` GET : http://127.0.0.1:8000/event/?email="l'email du client"````
  * ```` GET : http://127.0.0.1:8000/event/?date="la date de l'événement"````
````
GET : http://127.0.0.1:8000/event/"ID-d'un-événement"
````
* Permet de visualiser un événement en détail.
* Authorisation : L'équipe de vente, l'équipe support et l'équipe de management.

````
PUT : http://127.0.0.1:8000/event/"ID-d'un-événement"
````
* Permet de modifier les informations d'un événement.
  * contract_event : L'ID (l'identifiant) du contract pour lequel l'événement est créer.
  * event_date : La date de l'événment.
  * number_guests : Le nombre d'invité à l'événement.
  * commentary : Un commentaire sur l'événement (informations diverse sur l'événement).
  * support_contact : L'ID (l'identifiant) d'un membre de l'équipe de support qui aura en charge l'événement.
  * event_status : Les status : 'paiement en cours', 'payé', 'événement à venir', 'événement en cours', 'événement terminé'.
* Authorisation : L'équipe de vente et l'équipe de management peuvent modifier un événement.

````
DEL : http://127.0.0.1:8000/event/"ID-d'un-événement"
````
* Permet de supprimer un événement.
* Authorisation : L'équipe de vente, l'équipe support peuvent supprimer un événement.
