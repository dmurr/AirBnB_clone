#!/usr/bin/python3
import cmd
from datetime import datetime
from uuid4 import uuid
"""
module
"""

class BaseClass():
    """ Parent of all other classes """

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
