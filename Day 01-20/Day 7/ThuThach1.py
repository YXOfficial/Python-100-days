import os
import time

def freefire():
    content = 'Free fire sống dai thành huyền thoại…………'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
if __name__ == '__main__':
    freefire()