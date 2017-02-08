import subprocess
import os
import time
import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler
from subprocess import Popen

h = os.popen('hostname')
nama = h.read()

p = os.popen('pwd')
direk = p.read()

l = os.popen('ls -lrt')
isi = l.read()

t = subprocess.Popen(["ls", "-lrt"], stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
lihat = t.stdout.read()

df = os.popen('df -kh')
memori = df.read()

def mulai(bot, update):
    update.message.reply_text('Welcome {}'.format(update.message.from_user.first_name))
    update.message.reply_text('Silahkan berikan command linux = /hostname, /pwd, /ls, /tail, /space ')

def hostname(bot, update):
        update.message.reply_text(
        nama
        )

def pwd(bot, update):
        update.message.reply_text(
        direk
        )

def ls(bot, update):
        update.message.reply_text(
        isi
        )

def tail(bot, update):
        update.message.reply_text(
        lihat
        )

def space(bot, update):
        update.message.reply_text(
        memori
        )

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

updater = Updater('314762661:AAHA2a-LKZvnrFPevaR-u5X7JeidjZxotks')

updater.dispatcher.add_handler(CommandHandler('mulai', mulai))
updater.dispatcher.add_handler(CommandHandler('hostname', hostname))
updater.dispatcher.add_handler(CommandHandler('pwd', pwd))
updater.dispatcher.add_handler(CommandHandler('ls', ls))
updater.dispatcher.add_handler(CommandHandler('tail', tail))
updater.dispatcher.add_handler(CommandHandler('space', space))
updater.dispatcher.add_handler(CommandHandler('exec', exec, pass_args=True
))

updater.start_polling()
updater.idle()