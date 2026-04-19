# 🧩 **TODO API**
## **🇬🇧 English Version**

### 📌 **Overview**
This project is a simple **Todo List API** built to strengthen foundational skills using **Python** and the **FastAPI** framework.
The API focuses on implementing core **CRUD operations** (Create, Read, Update, Delete).

---

### 🚀 **Features**
The API includes the following features:
* ➕ Create a task (id?, content, status?, created?, updated?)
* ✏️ Update a task (content?)
* 🔄 Change task status  (active, complete)
* 📋 Retrieve tasks filtered by status (active, complete)

---

###  🛠️ **Tech Stack**
* 🐍 **Python**
* ⚡ **FastAPI**
* 🗄️ **SQLite**

---

### 🧱 **Data Model**
**Task Entity**

| Field     | Type     | Description                       |
|-----------| -------- |-----------------------------------|
| `id`      | UUID     | Unique identifier of the task     |
| `content`  | String   | Task content                       |
| `status`  | Enum     | Task status: `active`, `complete` |
| `created` | DateTime | Task creation date                |
| `updated` | DateTime | Last update date                  |

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

* ➕ Ajouter une tâche (id?, content, status?, created?, updated?)
* ✏️ Modifier une tâche (content?)
* 🔄 Changer le statut d’une tâche (active, complete)
* 📋 Afficher les tâches selon leur statut (active, complete)

---

### 🛠️ **Stack Technique**
* 🐍 **Python**
* ⚡ **FastAPI**
* 🗄️ **SQLite**

---

### 🧱 **Modèle de données**
**Entité Task**

| Champ     | Type     | Description                    |
|-----------| -------- |--------------------------------|
| `id`      | UUID     | Identifiant unique de la tâche |
| `content` | String   | Contenu de la tâche            |
| `status`  | Enum     | Statut : `active`, `complete`  |
| `created` | DateTime | Date de création               |
| `updated` | DateTime | Date de dernière mise à jour   |

---

### URL Documentation
* **Docs :** [https://todo-list-api.fastapicloud.dev/docs](https://todo-list-api.fastapicloud.dev/docs)
* **Redocs :** [https://todo-list-api.fastapicloud.dev/redoc](https://todo-list-api.fastapicloud.dev/redoc)

---

### ⚠️ **Remarque**
Tout attribut marqué avec `?` est optionnel.
