# Python Flask Docker Project

This project demonstrates a multi-container Docker setup using **Flask**, **PostgreSQL**, and **cron jobs**. It includes a simple Flask web application, a Flask app connected to a PostgreSQL database, a standalone Python app, and a scheduled cron job.

---

## Table of Contents
- [Python Flask Docker Project](#python-flask-docker-project)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Setup and Usage](#setup-and-usage)

---

## Project Structure

```
Python_app/
├── cron_job/
│   ├── cron_app.py
│   ├── Dockerfile
│   └── requirements.txt
├── flask_app/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── flask_db_app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── simple_app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

## Setup and Usage

To run this project locally, follow these steps:

1.  **Clone the repository (if applicable) and navigate to the project directory.**

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    You will need to have Flask installed.
    ```bash
    pip install Flask
    ```

4.  **Run the application:**
    Assuming your main Flask file is `app.py` inside the `flask_app` directory, you can run it directly:
    ```bash
    python flask_app/app.py
    ```

5.  **View the application:**
    Open your web browser and go to `http://127.0.0.1:5000`.