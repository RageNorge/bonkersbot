#!/usr/local/bin/python3
# coding:utf-8
import socket
import os
import ssl
import sys
import praw
import time
from time import sleep
from datetime import datetime
from random import randint
                                #THIS BOT IS LICENSED UNDER THE BSD LICENSE
###FEEL FREE TO MAKE IT PROPRIETARY AND REPACKAGE IT IN A NICE LITTLE GOLDEN BOX TO THEN SELL IT TO ME
"""
Copyright (c) 2016, pavestnavi
All rights reserved.])

Weaselbot was heavily inspired by zinixbot, thanks to zinn, unixbird and alinea for making it.
https://git.indohy.us/dubbleohnexus/zinixbot

This Bot is based off the weaselbot base, thanks to weabot for making the bot.
https://github.com/pavestnavi/weaselbot
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(s)
line = "placeholder"
cchannel = ""
adminlist = ["RageNorge"] #add your username in there. Make sure your own username is the first entry.

r = praw.Reddit(user_agent='.meme command from bonkersbot, the irc-bot. Searches for imgur links on r/dankmemes to add to separate file')
print("Grabbing /r/dankmemes hot...")
submissions = r.get_subreddit('dankmemes').get_hot(limit=30)

memelist = []
memecache = []
cache = []
MIN_SCORE = 200

class IRCBOT(object):

    channelslst = []

    def __init__(self, nick, ident, password, host, port, realname, channels):
        self.nick = nick
        self.ident = ident
        self.password = password
        self.host = host
        self.port = port
        self.realname = realname
        self.channels = channels

    def makeChannelsList(self):
        for i in self.channels.split():
            self.channelslst.append(i)

    def connect(self):
        s.connect((self.host,self.port))
        s.send(str.encode("NICK " + self.nick + "\n"))
        s.send(str.encode("USER " + self.ident + " " + self.ident + " " + self.ident + " :This is a bot." + "\r\n"))

#PAST THIS POINT ONLY PUT IN THE MAIN LOOP

    def pong(self):
        for item in line:
            if (item.find("PING") != -1):
                item = item.rstrip()
                item = item.split()
                s.send(str.encode('PONG ' + item[1] + '\n'))


    def identify(self):
        for item in line:
            if item.find("Welcome") != -1:
                while True:
                    s.send(str.encode("privmsg " + "NickServ" + " IDENTIFY " + self.password + "\r\n"))
                    s.send(str.encode("NICK " + self.nick + "\n"))
                    if item.find("You are now logged in"):
                        break

    def join_channels(self): #write more than one channel by separating using spaces
        for item in line:
            if item.find("Welcome") != -1:
                for i in self.channelslst:
                    s.send(str.encode("JOIN " + i + "\n"))

    def greet(self):
        channel = self.channels.split()
        for item in channel:
            s.send(str.encode("privmsg " + item + " :ayy errybody\r\n"))

#functions for more complex commands should go here

def sendMessage(chan,msg): #function to send a "msg" message to the "chan" channel
    s.send(str.encode("privmsg " + chan + ' ' + msg + "\r\n"))

def maymaytron():
    time.sleep(0)
    # Process all the submissions from the front page
    print("Grabbing submissions...")
    for submission in submissions:
        # Check for all the cases where we will skip a submission:
        if "i.imgur.com/" not in submission.url:
            print("Not imgur link, skipping...")
            continue # skip non-imgur submissions
        if submission.score < MIN_SCORE:
            print("Submission has under 200 points, skipping...")
            continue # skip submissions that haven't even reached 100 (thought this should be rare if we're collecting the "hot" submission)
        if submission.url not in cache and "imgur.com/" in submission.url: #checks for imgur link
            print("Found imgur link! \n Appending...")
            memelist.append(submission.url)
            cache.append(submission.url)

def dothething():
    multargs = False
    for item in line:
        print(item)
        try: #this whole thing is to define the cchannel, TEMPUSR and msgpart variables.
            complete = item[1:].split(':',1)
            info = complete[0].split(' ')
            msgpart = complete[1] #This is what the message consists of
            sender = info[0].split('!')
            TEMPUSR = str(sender[0]) #This is the name of the user who sent the message.
            cchannel = str(info[2]) #This is the name of the channel the message was read from.
            #Using cchannel with the sendMessage argument ensures that your bot replies in the right channel.
            print(cchannel)
            print(TEMPUSR)
        except IndexError:
            return 0

        if len(msgpart) >= 1:
            if msgpart[0] == "." and len(msgpart.split()) > 1: # This has the bot make a distinction between commands with arguments and commands without.
                multargs = True
                cmdprt = msgpart.split()[0] #cmdprt is the command
                argprt = msgpart.split()[1] #argprt is the argument
            else:
                multargs = False

        #shamelessly making my dictionary in the middle of the function
        #Making a dictionary for input/output
        #Remember to separate items in a dictionary with a comma. See the examples in the argcommands dictionary
        #Using a list as the dictionary's value will have your bot pick one item at random. See the example in the commands dictionary
        bullshit = { # The bot replies to a key in this dictionary with its value. It looks for them anywhere in the message, so make sure not to use a common word to not make it spammy
                "ayy":"lmao",
                "bonkersbot is shit":"u fukin wot m8, i'll rek you on wii party",
                "bonkersbot is spammy":"wtf did you just expect me to do?",
                "good bonkersbot":"danks m89",
                "bad bonkersbot":"u fukin wot m8, i'll rek you on wii party",
                "cheese":"sometimes, i dream about cheese..."
        }

        commands = { #This is the same as the bullshit dictionary except it will look in the beginning of the message for a '.', then the message right after. It only responds if 1 word is said.
                #replies bonkersbot git repo
                "gitbonkers":"https://github.com/RageNorge/bonkersbot",
                "purpose":"I pass the butter",
                "creator":"RageNorge, our attack helicopter, lord and saviour. weabot, someone who is a weaboo",
                "magic":"http://www.reactiongifs.com/r/mgc.gif",
                #if the bot sees .example in the beginning of the message and there are no other words following, he has a 50/50 chance of printing either "This is an example" or "This is another example"
        }
        if len(msgpart) >= 1:
            if multargs == True: #This will only be read if the message has more than 1 word, this is meant to take in an argument and print it back. Pushing the argument to a function to make it say something different for every word would theoretically work, but I haven't had a use for that yet.
                argcommands = {
                        #".example word" will only print "This is an example"
                        #"example":"This is an example", #notice the comma at the end to separate the 2 entries
                        #"mkexamplefor something" will print "Here is an example for: something"
                        "fetch":"*fetches " + argprt + "*"
                }

        memedict = {
                "maymay":memelist
        }

        #variables that should be used with more complex commands should go here.
        askjoin = "bonksjoin " #modify this to define what you have to say to your bot to make it join a channel, this works over PM as well
        askleave = "bonkspart"
        asksay = ".sayin "
        cmd = "PRIVMSG " + cchannel + " :."
        masterserve = "BOOONKERS!"
        askquit = "bonksdown"
        maymay = "maymay"

        #Good old bullshit input/output
        for key in bullshit.keys(): #This looks for keys in the bullshit dictionary, determine whether it's a string or a list and respond accordingly
            if key.lower() in item.lower():
                if isinstance(bullshit[key],str):
                    sleep(1)
                    sendMessage(cchannel,bullshit[key])
                else:
                    sleep(1)
                    x = randint(0,len(bullshit[key]) - 1)
                    sendMessage(cchannel,bullshit[key][x])

        #good old commands
        if len(msgpart) >= 1:
            if multargs == False:
                for command in commands.keys(): #same as with bullshit except with the commands dictionary, only if it has only 1 word and starts with a "."
                    if msgpart.split()[0].lower() == "." + command and cmd.lower() + command.lower() in item.lower():
                        if isinstance(commands[command],str):
                            sendMessage(cchannel,commands[command])
                        else:
                            x = randint(0,len(commands[command]) - 1)
                            sendMessage(cchannel,commands[command][x])
            else:
                for command in argcommands.keys(): #same as with the others except only if it has over a word after the "."
                    if msgpart.split()[0].lower() == "." + command and cmd.lower() + command in item.lower():
                        if isinstance(argcommands[command],str):
                            sendMessage(cchannel,argcommands[command])
                        else:
                            x = randint(0,len(argcommands[command]) - 1)
                            sendMessage(cchannel,argcommands[command][x])

        #misc/special snowflakes
        #define more complex commands here that aren't covered with the dictionaries. This is where sendMessage() is useful
            if TEMPUSR in adminlist and askleave in item: #this command allows anybody in the adminlist to tell the bot to leave
                bonkersbot.channelslst.remove(cchannel)
                s.send(str.encode("PART " + cchannel + "\r\n"))
            if TEMPUSR in adminlist and askquit in item:
                exit()
            if TEMPUSR in adminlist and len(msgpart.split()) == len(askjoin.split())+1 and cmd + askjoin in item: #this one allows anybody in the adminlist to tell the bot to join a specific channel
                TEMPCHANNEL = msgpart.split()[1] # The 6th word is the channel's name, if you modify the message modify this as well. For example: weaselbot: Please join this channel: #weaselbot would have it join #weaselbot
                bonkersbot.channelslst.append(TEMPCHANNEL)
                s.send(str.encode("JOIN " + TEMPCHANNEL + "\r\n"))
            if TEMPUSR in adminlist and cmd.lower() + "say" in item.lower(): #allows you to tell him to say womething via the .say command

                saywhat = msgpart.split()[1:]
                sendMessage(cchannel,' '.join(saywhat))
            if TEMPUSR in adminlist and asksay in item: #This tells the bot to say in whatever channel you chose all the words that follow. The channel is the fifth word, right after in.
                whatchannel = msgpart.split()[1]
                saywhat2 = msgpart.split()[5:]
                sendMessage(whatchannel,' '.join(saywhat2))
            if TEMPUSR in adminlist and cmd + "mkADMIN" in item:
                newAdmin = msgpart.split()[1]
                if newAdmin == "bonkersbot":
                    sendMessage(cchannel,"Adding me to the KKK is too dangerous for our Universe and the life within it.")
                else:
                    adminlist.append(newAdmin)
                    sendMessage(cchannel,"Added " + newAdmin + " to the admin list!")
            if TEMPUSR in adminlist and cmd + "rmADMIN" in item: #This allows only you to remove admins.
                rmAdmin = msgpart.split()[1]
                if rmAdmin != adminlist[0]:
                        if rmAdmin in adminlist:
                                adminlist.remove(rmAdmin)
                                sendMessage(cchannel,"Removed naughty boy " + rmAdmin + " from the admin list!")
                        else:
                                sendMessage(cchannel,rmAdmin + " is not in the admin list.")
                else:
                        sendMessage(cchannel,"I won't remove my master from the admin list! What about you instead?")
                        adminlist.remove(TEMPUSR)
            if TEMPUSR in adminlist and masterserve in item:
                sendMessage(cchannel,"Y-yes m-master?")
            if cmd + maymay in item:
                if len(msgpart) >= 1:
                    if multargs == False:
                        for memerino in memedict.keys(): #same as with commands except with the memedict dictionary.
                            if msgpart.split()[0].lower() == "." + memerino and cmd.lower() + memerino.lower() in item.lower():
                                if isinstance(memedict[memerino],str):
                                    sendMessage(cchannel,memedict[memerino])
                                else:
                                    x = randint(0,len(memedict[memerino]) - 1)
                                    sendMessage(cchannel,memedict[memerino][x])

#define your bot here. Make sure to replace yourbot.* with your bot's name and add your name where necessary, in the adminlist at least.
#I named everything that you should replace "yourbot" and "yourname"
#password = open("password.txt")
bonkersbot = IRCBOT("bonkersbot", "bonkersbot", "fdjk190d", "irc.snoonet.org", 6697, "Bonkers of the 9th order", "#lmroutside #ragenorge #bonkersbot")

bonkersbot.makeChannelsList()
bonkersbot.connect()
#uncomment this if you want to have it do a greeting message
"""
times = 0
while times != 5:
        sleep(3)
        line = s.recv(2048).decode("utf-8","replace")
        line = line.rstrip()
        line = line.split("\n")
        yourbot.pong()
        yourbot.identify()
        yourbot.join_channels()
        times += 1


print("greeting..")
#yourbot.greet()
print("done greeting, heading on to main loop")
"""
while 1:
    bonkersbot.pong()
    bonkersbot.identify()
    bonkersbot.join_channels()
    line = s.recv(2048).decode("utf-8","replace")
    line = line.rstrip()
    line = line.split("\n")
    dothething()
    maymaytron()
