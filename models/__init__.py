#!/usr/bin/python3
"""package declaration file __init__"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
