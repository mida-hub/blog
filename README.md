# blog
```
cf. https://qiita.com/kawaMk4/items/89b18c608dc7dd2b946b
cf. https://qiita.com/tomo0/items/8dc619cc271f4c69658a
```

## django setup
```
pipenv shell
django-admin startproject config .
pipenv install -r ./requirements.txt
python manage.py migrate
django-admin startapp backend
// model 作成後
python manage.py makemigrations
python manage.py migrate
```

## vue setup
```
npm install -g @vue/cli@3.5.1
// lint is Basic
vue init webpack frontend
cd frontend
vue add vuetify
npm install --save webpack webpack-cli
npm install --save axios
npm run serve
```
![vue01](setup_img/vue01.png)
![vue02](setup_img/vue02.png)

## django setup2
```
cd ..
python manage.py runserver
```

## backend implementation
```
python manage.py migrate
python manage.py createsuperuser
```
