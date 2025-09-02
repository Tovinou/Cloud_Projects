# Data Platform Project
A comprehensive Docker-based data platform project that implements multiple exercises covering containerization, web APIs, database integration, cron jobs, and ETL processes.

## Project Overview
This project demonstrates various data engineering concepts through a series of interconnected services, all containerized with Docker and orchestrated with Docker Compose.

## Services
1. **Simple Python App (Övning 1)**
A basic Python application that reads data from a file and outputs it to the console.

2. **Flask App (Övning 2)**
A Flask web application that renders a template with information about a user or project.

3. **Flask DB App (Övning 3)**
A Flask application connected to a PostgreSQL database, demonstrating database interactions using SQLAlchemy.

4. **Cron Job with Playwright (Övning 4)**
A scheduled task that uses Playwright to measure website load times and logs the results.

5. **Fake Data API (Övning 5.1)**
A Flask API that generates fake customer, product, and order data using the Faker library.

6. **ETL Processor (Övning 5.2)**
A data processing application that extracts data from the Fake Data API, transforms it, and loads it into a database while creating visualizations.

7. **Database**
A PostgreSQL database instance used by the Flask DB App and ETL Processor.

8. **Nginx Web Server**
Serves the results from the cron job measurements.

## Prerequisites
- Docker
- Docker Compose
- Git (optional)

## Project Structure
```
data-platform-project/
├── docker-compose.yml
├── simple-python-app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── flask-app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   └── templates/
│       └── index.html
├── flask-db-app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   └── models.py
├── cron-job/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── script.py
│   └── data/
├── fake-data-api/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   └── generators.py
├── etl-processor/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── processor.py
└── nginx/
    └── nginx.conf
```

## Installation and Setup
1. Clone or download this project to your local machine.

2. Ensure Docker and Docker Compose are installed and running.

3. Build and start all services:
   ```bash
   docker-compose up --build
   ```
   To run services in detached mode:
   ```bash
   docker-compose up -d --build
   ```

## Accessing the Services
After starting the containers, you can access the various services:

- **Flask App:** http://localhost:5000
- **Flask DB App:** http://localhost:5001
- **Fake Data API:** http://localhost:5002
- **Cron Job Results:** http://localhost:8080

### API Endpoints
**Fake Data API**
- `GET /customers` - Returns generated customer data
- `GET /products` - Returns generated product data
- `GET /orders` - Returns generated order data

**Flask DB App**
- `GET /products` - Returns products from the database
- `GET /products/<id>` - Returns a specific product by ID

## Usage Examples
### Generate and Process Data
1. Ensure all services are running with `docker-compose up`.
2. The Fake Data API will be available at `http://localhost:5002`.
3. The ETL Processor will automatically fetch data from the API and process it.

### View Cron Job Results
- The cron job runs every minute to measure website load times.
- Results are saved to JSON files in the `cron-job/data` directory.
- View results at `http://localhost:8080`.

### Manual ETL Execution
To manually run the ETL process:
```bash
docker-compose run etl-processor python processor.py
```

## Stopping the Services
To stop all running containers:
```bash
docker-compose down
```
To stop and remove volumes (including database data):
```bash
docker-compose down -v
```

## Customization
- **Modifying Fake Data:** Edit `fake-data-api/generators.py` to change the data generation logic.
- **Changing Cron Job Target:** Edit `cron-job/script.py` to measure load times for different websites.
- **Adjusting ETL Process:** Modify `etl-processor/processor.py` to change how data is processed and visualized.

## Troubleshooting
### Common Issues
- **Port conflicts:** Change port mappings in `docker-compose.yml` if ports are already in use.
- **Build failures:** Ensure all required files exist in each service directory.
- **Database connection issues:** Verify the database container is running before starting dependent services.

### Viewing Logs
To view logs for a specific service:
```bash
docker-compose logs <service-name>
```
To view logs for all services:
```bash
docker-compose logs
```

## Technologies Used
- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Playwright
- Faker
- Pandas
- Matplotlib
- Docker
- Docker Compose
- Nginx

## License
This project is for educational purposes as part of the "Dataplattformar, dataintegration och molnlösningar" course.

## Contributing
This is an educational project. Forks and modifications are welcome for learning purposes.
