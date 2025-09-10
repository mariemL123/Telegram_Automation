# Telegram Auto

🚀 Projet permettant d’automatiser certaines actions sur **Telegram** (par exemple : ajouter des utilisateurs à un groupe ou une chaîne).  
Le projet est basé sur **Python** et **Docker**, et utilise l’API officielle de Telegram (via [Telethon](https://github.com/LonamiWebs/Telethon)).

---

## ⚙️ Fonctionnalités
- Connexion à Telegram via l’API (`API_ID` & `API_HASH` requis).
- Gestion sécurisée de la session.
- Script `add_users.py` pour ajouter des membres automatiquement.
- Conteneurisation avec Docker pour un déploiement simple et portable.

---

## 📦 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/toncompte/telegram_auto.git
cd telegram_auto
