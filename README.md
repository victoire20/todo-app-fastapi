# 🧩 **TODO API**
## **🇬🇧 English Version**

### 📌 **Overview**
This project is a simple **Todo List API** built to strengthen foundational skills using **Python** and the **FastAPI** framework.
The API focuses on implementing core **CRUD operations** (Create, Read, Update, Delete).

---

### 🚀 **Features**
The API includes the following features:
* ➕ Create a task (id?, title, description, status?, created?, updated?)
* ✏️ Update a task (title?, description?)
* 🔄 Change task status  (todo, waiting, completed)
* 📋 Retrieve tasks filtered by status (todo, waiting, completed)

---

###  🛠️ **Tech Stack**
* 🐍 **Python**
* ⚡ **FastAPI**
* 🗄️ **SQLite**

---

### 🧱 **Data Model**
**Task Entity**

| Field         | Type     | Description                                 |
| ------------- | -------- | ------------------------------------------- |
| `id`          | UUID     | Unique identifier of the task               |
| `title`       | String   | Task title                                  |
| `description` | String   | Task description                            |
| `status`      | Enum     | Task status: `todo`, `waiting`, `completed` |
| `created`     | DateTime | Task creation date                          |
| `updated`     | DateTime | Last update date                            |

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

* ➕ Ajouter une tâche (id?, title, description, status?, created?, updated?)
* ✏️ Modifier une tâche (title?, description?)
* 🔄 Changer le statut d’une tâche (todo, waiting, completed)
* 📋 Afficher les tâches selon leur statut (todo, waiting, completed)

---

### 🛠️ **Stack Technique**
* 🐍 **Python**
* ⚡ **FastAPI**
* 🗄️ **SQLite**

---

### 🧱 **Modèle de données**
**Entité Task**

| Champ         | Type     | Description                             |
| ------------- | -------- | --------------------------------------- |
| `id`          | UUID     | Identifiant unique de la tâche          |
| `title`       | String   | Titre de la tâche                       |
| `description` | String   | Description de la tâche                 |
| `status`      | Enum     | Statut : `todo`, `waiting`, `completed` |
| `created`     | DateTime | Date de création                        |
| `updated`     | DateTime | Date de dernière mise à jour            |

---

### ⚠️ **Remarque**
Tout attribut marqué avec `?` est optionnel.