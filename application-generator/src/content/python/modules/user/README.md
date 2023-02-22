## How to Run Gunicorn
```gunicorn -b localhost:5003 'app:create_app()'```

## Migration
Create a migration repository `flask db init`
- Run migration `flask db migrate -m '<message>'`
- Apply the migration `flask db upgrade`

## Run Migration Seeder
- Run database seeder `flask seed run`

## Run Application with Flask
Create a migration repository `flask run`
