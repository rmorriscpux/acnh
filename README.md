# acnh
Animal Crossing New Horizons Collections

## Before Running Server First Time

After running makemigrations and migrate, do the following from the Django manage.py shell:

> from collectables import rebuild_db

__Do not touch rebuild_db.py otherwise!__

### Dependency

django-mathfilters
