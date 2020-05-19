runtime! debian.vim
if has("syntax")
  syntax on
endif
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif
"--------------------------基本配置
set number	"显示行号
set relativenumber	"显示相对行号·
set cursorline	"高亮当前行
set cursorcolumn	"高亮当前列
syntax on		"语法高亮
syntax enable
filetype on	"侦测文件类型
filetype indent on		"开启文件类型检查，并且载入与该类型对应的缩进规则
filetype plugin on           "针对不同的文件类型加载对应的插件
filetype plugin indent on    " 启用自动补全
set showmode	"在底部显示，当前处于命令模式还是插入模式
set showcmd		"命令模式下，在底部显示，当前键入的指令
set mouse=a		"支持使用鼠标
set t_Co=256		"启用256色
set autoindent	"按下回车键后，下一行的缩进会自动跟上一行的缩进保持一致
set tabstop=2		"按下 Tab 键时，Vim 显示的空格数
set shiftwidth=4	"在文本上按下>>（增加一级缩进）、<<（取消一级缩进）或者==（取消全部缩进）时，每一级的字符数
set expandtab			"由于 Tab 键在不同的编辑器缩进不一致，该设置自动将 Tab 转为空格
set textwidth=80	"一行80个字符
set wrap				"自动折行，即太长的行分成几行显示
set linebreak		"只有遇到指定的符号（比如空格、连词号和其他标点符号），才发生折行。也就是说，不会在单词内部折行
set wrapmargin=2	"指定折行处与编辑窗口的右边缘之间空出的字符数
set scrolloff=5		"垂直滚动时，光标距离顶部/底部的位置（单位：行）
set sidescrolloff=15	"水平滚动时，光标距离行首或行尾的位置（单位：字符）。该配置在不折行时比较有用
set laststatus=2			" 总显示最后一个窗口的状态行；设为1则窗口数多于一个的时候显示最后一个窗口的状态行；0不显示最后一个窗口的状态行"
set ruler							"在状态栏显示光标的当前位置（位于哪一行哪一列）
set showmatch					"光标遇到圆括号、方括号、大括号时，自动高亮对应的另一个圆括号、方括号和大括号
set showtabline=2			"总是显示标签栏"
set hlsearch					"搜索时，高亮显示匹配结果
set ignorecase				"搜索忽略大小写
"set spell spelllang=en_us		"打开英语单词的拼写检查
set nobackup				"不创建备份文件。默认情况下，文件保存时，会额外创建一个备份文件，它的文件名是在原文件名的末尾，再添加一个波浪号（〜）
set noswapfile
set helplang=cn                " 中文文档"
set nocompatible			"设置不兼容vi
set encoding=utf-8		"使用 utf-8 编码
set fenc=utf-8
set fileencodings=utf-8,gbk,cp936,latin-1
set fileformat=unix
set fileformats=unix,mac,dos
set completeopt=preview   
"set omnifunc=syntaxcomplete#Complete
set backupdir=~/.local/.vim/.backup//	"设置备份文件、交换文件、操作历史文件的保存位置
"set directory=~/.local/.vim/.swp//
"set undodir=~/.local/.vim/.undo//
set autochdir		"自动切换工作目录。这主要用在一个 Vim 会话之中打开多个文件的情况，默认的工作目录是打开的第一个文件的目录。该配置可以将工作目录自动切换到，正在编辑的文件的目录。
set autoread		"打开文件监视。如果在编辑过程中文件发生外部改变（比如被别的编辑器编辑了），就会发出提示。
set wildmenu		"命令模式下，底部操作指令按下 Tab 键自动补全。第一次按下 Tab，会显示所有匹配的操作指令的清单；第二次按下 Tab，会依次选择各个指令。

