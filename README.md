# blog
## cf.
```
- https://illust8.com/contents/184
- https://qiita.com/citykong/items/bdd428dc50c8458dfd85
- https://qiita.com/kawaMk4/items/89b18c608dc7dd2b946b
- https://qiita.com/ryo_mt09sp/items/574bed236f3128cf97cd
- https://medium.com/@kjmczk/blogsite-django-747046b453f9
- https://stackoverflow.com/questions/22677070/additional-field-while-serializing-django-rest-framework
- https://qiita.com/hayato1130/items/f4e84ef9ec3abb5e453c
- https://www.django-rest-framework.org/api-guide/filtering/
- https://nmomos.com/tips/2019/07/18/django-vuejs-2/

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
python manage.py createsuperuser
python manage.py collectstatic
python manage.py runserver
```

## nodejsのインストール
```
brew install nodebrew
nodebrew -v

// インストールできるNode.jsのバージョンの確認
nodebrew ls-remote

// ディレクトリの作成
mkdir -p ~/.nodebrew/src

// 安定版のNode.jsをインストール
nodebrew install-binary stable

// 使用できるNode.jsのバージョンを確認
nodebrew ls

// 使用するNode.jsのバージョンを指定
nodebrew use [インストールしたバージョン]

// nodeが使えるようにパスを通す
echo 'export PATH=$HOME/.nodebrew/current/bin:$PATH' >> ~/.zprofile

// 設定を反映させる
source ~/.zprofile

// Node.jsの実行確認
node -v
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
npm install axios --save
npm install sweetalert2 --save
npm install markdown-it-vue
npm run serve
```
