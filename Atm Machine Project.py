Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time

print('WLCOME To ICICI Bank')

print('\n\==Please Insit Your ATM CAED==/\n..Do Not Remove Your Card..')
time.sleep(3)

pin = int(input('\nPlease inter your 4 digit number--- '))
blance = 1000

if pin == 9090:
    while True:
        print('\n=== ATM MACHINE ===\n')
        print('1 = check blance')
        print('2 = withdraw amount')
        print('3 = deposit money')
        print('4 = Exit the machine')

        try:
            option = int(input('\nPLEASE CHOOSE ANY ONE OPTION.-->> '))
        except:
            print('Sorry Something went wrong,, Please do one more time..')

        if option == 1:
...             print('------------------------')
...             print(f'Your Current Blance is,, {blance}')
... 
...         if option == 2:
...             withdraw_money = int(input('please inter the withdrawal_amount..--> '))
...             if withdraw_money <= blance:
...                 print('-----------------------------')
...                 blance = blance - withdraw_money
...                 print('\n{please wait your transaction is process}')
...                 print('----------------------------------------|\t')
...                 time.sleep(3)
...                 print(f'{withdraw_money},, Your amount has debited...|')
...                 print(f'Your Current Blance is,, {blance}')
...             else:
...                 print('-------------------------')
...                 print('Sorry Do not Have Sufficent Blance')
... 
...         if option == 3:
...             deposit_money = int(input('Please inter the deposit_amount..--> '))
...             if deposit_money >= 1000:
...                 print('----------------------')
...                 blance = blance + deposit_money
...                 print('Please Wait....| ')
...                 time.sleep(3)
...                 print(f'{deposit_money},, Your amount has credited...| ')
...                 print(f'Your Current Blance is,, {blance}')
...             else:
...                 print('---------------------------')
...                 time.sleep(2)
... 
...                 print('Sorry You Can Not Deposit... You Deposit 1000 Above Only...')
... 
...         if option == 4:
...             print('Thank you from visting our ATM BANK MACHINE ... Please come soon../')
...             break
... else:
