"""database engine
"""
from mongoengine import connect

connect(db="db_bp", host='127.0.0.1', port=27017)
