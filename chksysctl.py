#!/usr/bin python3
# -*- coding: utf-8 -*-

#引数にSystemctlのステータスを表示したいものを入れると返してくれる

import subprocess
from subprocess import PIPE
import time
import sys
args = sys.argv

def main():
    try:
        #################### メイン処理 ####################
        
        proc = subprocess.run("sudo systemctl status " + args[1], shell=True, stdout=PIPE, stderr=PIPE, text=True)
        status = proc.stdout
        #print(status)
        l = status.splitlines()[4]
        print("Status of " + args[1] + ": "+ l[11:])
        #print('STDOUT: {}'.format(status))
        
        
        
    except KeyboardInterrupt:
        pass
    finally:
        pass
if __name__ == '__main__':
    main()
        