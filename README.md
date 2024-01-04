
1. Rebuild the schema and database
```
rm db/relevation.db
python manage.py migrate --run-syncdb
```

2. Start server
```
python manage.py runserver
```
