
set termguicolors
let g:onedark_termcolors=256
let g:onedark_hide_endofbuffer=1
colorscheme onedark 
"colorscheme space-vim-dark
"hi Normal     ctermbg=NONE guibg=NONE
"hi LineNr     ctermbg=NONE guibg=NONE
"hi SignColumn ctermbg=NONE guibg=NONE
"hi Comment guifg=#5C6370 ctermfg=59 cterm=italic
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
