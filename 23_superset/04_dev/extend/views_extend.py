# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=invalid-name
from __future__ import annotations

from flask_appbuilder import expose
from flask_appbuilder.models.sqla.interface import SQLAInterface

from superset.views.base import (
    DeleteMixin,         # add lzp
    SupersetModelView    # add lzp
)

from superset.models.extend import JupyterLabModel


class JupyterLabView(SupersetModelView, DeleteMixin):
    datamodel = SQLAInterface(JupyterLabModel)
    label_columns = {'name':'Name', 'info':'Info'}
    list_columns = ['name', 'Name']

    @expose('/jupyterlab')
    def jupyter(self):
        return self.render_template('jupyterlab.html')