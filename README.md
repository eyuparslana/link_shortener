# Link Shortener App

application for link shortening and daily click tracking

## Installation

- download the repo

```bash
https://github.com/eyuparslana/link_shortener.git
```

#### Required Installations

- postgresql
- redis

--------

- You must create a database named shortenerdb you can change the information in the settings file according to your own database
---

- change to project folder and run command below

```bash
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

- For celery worker run the code below
```bash
celery -A link_shortener beat -l INFO
```

Now you can use the app on localhost:8000

### Docker

- use on docker

```dockerfile
docker-compose up
```



