# blog
```
cf. https://qiita.com/citykong/items/bdd428dc50c8458dfd85
```

## django setup
```
pipenv shell
pipenv install -r ./requirements.txt
mkdir django_vue
cd django_vue
django-admin startproject config .
python manage.py migrate
django-admin startapp blog
python manage.py runserver
```

## vue setup
```
npm install -g @vue/cli@4.4.6
// lint is Basic
vue create frontend
cd frontend
npm install --save-dev webpack-bundle-tracker@0.4.3
touch vue.config.js
npm run build
```

## vue setup2
```
vue add vuetify
npm install --save axios
npm run serve
```
