import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes,re, os.path

class LinkGen:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKCYAN = '\033[96m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

        self.current_path = os.path.dirname(os.path.realpath(__file__))
        while True:
            print(f'''
{self.ENDC}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{self.ENDC}┃          {self.OKGREEN}Nitro Tool by {self.HEADER}sem#4774{self.ENDC}          ┃
{self.ENDC}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{self.ENDC}┃ [{self.HEADER}1{self.ENDC}] {self.OKGREEN}Generate codes{self.ENDC}                       ┃
{self.ENDC}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{self.ENDC}┃ [{self.HEADER}2{self.ENDC}] {self.OKGREEN}Check codes{self.ENDC}                          ┃
{self.ENDC}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{self.ENDC}┃ [{self.HEADER}3{self.ENDC}] {self.OKGREEN}Reset{self.ENDC}                                ┃
{self.ENDC}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{self.ENDC}┃ [{self.HEADER}4{self.ENDC}] {self.OKGREEN}Info{self.ENDC}                                 ┃
{self.ENDC}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{self.ENDC}┃ [{self.HEADER}5{self.ENDC}] {self.OKGREEN}Exit{self.ENDC}                                 ┃
{self.ENDC}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            ''')

            answer = input(f'[{self.HEADER}Nitro Tool{self.ENDC}]{self.OKGREEN} >{self.ENDC} ')
            if answer == '1':
                self.generate()

            elif answer == '2':
                self.check()

            elif answer == '3':
                self.clear()

            elif answer == '4':
                self.info()

            elif answer == '5':
                print(f'\n[{self.HEADER}+{self.ENDC}] Closing..{self.ENDC} ')
                break 

    def generate(self):
        count = 0
        self.generate = int(input(f'\n[{self.HEADER}+{self.ENDC}] Enter an amount{self.OKGREEN} >{self.ENDC} '))
        print('')

        while(int(count)<int(self.generate)):
            generated = "https://discord.gift/"+random.choice(string.ascii_letters + string.digits)+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
            f= open(self.current_path+"/"+str("codes")+str("")+".txt","a")
            f.write(generated[21:]+"\n")
            print(f'[{self.HEADER}Generated{self.ENDC}]{self.OKGREEN} >{self.ENDC} ' + generated)
            count+=1
            #print('')
        print('')
        print(f'[{self.HEADER}+{self.ENDC}] Added all codes to codes.txt{self.ENDC} ')

    def check(self):
        with open('codes.txt', 'r') as f:
            time.sleep(0.4)
            print(f'\n[{self.HEADER}+{self.ENDC}] Checking all codes in codes.txt{self.ENDC} ')
            time.sleep(0.8)
            print()
            lines = f.readlines()
            j = 1
            while j <= len(f'{self.generate}'):
                j += 1
                for i in lines:
                    url = 'https://discord.com/api/v8/entitlements/gift-codes/' + (i) + '?with_application=false&with_subscription_plan=true'
                    s = requests.session()
                    response = s.get(url)

                    if 'subscription_plan' in response.text:
                        print(f'[{self.OKGREEN}Valid{self.ENDC}]{self.OKGREEN} > ' + 'https://discord.gift/' + f'{(i)}')
                        break 

                    elif 'Access denied' in response.text:
                        print(f'[{self.FAIL}Connection error{self.ENDC}]{self.OKGREEN} >{self.ENDC} ' + 'Failed checking: ' + 'https://discord.gift/' + f'{(i)}')
                        continue 

                    else:
                        print(f'[{self.HEADER}Invalid{self.ENDC}]{self.OKGREEN} >{self.ENDC} ' + 'https://discord.gift/' + f'{(i)}'.strip())

            print(f'\n[{self.HEADER}+{self.ENDC}] Finished checking{self.ENDC} ')

    def clear(self):
        f = open(f"{self.current_path}/codes.txt", "r+")
        f.truncate(0)
        f.close()
        print(f'\n[{self.HEADER}+{self.ENDC}] Done resetting codes.txt{self.ENDC} ')

    def info(self):
        print(f'''
[{self.HEADER}+{self.ENDC}] This tool is made to generate/check Discord Nitro gift codes. {self.ENDC}
[{self.HEADER}+{self.ENDC}] Its using brute to find valid codes so keep in mind that it might take a while{self.ENDC}

[{self.HEADER}+{self.ENDC}] Option 3 (reset) will clear everything in codes.txt{self.ENDC}
[{self.HEADER}+{self.ENDC}] I recommend using reset if no valid code is found after a run, otherwise it will keep looking for the same code{self.ENDC}

[{self.HEADER}+{self.ENDC}] Note that every Nitro code created by Discord expires in 48 hours{self.ENDC}
[{self.HEADER}+{self.ENDC}] Checking will stop when a valid code is found, so the valid code stays at the bottom{self.ENDC}

[{self.HEADER}+{self.ENDC}] Just make sure to not close the application{self.ENDC}
[{self.HEADER}+{self.ENDC}] That being said, enjoy :){self.ENDC}

[{self.HEADER}+{self.ENDC}] For any questions hit me up on Discord sem#4744{self.ENDC}
        ''')

LinkGen()
