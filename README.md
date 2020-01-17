# Quiz web server
[![Build Status](https://travis-ci.org/rustam-python/Questioner-Server.svg?branch=master)](https://travis-ci.org/rustam-python/Questioner-Server)

Create your own quizzes with pretty simple web server!

## Getting Started
These instructions will get you a copy of the Quiz web server up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Packeges you need to deploy the Quiz web server on your system:

1. [Docker Engine-Community](https://docs.docker.com/install/linux/docker-ce/centos/) — any flavor you preffer (or for Windows).

2. [Docker Compose](https://docs.docker.com/compose/install/) — as simple orchestrator.


### Modules
The bot uses the following modules:
1. NGINX as a reverse proxy (to access to content of site and the graphical API of the web server).
2. PostgreSQL database for storing cumulative data.
3. The web server with Gunicorn engine.

### Settings
The application uses configuration files to interact with user configurations. To use the application your way, you need to create in the following configuration files:
1. `variables.env` — is settings file for postgres container.

```
POSTGRES_DB_HOST_NAME=db_host
POSTGRES_DB_PORT=db_port
POSTGRES_DB=db_name
POSTGRES_USER=user
POSTGRES_PASSWORD=password
SERVER_HOST=0.0.0.0
SERVER_PORT=5008
```

### Deploying

Build the containers and start docker-compose:

```
cd path_to_cloned_project/
docker-compose build
docker-compose up -d
```