"-------------------------vim 三种模式下光标样式
set gcr=n-v-c:ver25-Cursor/lCursor,ve:ver35-Cursor,o:hor50-Cursor,i-ci:ver25-Cursor/lCursor,r:hor50-Cursor/lCursor
"-----------------------------重新打开一个文件时跳到上一次编辑的地方
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif
"-------------------------python3路径
let g:python3_host_prog="/usr/bin/python3"
"-----------------------------插件管理
call plug#begin('/home/dd/.local/vim/plugged')
"文件管理
"Plug 'preservim/nerdtree'
"Plug 'vim-airline/vim-airline'
"Plug 'vim-airline/vim-airline-themes'
Plug 'itchyny/lightline.vim'
Plug 'bling/vim-bufferline'
"snippets
Plug 'honza/vim-snippets'
"Plug 'SirVer/ultisnips'
"彩虹括号
Plug 'kien/rainbow_parentheses.vim'
"成对括号
Plug 'tpope/vim-surround'
"快速移动
Plug 'easymotion/vim-easymotion'
"启动界面
Plug 'mhinz/vim-startify'
"大纲浏览
"Plug 'majutsushi/tagbar'
"快速查找
Plug 'Yggdroot/LeaderF', { 'do': './install.sh'  }
"快速注释
Plug 'scrooloose/nerdcommenter'
"缩进条
Plug 'yggdroot/indentline'
"solarized主题
Plug 'altercation/vim-colors-solarized'
"One主题
Plug 'joshdick/onedark.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'liuchengxu/space-vim-dark'
Plug 'tomasr/molokai'
"括号补全
Plug 'jiangmiao/auto-pairs'
"高亮复制区域
Plug 'machakann/vim-highlightedyank'
"markdown预览
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install()  }, 'for':['markdown','vim-plug']  }
Plug 'godlygeek/tabular',{'for':['markdown','vim-plug']}
"Plug 'plasticboy/vim-markdown', {'for':['markdown','vim-plug']}
Plug 'dhruvasagar/vim-table-mode',{'for':['markdown','vim-plug']}
Plug 'dkarter/bullets.vim',{'for':['markdown','vim-plug']}
"代码补全
Plug 'neoclide/coc.nvim', {'branch': 'release'}
"Plug 'python-mode/python-mode', { 'for': 'python', 'branch': 'develop' }
call plug#end()
"------------------Leaderf 设置
" don't show the help in normal mode
let g:Lf_HideHelp = 1
let g:Lf_UseCache = 0
let g:Lf_UseVersionControlTool = 0
let g:Lf_IgnoreCurrentBufferName = 1
" popup mode
let g:Lf_WindowPosition = 'popup'
let g:Lf_PreviewInPopup = 1
let g:Lf_StlSeparator = { 'left': "\ue0b0", 'right': "\ue0b2" }
let g:Lf_PreviewResult = {'Function': 0, 'BufTag': 0 }
let g:Lf_ShortcutF = "<leader>ff"
noremap <leader>fb :<C-U><C-R>=printf("Leaderf buffer %s", "")<CR><CR>
noremap <leader>fm :<C-U><C-R>=printf("Leaderf mru %s", "")<CR><CR>
noremap <leader>ft :<C-U><C-R>=printf("Leaderf bufTag %s", "")<CR><CR>
noremap <leader>fl :<C-U><C-R>=printf("Leaderf line %s", "")<CR><CR>
noremap <C-B> :<C-U><C-R>=printf("Leaderf! rg --current-buffer -e %s ", expand("<cword>"))<CR>
noremap <C-F> :<C-U><C-R>=printf("Leaderf! rg -e %s ", expand("<cword>"))<CR>
" search visually selected text literally
xnoremap gf :<C-U><C-R>=printf("Leaderf! rg -F -e %s ", leaderf#Rg#visual())<CR>
noremap go :<C-U>Leaderf! rg --recall<CR>
" should use `Leaderf gtags --update` first
let g:Lf_GtagsAutoGenerate = 0
let g:Lf_Gtagslabel = 'native-pygments'
noremap <leader>fr :<C-U><C-R>=printf("Leaderf! gtags -r %s --auto-jump", expand("<cword>"))<CR><CR>
noremap <leader>fd :<C-U><C-R>=printf("Leaderf! gtags -d %s --auto-jump", expand("<cword>"))<CR><CR>
noremap <leader>fo :<C-U><C-R>=printf("Leaderf! gtags --recall %s", "")<CR><CR>
noremap <leader>fn :<C-U><C-R>=printf("Leaderf gtags --next %s", "")<CR><CR>
noremap <leader>fp :<C-U><C-R>=printf("Leaderf gtags --previous %s", "")<CR><CR>
"----------------onedark设置
set termguicolors
let g:onedark_termcolors=256
let g:onedark_hide_endofbuffer=1
"colorscheme solarized 
colorscheme onedark 
"colorscheme space-vim-dark
hi Normal     ctermbg=NONE guibg=NONE
hi LineNr     ctermbg=NONE guibg=NONE
hi SignColumn ctermbg=NONE guibg=NONE
hi Comment guifg=#5C6370 ctermfg=59 cterm=italic
"set background=dark
let g:lightline = {
    \ 'colorscheme': 'one',
    \ 'active': {
    \   'left': [ [ 'mode', 'paste' ],
    \             [ 'gitbranch', 'readonly', 'filename', 'modified', 'helloworld' ] ],
    \   'right': [ [ 'lineinfo' ],
    \              [ 'percent' ],
    \              [ 'fileformat', 'fileencoding', 'filetype' ] ]
    \ },
    \ 'component': {
    \   'helloworld': 'Hello, daoist!'
    \ },
    \ 'component_function': {
    \   'gitbranch': 'fugitive#head',
    \   'filename': 'LightlineFilename'
    \ },
    \ }
function! LightlineFilename()
    let filename = expand('%:t') !=# '' ? expand('%:t') : '[No Name]'
    "let modified = &modified ? ' +' : ''
    "return filename . modified
    return filename 
endfunction
"------------------------F5 一键编译运行（不允许输入）
func! CompileRunGcc()
    exec"w!"
    if &filetype =='c'
        exec"!g++ % -o %<"
        exec"!time ./%<"
    elseif &filetype =='cpp'
        exec":!g++ % -o %<"
		exec":call OpenFloatingWin()"
        exec":term time ./#<" 
    elseif &filetype =='java'
        exec"!javac %"
        exec"!time java %<"
    elseif &filetype =='python'
		exec":call OpenFloatingWin()"
        exec ":term time python3 ./#"
    elseif &filetype =='go'
        exec"!go build %<"
        exec"!time go run %"
	elseif &filetype =='markdown'
		exec "MarkdownPreview"
    endif
endfunc
"------------------------markdown-preview设置
let g:mkdp_path_to_chrome = "/mnt/c/Program\ Files\ (x86)/Google/Chrome/Application"
"--------------------------自动写入文件头
autocmd BufNewFile *.cpp,*.[ch],*.sh,*.py,*.html,*.php,*java exec ":call SetTitle()"
func SetTitle()
		if &filetype=='python'
				call setline(1, "#!/usr/bin/python3")
				call append(line("."), "#-*- encoding: UTF-8 -*-")
		endif
		if &filetype=='cpp'
				call setline(1, "/*************************************************************************")
				call append(line("."), "      > File Name: ".expand("%"))
				call append(line(".")+1, "      > Author: daoist")
				call append(line(".")+2, "      > Mail: @qq.com")
				call append(line(".")+3, "      > Created Time: ".strftime("%c"))
				call append(line(".")+4, "      > Last changed: TIMESTAMP")
				call append(line(".")+5, " ************************************************************************/")
				call append(line(".")+6, "#include<iostream>")
				call append(line(".")+7, "using namespace std;")
				call append(line(".")+8, "")
		endif
		if &filetype=='c'
				call setline(1, "/*************************************************************************")
				call append(line("."), "      > File Name: ".expand("%"))
				call append(line(".")+1, "      > Author: daoist")
				call append(line(".")+2, "      > Mail: @qq.com")
				call append(line(".")+3, "      > Created Time: ".strftime("%c"))
				call append(line(".")+4, "      > Last changed: TIMESTAMP")
				call append(line(".")+5, " ************************************************************************/")
				call append(line(".")+6, "#include<stdio.h>")
				call append(line(".")+7, "")
		endif
endfunc
autocmd BufNewFile * normal G "新建文件后，自动定位到文件末尾"
"--------------------------浮动窗口
function! OpenFloatingWin()
		let height = &lines - 3
		let width = float2nr(&columns - (&columns * 2 / 10))
		let col = float2nr((&columns - width) / 2)
		" 设置浮动窗口打开的位置，大小等。
		" 这里的大小配置可能不是那么的 flexible 有继续改进的空间
		let opts = {
				\ 'relative': 'editor',
				\ 'row': height * 0.3,
				\ 'col': col + 30,
				\ 'width': width * 2 / 3,
				\ 'height': height / 2
				\ }
		let buf = nvim_create_buf(v:false, v:true)
		let win = nvim_open_win(buf, v:true, opts)
		" 设置浮动窗口高亮
		call setwinvar(win, '&winhl', 'Normal:Pmenu')
		setlocal 
				\ buftype=nofile
				\ nobuflisted
				\ bufhidden=hide
				\ nonumber
				\ norelativenumber
				\ signcolumn=no
endfunction
function! OpenFloatWin2()
        let buf = nvim_create_buf(v:false, v:true)
        call nvim_buf_set_lines(buf, 0, -1, v:true, ["test", "text"])
				
				let height = &lines - 3
				let width = float2nr(&columns - (&columns * 2 / 10))
				let col = float2nr((&columns - width) / 2)
        
				let opts = {
						\ 'relative': 'editor',
						\ 'row': height * 0.3,
						\ 'col': col + 30,
						\ 'width': width * 2 / 3,
						\ 'height': height / 2,
						\ 'anchor': 'NW'
						\ }
        "hi def NvimFloatingWindow guibg=NONE ctermbg=NONE 
        let win = nvim_open_win(buf, v:true, opts)
        " optional: change highlight, otherwise Pmenu is used
        call nvim_win_set_option(win, 'winhl','Normal:Pmenu' )
        exec"term"
        exec"startinsert"
endfunction
"----------------------cocnvim配置
" TextEdit might fail if hidden is not set.
set hidden

" Some servers have issues with backup files, see #649.
set nobackup
set nowritebackup

" Give more space for displaying messages.
set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved.
set signcolumn=yes

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current
" position. Coc only does snippet and additional edit on confirm.
" <cr> could be remapped by other vim plugin, try `:verbose imap <CR>`.
if exists('*complete_info')
  inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"
else
  inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
endif

" Use `[g` and `]g` to navigate diagnostics
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  else
    call CocAction('doHover')
  endif
endfunction

" Highlight the symbol and its references when holding the cursor.
autocmd CursorHold * silent call CocActionAsync('highlight')

" Symbol renaming.
nmap <leader>rn <Plug>(coc-rename)

" Formatting selected code.
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s).
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder.
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Applying codeAction to the selected region.
" Example: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap keys for applying codeAction to the current line.
nmap <leader>ac  <Plug>(coc-codeaction)
" Apply AutoFix to problem on the current line.
nmap <leader>qf  <Plug>(coc-fix-current)

