# Recipe-Tracker-API

## Migration

- `python manage.py makemigrations --name <change_log> <app_label>`
- `python manage.py migrate`

## Quickstart

- Install postgres, poetry, cmake
- Create .env file with `.env.example` fields
- Run migration:

```
make migrate
```

- Run app:

```
make run
```

## Stagger docs

```
http://localhost:8000/swagger/
```
