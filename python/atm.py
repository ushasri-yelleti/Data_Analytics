usha_details_ICIC = {
'Adr': '234567890',
'pan': 'APYU146R',
'ATMPIN':'6600',
'balance': '10000'
}
All_attempts = 3
while All_attempts >0:
     user_pin = input('enter ur atm pin:')
     if user_pin in usha_details_ICIC['ATMPIN']:
        print('welcome to ICIC ATM')
        choice_ = int(input('enter \n1.withdraw \n2.deposite:'))
        if choice_ ==1:
           with_m = int(input('enter amount to withdraw:'))
           if with_m <= usha_details_ICIC['balance'] and with_m % 100 ==0:
              usha_details_ICIC['balance'] -= with_m
              print(f'take ur cash nd the balance is {usha_details_ICIC['balance']}')
              else:
                  print(f'insufficient balance or this atm cannot provide change')
                  elif choice_ == 2:
                       depo_m = int(input('enter amount to deposit:'))
                       if depo_m % 100 == 0:
                          usha_details_ICIC['balance'] += depo_m
                          print(f'amount to deposit nd total amount in the bank is {usha_details_ICIC["balance"]}')
                          else:
                              print('this atm doesnt accept change')
         
else:
     All_attempts -= 1
     if All_attempts > 0:
         print(f'incorrect pin entered nd u have {All_attempts} left')
    else:
        print('ur card is blocked..')
         
