## 配置

### 1、安装插件管理器(vim-plug)
    
    https://github.com/junegunn/vim-plug
    $ wget https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    $ mkdit ~/.vim/autoload/
    $ cp plug.vim ~/.vim/autoload/.

    或者
    $ curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

    $ cp vimrc ~/.vimrc


### 特殊插件说明
    
    1、vim-isort (Vim plugin to sort python imports using, 导入进行排序)
    
    # pip install isort
    Plug 'fisadev/vim-isort'
    https://github.com/fisadev/vim-isort


### 问题

    1、requires Vim compiled with Python (3.8.0+) support
    $ brew install macvim