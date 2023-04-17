# Employees app
A web page that displays the hierarchy of employees in a tree form.

* Url: http://localhost/employees

## Run app
### Create .env
```bash
cp config/.env.example config/.env
```
### Run
```bash
docker-compose up -d --build
```

## Run dev
```bash
docker-compose -f docker-compose.yml -f docker-compose-dev.yml up -d
```
### Linter
```bash
pip install -r requirements-dev.txt
flake8 .
isort .
```