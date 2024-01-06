## 配置

### 1、安装插件管理器(vim-plug)
    
    https://github.com/junegunn/vim-plug
    $ wget https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    $ mkdit ~/.vim/autoload/
    $ cp plug.vim ~/.vim/autoload/.

    或者
    $ curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

    cp vimrc ~/.vimrc

## plug

    1、A tree explorer plugin for vim.
    Plug 'preservim/nerdtree'
    git clone git@github.com:preservim/nerdtree.git

    2、Vim plugin that displays tags in a window, ordered by scope
    Plug 'majutsushi/tagbar'
    git clone git@github.com:preservim/tagbar.git

    3、lean & mean status/tabline for vim that's light as air
    Plug 'vim-airline/vim-airline'
    git clone git@github.com:vim-airline/vim-airline.git

    4、A collection of themes for vim-airline
    Plug 'vim-airline/vim-airline-themes'
    git clone git@github.com:vim-airline/vim-airline-themes.git

call plug#begin()

Plug 'preservim/nerdtree'
Plug 'majutsushi/tagbar'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Using a tagged release; wildcard allowed (requires git 1.9.2 or above)
Plug 'fatih/vim-go', { 'tag': '*' }

Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'ycm-core/YouCompleteMe'
let g:ycm_server_keep_logfiles = 1
let g:ycm_server_log_level = 'debug'
Plug 'w0rp/ale'
Plug 'uber/prototool', { 'rtp':'vim/prototool' }
"Plug 'psf/black', { 'branch': 'stable' }

Plug 'google/vim-maktaba'
Plug 'google/vim-codefmt'
Plug 'google/vim-glaive'
Plug 'fisadev/vim-isort'

Plug 'jceb/vim-orgmode'

call plug#end()