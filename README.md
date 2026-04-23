# 🧩 **TODO API**
## **🇬🇧 English Version**

### 📌 **Overview**
This project is a simple **Todo List API** built to strengthen foundational skills using **Python** and the **FastAPI** framework.
The API focuses on implementing core **CRUD operations** (Create, Read, Update, Delete).

---

### 🚀 **Features**
The API includes the following features:
#### 👤 **User Management**
* ➕ Register a user (`id?`, `name`, `email`, `password`)
* 🔐 Login user
* 👤 Get current user profile (`me`) via JWT token
* 🚪 Logout use
#### ✅ **Task Management**
* ➕ Create a task (`id?`, `title`, `description?`, `status?`, `created?`, `updated?`)
* ✏️ Update a task (`title?`, `description?`)
* 🔄 Change task status (`active`, `complete`)
* 📋 Retrieve tasks filtered by status (`active`, `complete`)

---

###  🛠️ **Tech Stack**
* 🐍 **Python**
* ⚡ **FastAPI**
* 🗄️ **SQLite**

---

### 🧱 **Data Model**
👤 **User Entity**

| Field      | Type   | Description                   |
| ---------- | ------ | ----------------------------- |
| `id`       | UUID   | Unique identifier of the user |
| `name`     | String | User full name                |
| `email`    | String | User email address            |
| `password` | String | Hashed password               |

✅ **Task Entity**

| Field         | Type     | Description                   |
| ------------- | -------- | ----------------------------- |
| `id`          | Int      | Unique identifier of the task |
| `title`       | String   | Task title                    |
| `description` | String   | Task description              |
| `status`      | Enum     | `active` or `complete`        |
| `created`     | DateTime | Creation timestamp            |
| `updated`     | DateTime | Last update timestamp         |

---

### URL Documentation
* **Docs :** [https://todo-list-api.fastapicloud.dev/docs](https://todo-list-api.fastapicloud.dev/docs)
* **Redocs :** [https://todo-list-api.fastapicloud.dev/redoc](https://todo-list-api.fastapicloud.dev/redoc)

---

### **⚠️ Note**
Any field marked with `?` is optional.

---
___

## **🇫🇷 Version Française**

### 📌 **Présentation**
Ce projet est une **API de gestion de tâches (Todo List)** conçue pour renforcer les connaissances de base en **Python** avec le framework **FastAPI**.
L’API est principalement basée sur les opérations **CRUD** (Créer, Lire, Mettre à jour, Supprimer).

---

### 🚀 **Fonctionnalités**
Les fonctionnalités principales sont :

#### 👤 **Gestion des utilisateurs**
* ➕ Inscription d’un utilisateur (`id?`, `name`, `email`, `password`)
* 🔐 Connexion utilisateur
* 👤 Récupération du profil utilisateur connecté (`me`) via JWT
* 🚪 Déconnexion utilisateur

#### ✅ **Gestion des tâches**
* ➕ Création d’une tâche (`id?`, `title`, `description?`, `status?`, `created?`, `updated?`)
* ✏️ Modification d’une tâche (`title?`, `description?`)
* 🔄 Changement du statut d’une tâche (`active`, `complete`)
* 📋 Récupération des tâches filtrées par statut

---

### 🛠️ **Stack Technique**
* 🐍 **Python**
* ⚡ **FastAPI**
* 🗄️ **SQLite**

---

### 🧱 **Modèle de données**
👤 **Entité User**

| Champ      | Type   | Description                         |
| ---------- | ------ | ----------------------------------- |
| `id`       | UUID   | Identifiant unique de l’utilisateur |
| `name`     | String | Nom complet                         |
| `email`    | String | Adresse email                       |
| `password` | String | Mot de passe hashé                  |

✅ **Entité Task**

| Champ         | Type     | Description                    |
| ------------- | -------- | ------------------------------ |
| `id`          | Int      | Identifiant unique de la tâche |
| `title`       | String   | Titre de la tâche              |
| `description` | String   | Description de la tâche        |
| `status`      | Enum     | `active` ou `complete`         |
| `created`     | DateTime | Date de création               |
| `updated`     | DateTime | Dernière mise à jour           |

---

### URL Documentation
* **Docs :** [https://todo-list-api-8526eac4.fastapicloud.dev/docs](https://todo-list-api-8526eac4.fastapicloud.dev/docs)
* **Redocs :** [https://todo-list-api-8526eac4.fastapicloud.dev/redoc](https://todo-list-api-8526eac4.fastapicloud.dev/redoc)

---

### ⚠️ **Remarque**
Tout attribut marqué avec `?` est optionnel.
