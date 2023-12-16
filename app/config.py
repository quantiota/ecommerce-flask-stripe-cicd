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

    STRIPE_SECRET_KEY      = os.getenv('STRIPE_SECRET_KEY'     , None )
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', None )
    SERVER_ADDRESS         = os.getenv('SERVER_ADDRESS', 'http://localhost:5000/')

    STRIPE_IS_ACTIVE = False
    if STRIPE_SECRET_KEY and STRIPE_PUBLISHABLE_KEY:
        STRIPE_IS_ACTIVE = True

    #######################################
    # Flask-Mail configuration for contact form

   # Mail Settings
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 465))  # Default to 587 if not set

    # Mail Authentication
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False') == 'False'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False') == 'True'

    # Mail Accounts
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')


