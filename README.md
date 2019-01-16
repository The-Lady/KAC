Key Aggregate Cryptosystem
======


### Introduction
This project is used for sharing data selectively among registered users.
- Share scalable data on cloud securely
- Delegate access rights to other users for selective data sharing using a fixed-size decryption key.

---

### Steps for setting up project
1. Clone the repo from URL `https://github.com/The-Lady/KAC.git`
2. Create a virtual environment **venv** using **virtualenv**
    - For PyCharm: Change interpreter to **virtualenv** which creates default virtual environment
    - Else: Use command `virtualenv venv`
3. Install requirements by `pip install -r requirements.txt`
4. Make migrations and run server
    ```bash
      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver
    ```
