# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 04:06
from __future__ import unicode_literals

from django.db import migrations

openeats_navbar = [
    {
        "pk": 1,
        "name": "about",
        "parent": None,
        "title": "about",
        "url": "/about/",
        "user_type": "E",
        # "groups": [],
        "path_type": "P",
        "order": 5,
        "lft": 1,
        "rght": 2,
        "tree_id": 1,
        "level": 0
    },
    {
        "pk": 2,
        "name": "create",
        "parent": None,
        "title": "new recipe",
        "url": "/recipe/new/",
        "user_type": "L",
        # "groups": [],
        "path_type": "P",
        "order": 1,
        "order": 0,
        "lft": 1,
        "rght": 2,
        "tree_id": 1,
        "level": 0
    },
    {
        "pk": 3,
        "parent": None,
        "name": "home",
        "slug": "home",
        "title": "home",
        "url": "/recipe/",
        "active": True,
        "user_type": "E",
        # "groups": [],
        "path_type": "P",
        "order": 0,
        "lft": 1,
        "rght": 2,
        "tree_id": 1,
        "level": 0
    },
    {
        "pk": 4,
        "name": "sign in",
        "parent": None,
        "title": "sign in",
        "url": "/accounts/signIn/",
        "user_type": "A",
        # "groups": [],
        "path_type": "P",
        "order": 3,
        "lft": 1,
        "rght": 2,
        "tree_id": 1,
        "level": 0
    },
    {
        "pk": 6,
        "name": "news",
        "parent": None,
        "title": "development blog",
        "url": "/news/list/",
        "user_type": "E",
        # "groups": [],
        "path_type": "P",
        "order": 6,
        "lft": 1,
        "rght": 2,
        "tree_id": 1,
        "level": 0     
    },
    {
        "pk": 7,
        "name": "blog",
        "parent": None,
        "title": "development blog",
        "url": "http://dev.openeats.org",
        "user_type": "E",
        # "groups": [],
        "path_type": "P",
        "order": 6,
        "lft": 1,
        "rght": 2,
        "tree_id": 1,
        "level": 0
    },
    {
        "pk": 8,
        "name": "admin",
        "parent": None,
        "title": "admin",
        "url": "/admin/",
        "user_type": "X",
        # "groups": [],
        "path_type": "P",
        "order": 6,
        "lft": 1,
        "rght": 2,
        "tree_id": 1,
        "level": 0
#    },
#    {
#         "pk": 1,
#         "registration_required": False,
#         "title": "about",
#         "url": "/about/",
#         "template_name": "flatpages/about_page.html",
#         "sites": [
#             1
#         ],
#        "content": "<div class=\"about\">\r\n<h2>About OpenEats</h2>\r\n<p>OpenEats is an Open Source, recipe management web application. &nbsp;Using OpenEats you can store, share and catalogue your favorite recipes.</p>\r\n<h3>Features</h3>\r\n<ul>\r\n<li> \r\n<ul>\r\n<li>100% OpenSource you can download the software and run it on your own server or create an account at&nbsp;<a href=\"http://www.openeats.org/\">OpenEats</a></li>\r\n<li>Internationalization Support</li>\r\n<li>Recipe Sharing</li>\r\n<li>Recipe Ranking</li>\r\n<li>UTF-8 compliant</li>\r\n<li>Versioning of Recipes</li>\r\n<li>Share or mark recipes private</li>\r\n<li>Built in <a href=\"http://en.gravatar.com/\">Gravatar</a>&nbsp;Support</li>\r\n<li>Friend fellow chef's and follow them</li>\r\n<li>Tagging of recipes</li>\r\n<li>WYSIWYG Editor for recipes</li>\r\n<li>Print View</li>\r\n<li>Cooking view for recipes so you can have a large pop up view of the recipe you are working on and look at it while in the kitchen</li>\r\n<li>Security - preventing XSS attacks and CSRF attacks</li>\r\n<li>Grocery list so you can make sure you always have what you need to make the meals you want</li>\r\n</ul>\r\n</li>\r\n</ul>\r\n</div>",
#        "enable_comments": False,
#        "lft": 1,
#        "rght": 2,
#        "tree_id": 1,
#        "level": 0        
     }
]


def add_navbar(apps, schema_editor):
    navbarentry = apps.get_model("navbar", "navbarentry")
    for entry in openeats_navbar:
        record = navbarentry(**entry)
        record.save()

class Migration(migrations.Migration):

    dependencies = [
        ('openeats', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_navbar)
    ]
