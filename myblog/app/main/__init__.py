from flask import Blueprint
main=Blueprint("main",__name__)

from myblog.app.main import views
