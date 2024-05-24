
from __future__ import annotations

import builtins
import json
import logging

from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
)


# jupyterlab
class JupyterLabModel(Model):
    __tablename__ = 'jupyterlab'
    type = "table"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=True)
    info = Column(String(256), nullable=True)