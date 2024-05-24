
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


config = app.config
custom_password_store = config["SQLALCHEMY_CUSTOM_PASSWORD_STORE"]
stats_logger = config["STATS_LOGGER"]
log_query = config["QUERY_LOGGER"]
metadata = Model.metadata  # pylint: disable=no-member
logger = logging.getLogger(__name__)

# jupyterlab
class JupyterLabModel(Model):
    __tablename__ = 'jupyterlab'
    type = "table"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=True)
    info = Column(String(256), nullable=True)