from pathlib        import Path #기존에 settings.py 에 있는 코드
from my_settings    import DATABASES, SECRET_KEY

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NAME',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
				'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = 'django-insecure-a7+&#mqz!(mpx_9+2740*y#)&sz1*-eui)kq)jzm8*=fc*_wt$'


