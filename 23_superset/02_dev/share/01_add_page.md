## Superset 添加一个页面

### 1.  添加一个模型
    
    superset\models\extend.py

    # jupyterlab
    class JupyterLabModel(Model):
        __tablename__ = 'jupyterlab'
        type = "table"
        id = Column(Integer, primary_key=True)
        name = Column(String(256), nullable=True)
        info = Column(String(256), nullable=True)

    ExeclInfoAdd.__table__.create(db.engine, checkfirst=True)

### 2. 添加视图
    
    superset\views\extend.py
    
    class JupyterLabView(SupersetModelView, DeleteMixin):
        datamodel = SQLAInterface(JupyterLabModel)
        label_columns = {'name':'Name', 'info':'Info'}
        list_columns = ['name', 'Name']

        @expose('/jupyterlab')
        def jupyter(self):
            return self.render_template('jupyterlab.html')

### 3. 添加视图到

    vim superset/initialization/__init__.py

    # add lzp
    from superset.views.core import JupyterView
    appbuilder.add_view(
        JupyterView,
        "jupyter",
        label=__("Jupyterhub"),  # 修改为Jupyterhub
        # label=__("Jupyter Notebook"),
        href="/jupyterview/jupyter",
        icon='fa-cogs',
        category = "SQL Lab",
        category_label = __("SQL Lab"),
    )

### 4. 更改数据库

    $ superset db migrate
    $ superset db upgrade
    $ superset init        # 更新权限