" All system-wide defaults are set in $VIMRUNTIME/debian.vim and sourced by
" the call to :runtime you can find below.  If you wish to change any of those
" settings, you should do it in this file (/etc/vim/vimrc), since debian.vim
" will be overwritten everytime an upgrade of the vim packages is performed.
" It is recommended to make changes after sourcing debian.vim since it alters
" the value of the 'compatible' option.

" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages available in Debian.
runtime! debian.vim

" Vim will load $VIMRUNTIME/defaults.vim if the user does not have a vimrc.
" This happens after /etc/vim/vimrc(.local) are loaded, so it will override
" any settings in these files.
" If you don't want that to happen, uncomment the below line to prevent
" defaults.vim from being loaded.
" let g:skip_defaults_vim = 1

" Uncomment the next line to make Vim more Vi-compatible
" NOTE: debian.vim sets 'nocompatible'.  Setting 'compatible' changes numerous
" options, so any other options should be set AFTER setting 'compatible'.
"set compatible

" Vim5 and later versions support syntax highlighting. Uncommenting the next
" line enables syntax highlighting by default.
if has("syntax")
  syntax on
endif

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
"set background=dark

" Uncomment the following to have Vim jump to the last position when
" reopening a file
"if has("autocmd")
"  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
"endif

" Uncomment the following to have Vim load indentation rules and plugins
" according to the detected filetype.
"if has("autocmd")
"  filetype plugin indent on
"endif

" The following are commented out as they cause vim to behave a lot
" differently from regular Vi. They are highly recommended though.
"set showcmd		" Show (partial) command in status line.
"set showmatch		" Show matching brackets.
"set ignorecase		" Do case insensitive matching
"set smartcase		" Do smart case matching
"set incsearch		" Incremental search
"set autowrite		" Automatically save before commands like :next and :make
"set hidden		" Hide buffers when they are abandoned
"set mouse=a		" Enable mouse usage (all modes)

" Source a global configuration file if available
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif

set number	"显示行号
set relativenumber	"显示相对行号·
set cursorline	"高亮当前行
set cursorcolumn	"高亮当前列
syntax on		"语法高亮
set showmode	"在底部显示，当前处于命令模式还是插入模式
set showcmd		"命令模式下，在底部显示，当前键入的指令
set mouse=a		"支持使用鼠标
set encoding=utf-8		"使用 utf-8 编码
set t_Co=256		"启用256色
set autoindent	"按下回车键后，下一行的缩进会自动跟上一行的缩进保持一致
set tabstop=2		"按下 Tab 键时，Vim 显示的空格数
set shiftwidth=4	"在文本上按下>>（增加一级缩进）、<<（取消一级缩进）或者==（取消全部缩进）时，每一级的字符数
set textwidth=80	"一行80个字符
set wrap				"自动折行，即太长的行分成几行显示
set linebreak		"只有遇到指定的符号（比如空格、连词号和其他标点符号），才发生折行。也就是说，不会在单词内部折行
set wrapmargin=2	"指定折行处与编辑窗口的右边缘之间空出的字符数
set scrolloff=5		"垂直滚动时，光标距离顶部/底部的位置（单位：行）
set sidescrolloff=15	"水平滚动时，光标距离行首或行尾的位置（单位：字符）。该配置在不折行时比较有用
set laststatus=2			"水平滚动时，光标距离行首或行尾的位置（单位：字符）。该配置在不折行时比较有用
set ruler							"在状态栏显示光标的当前位置（位于哪一行哪一列）
set showmatch					"光标遇到圆括号、方括号、大括号时，自动高亮对应的另一个圆括号、方括号和大括号
set hlsearch					"搜索时，高亮显示匹配结果
set spell spelllang=en_us		"打开英语单词的拼写检查
set nobackup					
"不创建备份文件。默认情况下，文件保存时，会额外创建一个备份文件，它的文件名是在原文件名的末尾，再添加一个波浪号（〜）
set noswapfile

"set backupdir=~/.local/.vim/.backup//	"设置备份文件、交换文件、操作历史文件的保存位置
"set directory=~/.local/.vim/.swp//
"set undodir=~/.local/.vim/.undo//
set autochdir		"自动切换工作目录。这主要用在一个 Vim 会话之中打开多个文件的情况，默认的工作目录是打开的第一个文件的目录。该配置可以将工作目录自动切换到，正在编辑的文件的目录。
set autoread		"打开文件监视。如果在编辑过程中文件发生外部改变（比如被别的编辑器编辑了），就会发出提示。
set wildmenu		"命令模式下，底部操作指令按下 Tab 键自动补全。第一次按下 Tab，会显示所有匹配的操作指令的清单；第二次按下 Tab，会依次选择各个指令。
"set wildmode=longest:list,full

"SI = INSERT mode
"SR = REPLACE mode
"EI = NORMAL mode (ELSE)
"无效下面五行
"let &t_ti.="\e[0 q"
"let &t_SI.="\e[5 q"
"let &t_SR.="\e[5 q"
"let &t_EI.="\e[3 q"
"let &t_te.="\e[0 q"
"let &t_SI = 
""\<Esc>]50;CursorShape=5\x7"

"let &t_SR = 
""\<Esc>]50;CursorShape=2\x7"
"let &t_EI = 
""\<Esc>]50;CursorShape=0\x7"
"Cursor settings:

"  1 -> blinking block
"  2 -> solid block
"  3 -> blinking underscore
"  4 -> solid underscore
"  5 -> blinking vertical bar
"  6 -> solid vertical bar
"SI = INSERT mode
"SR = REPLACE mode
"EI = NORMAL mode (ELSE)
"
"
"
call plug#begin('/home/dd/.local/vim/plugged')
"文件管理
Plug 'preservim/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
"彩虹括号
Plug 'kien/rainbow_parentheses.vim'
"成对括号
Plug 'tpope/vim-surround'
"快速移动
Plug 'easymotion/vim-easymotion'
"启动界面
Plug 'mhinz/vim-startify'
"大纲浏览
Plug 'majutsushi/tagbar'
"快速注释
Plug 'scrooloose/nerdcommenter'
"缩进条
Plug 'yggdroot/indentline'
"solarized主题
"Plug 'altercation/solarized'
Plug 'altercation/vim-colors-solarized'
"括号u补全
Plug 'jiangmiao/auto-pairs'
"高亮复制区域
Plug 'machakann/vim-highlightedyank'
"代码片段
call plug#end()

syntax enable
let g:solarized_termcolors=256
set background=dark
colorscheme solarized
let g:airline_theme="onedark"

map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec"w!"
    if &filetype =='c'
        exec"!g++ % -o %<"
        exec"!time ./%<"
    elseif &filetype =='cpp'
        exec"!g++ % -o %<"
        exec"!time ./%<"
    elseif &filetype =='java'
        exec"!javac %"
        exec"!time java %<"
    elseif &filetype =='sh'
        :!time bash %
    elseif &filetype =='python'
        exec "!python3 %"
    elseif &filetype =='html'
        exec"!firefox % &"
    elseif &filetype =='go'
        exec"!go build %<"
        exec"!time go run %"
    endif
endfunc

nmap fw :w!<CR>
nmap fq :q!<CR>
nmap fwq :wq!<CR>
