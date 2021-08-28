django-cors-headersのインストール
settings.pyの編集
INSTALLD_APPS
MIDDLEWARE
CORS_ORIGIN_WHITELIST
参考

(venv)$ pip install django-cors-headers
settings.pyの編集
INSTALLD_APPS
corsheadersを追加します。


INSTALLED_APPS = [
    ・・・
    'rest_framework',
    'api',
    'corsheaders', # ここに追加
　　・・・
]
MIDDLEWARE
corsheaders.middleware.CorsMiddlewareを追記します。


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # ここに追加
    'django.middleware.security.SecurityMiddleware',
    ・・・
]
CORS_ORIGIN_WHITELIST
CORS_ORIGIN_WHITELISTを追加し、フロントエンドで通信したいURLを記入します。


CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000', # ここに追加
]
