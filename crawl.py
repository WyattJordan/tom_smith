# packages:
# using python 2.6.7
# sudo apt-get build-essential libssl-dev libffi-dev python-dev
# sudo pip install -U setuptools
# sudo pip install cryptography
# sudo pip install enum34
# sudo pip install github3.py
#
# since on Python 2.7.6 run: pip install urllib3[secure]
# then import as below:
import urllib3.contrib.pyopenssl
from github3 import login
#from github import Github


credfile = open("credentials.txt", "r")
usr = credfile.readline()
pwd = credfile.readline()

loggedin = login(usr, password=pwd)
print "\n\nLogged in...\n\n"
myprof = loggedin.me()
print(myprof.name)
print(myprof.login)


#g.search.UserSearchResult()
