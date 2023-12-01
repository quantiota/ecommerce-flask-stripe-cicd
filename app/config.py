# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    DEBUG = (os.getenv('DEBUG', 'False') == 'True')

    # App Config - the minimal footprint
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_9999')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets') 

    # Mail Settings
    MAIL_SERVER   = os.getenv('MAIL_SERVER', 'server195.web-hosting.com')
    MAIL_PORT     = os.getenv('MAIL_PORT', '465')

    # Mail Authentication
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'amazonkdp@binomatrix.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'oi5c]Y~&Z{3NlGXPCG')
    MAIL_USE_SSL = True

    # Mail Accounts
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'amazonkdp@binomatrix.com')

    STRIPE_SECRET_KEY      = os.getenv('STRIPE_SECRET_KEY'     , None )
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', None )
    SERVER_ADDRESS         = os.getenv('SERVER_ADDRESS', 'http://localhost:5000/')

    STRIPE_IS_ACTIVE = False
    if STRIPE_SECRET_KEY and STRIPE_PUBLISHABLE_KEY:
        STRIPE_IS_ACTIVE = True
