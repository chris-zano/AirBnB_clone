#!/usr/bin/python3
"""
This is the __init__.py file of the models module
This instantiates an object of the FileStorage class
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
