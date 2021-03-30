# Django Settings

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'nacxoz%8qo$$l98supcyxh5&c7@5kue0uq_z9)_bui1(kp5xey'
DEBUG = True

MAGIC_MESSAGE = os.environ.get("MAGIC_MESSAGE")

ALLOWED_HOSTS = ['django', 'localhost']
INSTALLED_APPS = [
    'docker_demo'
]

ROOT_URLCONF = 'docker_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # 'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'docker_demo.wsgi.application'