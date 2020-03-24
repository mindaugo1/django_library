
#__init__.py file
import pymysql

pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()


#settings.py file
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gf',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '8889'
    }
}
