#!/usr/bin/env python3

import shutil, psutil, socket
import email.message
import smtplib, os, sys

user = os.environ.get('USER')

def is_disk_less_20percent():
    foo = shutil.disk_usage('/')
    if (foo.free / foo.total * 100) < 20:
        return True
    else:
        return False

def is_cpu_over_80percent():

    if int(psutil.cpu_percent()) > 80 :
        return True
    else:
        return False

def is_free_mem_less_500MB():
    if ( psutil.virtual_memory().free / 2**20) < 500 :
        return True
    else:
        return False


def localhost_is_unresolvable():
    if socket.gethostbyname('localhost') != '127.0.0.1' :
        return True
    else:
        return False


def generate(subject, body):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  # message["To"] = user + "@example.com"
  message["To"] = user + "x@gmail.com"
  message["From"] = "automation@example.com"
  message["Subject"] = subject
  message.set_content(body)
  return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()



def checker(func, subject):
    body = "Please check your system and resolve the issue as soon as possible."
    if func:
        print('Alert!!! : {}'.format(subject))
        message = generate(subject, body)
        send_email(message)
    else:
        print('No Alerts : {}'.format(subject))

checker(is_cpu_over_80percent(), "Error - CPU usage is over 80%")
checker(is_disk_less_20percent(), "Error - Available disk space is less that 20%")
checker(is_free_mem_less_500MB(), "Error - Available memery is less than 500MB")
checker(localhost_is_unresolvable(), "Error - localhost cannot be resolved to 127.0.0.1")
# for check in is_disk_less_20percent, is_cpu_over_80percent, is_free_mem_less_500MB, localhost_is_unresolvable:
    # rsrc = str(check.__name__)
    # if check():
    #     print('{} is alerting'.format(rsrc))
