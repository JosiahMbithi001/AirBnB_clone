#!/usr/bin/python3
""" unique FileStorage instance"""

from models.engine.file_storage import FileStorage

classes = {'BaseModel': 'BaseModel'}

storage = FileStorage()
storage.reload()
