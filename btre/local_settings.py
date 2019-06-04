SECRET_KEY = 'h6-(!q&^9!#t(u%9$r79a+=s^e(4)5v8+i4_%w$#e04dgmb@$h'

DEBUG = False

ALLOWED_HOSTS = ['46.101.172.145']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btre_prod',
        'USER': 'postgres',
        'PASSWORD': 'qwe123',
        'HOST': 'localhost'
    }
}
