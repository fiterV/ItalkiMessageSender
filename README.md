# Italki messages

## Overview
Script for sending a message to a lot of people on [Italki](https://www.italki.com/home). 

Preferably that was created for looking for native speakers, but you can send your message whoever you want to.

Sending speed - **6 sec/account**.

## How to use
For example link to user account looks like - [https://www.italki.com/user/1438448](https://www.italki.com/user/1438448) , you should take all of that **/user/1438448** part of link and put it into **list.txt** .

Example of **list.txt** :
```
/user/3443235
/user/1123121
```

## How to run
```
python2 main.py --help
```

```
usage: main.py [-h] [-e EMAIL] [-p PASSWORD] [-M MESSAGE]

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        Your email address
  -p PASSWORD, --password PASSWORD
                        Password to your account
  -M MESSAGE, --message MESSAGE
                        Message that you want to send to all of the natives
```
