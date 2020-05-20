#! python3

PASSWORDS = {   
                'luggage':'12346'
            }

import sys,pyperclip
if len(sys.argv) < 1:
    print('Usage:python sys1.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] 

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(pyperclip.paste())
else:
    print('no account')