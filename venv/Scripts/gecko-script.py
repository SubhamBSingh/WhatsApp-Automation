#!C:\Users\subha\PycharmProjects\WhatsApp\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Gecko==1.0.19','console_scripts','gecko'
__requires__ = 'Gecko==1.0.19'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Gecko==1.0.19', 'console_scripts', 'gecko')()
    )
