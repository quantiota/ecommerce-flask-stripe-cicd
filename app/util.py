# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, fnmatch, json
from app import app 

class Product:
    id       = ''
    name     = ''
    price    = 0
    currency = ''
    tax_behavior = ''
    tax_code = ''
    info     = ''
    short_description = ''
    full_description = ''
    slug     = '' 
    img_main   = ''
    img_card = ''
    img_1 = ''
    img_2 = ''
    img_3 = ''

def get_templates_dir():
    return os.path.join(app.root_path, 'templates' )

def get_products_dir():
    return os.path.join(app.root_path, 'templates', 'products' )

def get_product_path( aSlug ):
    return os.path.join(app.root_path, 'templates', 'products', aSlug )

def get_files( aPath, ext='html' ):

    matches = []

    for root, dirnames, filenames in os.walk( aPath ):
        for filename in fnmatch.filter(filenames, '*.'+ ext):

            item = os.path.join(root, filename)

            #print ' **** type(item) = ' + str( type ( item ) )
            matches.append( item )

    return matches

def get_products( ):

    return get_files( get_products_dir(), 'json' )

def get_slug( aPath, aExt='json' ):

    if aPath:
        head, tail = os.path.split( aPath ) # get file name
        return tail.replace('.' + aExt, '') # remove extension

    return None

def load_json_product( aJSONPath ): 
    f = open(aJSONPath, 'r')
    if not f:
        return None   
    
    # Read Product Info    
    data = json.load( f )

    return data

def load_product( aJSONPath ): 
    f = open(aJSONPath, 'r')
    if not f:
        return None   
    
    # Read Product Info    
    data = json.load( f )
    
    if not data:
        return None 
    
    product = Product()

    product.name  = data["name"] 
    product.info  = data["info"]
    product.currency = data["currency"]
    product.price = int( float(data["price"]) )
    product.tax_behavior = data["tax_behavior"]
    product.tax_code = data["tax_code"]
    product.short_description = data["short_description"]
    product.full_description  = data["full_description"]
    product.slug  = get_slug( aJSONPath )
    try:
        product.img_main = data['img_main']
        product.img_card = data['img_card']
        product.img_1 = data['img_1']
        product.img_2 = data['img_2']
        product.img_3 = data['img_3']
        product.id = data['id']
    except:
        product.id = get_slug( aJSONPath )

    return product

def load_product_by_slug( aSlug ):

    aJSONPath = get_product_path( aSlug + '.json' )

    return load_product( aJSONPath )

def load_product_by_id( id ):
    aJSONPath = get_product_path( id + '.json' )
    return load_product( aJSONPath )
