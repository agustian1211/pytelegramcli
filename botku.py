import subprocess
import os
import time
import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
from subprocess import Popen


def mulai(bot, update):
    update.message.reply_text('Welcome {}'.format(update.message.from_user.first_name))
    update.message.reply_text('Silahkan berikan command linux = /exec dilanjutkan dengan param $host@ip $command  ')

def exec(bot, update, args):
    user = update.message.from_user.username
    commands = ' '.join(args)
    mesin = args[0]
    perintah = args[1]
    #pesan = ' '.join('ssh',mesin,commands.split()[1:])
    pesan = ' '.join(commands.split()[1:])

    userlist = ['AllBlue1211','sutrissetyadi']
    list = ['vi','more','less','rm']
    if (user in userlist):
       if (perintah in list):
          p='command tidak boleh digunakan'
          update.message.reply_text(p)
       else:
          ssh = subprocess.Popen(["ssh", "%s" % mesin, pesan],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
          result = ssh.stdout.readlines()
          if result == []:
             error = ssh.stderr.readlines()
             print (error)
             update.message.reply_text(error)
          else:
             print (result)
             update.message.reply_text(result)
             #hasil = os.popen(pesan)
             #textting = hasil.read()
             #update.message.reply_text(mesin)
    else:
       pi='Kau tak bisa pakai bot ini'
       update.message.reply_text(pi)

updater = Updater('TOKEN')

updater.dispatcher.add_handler(CommandHandler('mulai', mulai))
updater.dispatcher.add_handler(CommandHandler('exec', exec, pass_args=True
))

updater.start_polling()
updater.idle()