" Map function and class text objects
" NOTE: Requires 'textDocument.documentSymbol' support from the language server.
xmap if <Plug>(coc-funcobj-i)
omap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap af <Plug>(coc-funcobj-a)
xmap ic <Plug>(coc-classobj-i)
omap ic <Plug>(coc-classobj-i)
xmap ac <Plug>(coc-classobj-a)
omap ac <Plug>(coc-classobj-a)

" Use CTRL-S for selections ranges.
" Requires 'textDocument/selectionRange' support of LS, ex: coc-tsserver
nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

" Add `:Format` command to format current buffer.
command! -nargs=0 Format :call CocAction('format')

" Add `:Fold` command to fold current buffer.
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Add `:OR` command for organize imports of the current buffer.
command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

" Add (Neo)Vim's native statusline support.
" NOTE: Please see `:h coc-status` for integrations with external plugins that
" provide custom statusline: lightline.vim, vim-airline.
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

" Mappings using CoCList:
" Show all diagnostics.
nnoremap <silent> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions.
nnoremap <silent> <space>e  :<C-u>CocList extensions<cr>
" Show commands.
nnoremap <silent> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document.
nnoremap <silent> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols.
nnoremap <silent> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list.
nnoremap <silent> <space>p  :<C-u>CocListResume<CR>
"---------------------------MarkdownPreview
let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 1
let g:mkdp_refresh_slow = 0
let g:mkdp_command_for_global = 0
let g:mkdp_open_to_the_world = 0
let g:mkdp_open_ip = ''
let g:mkdp_echo_preview_url = 0
let g:mkdp_browserfunc = ''
let g:mkdp_preview_options = {
			\ 'mkit': {},
			\ 'katex': {},
			\ 'uml': {},
			\ 'maid': {},
			\ 'disable_sync_scroll': 0,
			\ 'sync_scroll_type': 'middle',
			\ 'hide_yaml_meta': 1
			\ }
