## How to Run Gunicorn
```gunicorn -b localhost:5001 'app:create_app()'```

## Migration
Create a migration repository `flask db init`
- Run migration `flask db migrate -m '<message>'`
- Apply the migration `flask db upgrade`

## Run Application with Flask
Create a migration repository `flask run`