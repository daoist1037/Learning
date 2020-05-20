import shelve, sys, pyperclip
mcbself = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbself[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(mcbself.keys())))
        print(str(list(mcbself.keys())))
        print(mcbself.keys())
    elif sys.argv[1] in mcbself:
        pyperclip.copy(mcbself[sys.argv[1]])


mcbself.close()