let g:mkdp_markdown_css = ''
let g:mkdp_highlight_css = ''
let g:mkdp_port = ''
let g:mkdp_page_title = '「${name}」'
autocmd Filetype markdown inoremap <buffer> ,, <++>
autocmd Filetype markdown inoremap <buffer> ,f <Esc>/<++><CR>:nohlsearch<CR>"_c4l
autocmd Filetype markdown inoremap <buffer> ,w <Esc>/ <++><CR>:nohlsearch<CR>"_c5l<CR>
autocmd Filetype markdown inoremap <buffer> ,n ---<Enter><Enter>
autocmd Filetype markdown inoremap <buffer> ,b **** <++><Esc>F*hi
autocmd Filetype markdown inoremap <buffer> ,s ~~~~ <++><Esc>F~hi
autocmd Filetype markdown inoremap <buffer> ,i ** <++><Esc>F*i
autocmd Filetype markdown inoremap <buffer> ,d `` <++><Esc>F`i
autocmd Filetype markdown inoremap <buffer> ,c ```<Enter><++><Enter>```<Enter><Enter><++><Esc>4kA
autocmd Filetype markdown inoremap <buffer> ,m - [ ] 
autocmd Filetype markdown inoremap <buffer> ,p ![](<++>) <++><Esc>F[a
autocmd Filetype markdown inoremap <buffer> ,a [](<++>) <++><Esc>F[a
autocmd Filetype markdown inoremap <buffer> ,1 #<Space><Enter><++><Esc>kA
autocmd Filetype markdown inoremap <buffer> ,2 ##<Space><Enter><++><Esc>kA
autocmd Filetype markdown inoremap <buffer> ,3 ###<Space><Enter><++><Esc>kA
autocmd Filetype markdown inoremap <buffer> ,4 ####<Space><Enter><++><Esc>kA
autocmd Filetype markdown inoremap <buffer> ,l --------<Enter>

function! s:isAtStartOfLine(mapping)
  let text_before_cursor = getline('.')[0 : col('.')-1]
  let mapping_pattern = '\V' . escape(a:mapping, '\')
  let comment_pattern = '\V' . escape(substitute(&l:commentstring, '%s.*$', '', ''), '\')
  return (text_before_cursor =~? '^' . ('\v(' . comment_pattern . '\v)?') . '\s*\v' . mapping_pattern . '\v$')
endfunction

inoreabbrev <expr> <bar><bar>
          \ <SID>isAtStartOfLine('\|\|') ?
          \ '<c-o>:TableModeEnable<cr><bar><space><bar><left><left>' : '<bar><bar>'
inoreabbrev <expr> __
          \ <SID>isAtStartOfLine('__') ?
          \ '<c-o>:silent! TableModeDisable<cr>' : '__'
"----------------------快捷键映射
map <F5> :call CompileRunGcc()<CR>
nnoremap fw :w!<CR>
nnoremap fq :q!<CR>
nnoremap fwq :wq!<CR>
nnoremap fe :NERDTree<CR>
nnoremap fs :source ~/.config/nvim/init.vim<CR>
"				\ci				注释
"				\\w				easymotion
"
