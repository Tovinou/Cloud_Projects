# Simple CI/CD Pipeline

Ett enkelt exempel på en CI/CD-pipeline med GitHub Actions och OpenShift.

## Projektöversikt

Detta projekt demonstrerar en enkel CI/CD-pipeline för en Python Flask-applikation. Pipelinen använder GitHub Actions för att bygga, testa och distribuera applikationen till OpenShift.

## Funktioner

- Enkel Flask-webbapplikation
- Automatiserade tester med Behave (BDD)
- Containerisering med Docker
- CI/CD-pipeline med GitHub Actions
- Deployment till OpenShift

## Teknologier

- Python 3.x
- Flask 2.3.3
- Behave 1.2.6
- Docker
- GitHub Actions
- OpenShift

## Kom igång

### Förutsättningar

- Python 3.x
- pip
- Git
- Docker (valfritt för lokal containerisering)

### Installation

1. Klona repositoryt:
   ```
   git clone <repository-url>
   cd simple_cd_ci_pipeline
   ```

2. Installera beroenden:
   ```
   pip install -r requirements.txt
   ```

### Kör applikationen lokalt

```
python app.py
```

Applikationen kommer att köras på `http://localhost:8080`.

### Kör tester

```
behave
```

## CI/CD Pipeline

Projektet använder GitHub Actions för att automatisera bygg-, test- och deploymentprocessen. Pipelinen utför följande steg:

1. Bygger applikationen
2. Kör automatiserade tester
3. Bygger en Docker-container
4. Pushar containern till ett containerregister
5. Distribuerar applikationen till OpenShift

## Projektstruktur

```
simple_cd_ci_pipeline/
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # GitHub Actions workflow-konfiguration
├── features/
│   ├── exemple.feature    # BDD-testspecifikationer
│   └── steps/
│       └── test_steps.py  # Testimplementationer
├── app.py                 # Flask-applikation
├── Dockerfile             # Docker-konfiguration
├── kubernetes.yaml        # Kubernetes/OpenShift-konfiguration
├── requirements.txt       # Projektberoenden
└── README.md              # Projektdokumentation
```

## Bidra

1. Forka repositoryt
2. Skapa en feature branch (`git checkout -b feature/amazing-feature`)
3. Committa dina ändringar (`git commit -m 'Add some amazing feature'`)
4. Pusha till branchen (`git push origin feature/amazing-feature`)
5. Öppna en Pull Request

## Licens

Detta projekt är licensierat under MIT-licensen.