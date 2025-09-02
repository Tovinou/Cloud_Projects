# Dataplattformar, dataintegration och molnlösningar

This repository contains a collection of projects and exercises for the "Dataplattformar, dataintegration och molnlösningar" course at Jensen.

## Repository Structure

This repository is organized into several sub-directories, each containing a distinct project or set of exercises.

### Projects

-   **`/data-platform-project/`**: A microservices-based data platform project using Docker Compose. It includes services for a fake data API, an ETL processor, a cron job, a Flask web application, and an Nginx reverse proxy.

-   **`/EC2-instans docker/`**: Contains resources and instructions related to setting up and running Docker on an AWS EC2 instance.

-   **`/futurama_data/`**: A Python application that fetches data from a Futurama API and demonstrates storing it in various data stores, including MySQL, MongoDB, Redis, and the local file system.

-   **`/My_project/`**: A template or starting point for a general Python project.

-   **`/Pandas_Data_Analysis/`**: A data analysis project using the Pandas library. It includes scripts for downloading a Kaggle dataset, Jupyter notebooks for analysis, and various exercises.

-   **`/Python_app/`**: A containerized Python application using Docker Compose, featuring a cron job and a Flask web application.

-   **`/sports_joke_api/`**: A simple API that serves sports-related jokes, containerized with Docker.

### Exercises

-   **`/Övning/`**: Contains various exercises related to the course topics. (Övning is Swedish for "Exercise").

## Getting Started

Each project directory is self-contained. To run a specific project:

1.  Navigate to the project's directory:
    ```bash
    cd <project-directory>
    ```
2.  Look for a `README.md`, `docker-compose.yml`, or `requirements.txt` file for instructions on how to set up and run the project.
3.  For most Docker-based projects, you can typically start them with:
    ```bash
    docker-compose up --build
    ```
