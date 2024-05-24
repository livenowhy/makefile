## Superset 添加一个页面

### 1.  添加一个模型
    
    1.1 新增文件 superset/models/extend.py

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
    
    1.2 修改 superset/models/__init__.py 导入 extend

### 2. 添加视图

    2.1 新增视图文件 superset/views/extend.py
    
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

    2.2 修改 superset/views/__init__.py 导入 extend

### 3. 添加视图到

    vim superset/initialization/__init__.py

    # add lzp
    from superset.views.extend import JupyterLabView
    appbuilder.add_view(
        JupyterLabView,
        "jupyterlab",
        label=__("Jupyterhub"),
        href="/jupyterlabview/jupyterlab",
        icon='fa-cogs',
        category = "SQL Lab",
        category_label = __("SQL Lab"),
    )

### 4. 添加 html 文件
    
    superset/templates/jupyterlab.html

### 5. 添加jupyterlab 配置文件 ( jupyter_lab_config.py )

    $ jupyter lab --generate-config  (生成 jupyter_lab_config.py 文件，之后修改)
    # jupyter lab --allow-root  --ip 0.0.0.0 (一般启动命令)

    # mkdir /usr/local/lib/python3.10/site-packages/superset/jupyterlab/
    # cp jupyter_lab_config.py /usr/local/lib/python3.10/site-packages/superset/jupyterlab/jupyter_lab_config.py

### 6. 更改数据库

    $ superset db migrate
    $ superset db upgrade
    $ superset init        # 更新权限

### 7. 启动 jupyterlab

    $ jupyter lab --allow-root  --ServerApp.tornado_settings='{"headers":{"Content-Security-Policy":"frame-ancestors self *; report-uri /api/security/csp-report"}}' --allow-root --no-browser --ip=0.0.0.0 --port=8888 --ServerApp.token='' --ServerApp.password='' --ServerApp.quit_button=False

### 8. 参看
    
    # https://blog.csdn.net/qq_45957580/article/details/122496670
