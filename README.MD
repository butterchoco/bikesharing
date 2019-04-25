# BikeSharing 
[![pipeline status](https://gitlab.com/c6-basdat/bikesharing/badges/master/pipeline.svg)](https://gitlab.com/c6-basdat/bikesharing/commits/master)

## GETTING STARTED
Bike Sharing is an application to manage your bike station. This app is built in order to increase the usage of bike in largest city of Indonesia. Bike sharing is developed underpressure. Its idea is come from an assignment from contributor's university in Computer Science Faculty.

## INSTALLATION
Setting up the project to your local machine:
```
git init
git remote add origin https://gitlab.com/c6-basdat/bikesharing.git
git pull origin master
pip install -r requirements.txt
```

**Hilangkan comment CODE di bawah ini jika ingin integrasi django dengan postgres local**

```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'bikesharing',                                # NAME itu nama database local
         'USER' : 'postgres',                                  # USER itu nama user local
         'PASSWORD' : 'superuser',                             # PASSWORD itu password user local
         'HOST' : 'localhost',
         'PORT' : '5433',                                      # PORT yang ada di local saat install postgres pertama kali
     }
}
```

**Comment CODE di bawah ini jika ingin integrasi django dengan postgres local**
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1ejmv9dvb87c7',
        'USER' : 'ioerjbwnqvxdby',
        'PASSWORD' : 'fe09a0a3f8604581154d440db57c479d5fd858be1af21d2a299930ca1e51a744',
        'HOST' : 'ec2-23-23-228-132.compute-1.amazonaws.com',
        'PORT' : '5432',
    }
}

Finish your work based on apps that had already shuffled !

**Note** : Don't forget to do "python manage.py startapp [NEW_APP]" to make a new app.

## CONTRIBUTE
1. Ahmad Supriyanto
2. Azhar Rais
3. Fatih Almutawakkil
4. Yudha Ananda Rahayu Putra

## CREDIT
Database Course Term 2 - 2017