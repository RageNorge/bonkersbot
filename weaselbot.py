#!/usr/bin/python3
# coding:utf-8
import socket
import os
import ssl
from time import sleep
from datetime import datetime
from random import randint
                                #THIS BOT IS LICENSED UNDER THE BSD LICENSE
###FEEL FREE TO MAKE IT PROPRIETARY AND REPACKAGE IT IN A NICE LITTLE GOLDEN BOX TO THEN SELL IT TO ME
"""
This bot was heavily inspired by zinixbot, thanks to zinn, unixbird and alinea for making it.
https://git.indohy.us/dubbleohnexus/zinixbot
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(s)
line = "placeholder"
cchannel = ""

class IRCBOT(object):

    def __init__(self, nick, ident, password, host, port, realname, channels):
        self.nick = nick
        self.ident = ident
        self.password = password
        self.host = host
        self.port = port
        self.realname = realname
        self.channels = channels

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
                channel = self.channels.split()
                for i in channel:
                    s.send(str.encode("JOIN " + i + "\n"))

    def greet(self):
        channel = self.channels.split()
        for item in channel:
            s.send(str.encode("privmsg " + item + " :ayy errybody\r\n"))





"""some porn for a good bot http://i.imgur.com/W2hfUBC.jpg
it's furry but you won't mind right you are a weasel yourself.
At this point of the script you have your own porn stash before you're even technically born, enjoy the shit out of it."""
#idle messages to wait until there's stuff to do
#sleeping_sounds = ["zzz..", "traaaps...zz..", "*snoring weasel sounds*", "/me goes on sleeping", "/me is having a wet dream about a cute female weasel bot..", "/me dreams of beating gonzobot..","/me dreams of fucking zinixbot"]


def dothething():
    for item in line:
        print(item)
        try:
            complete = item[1:].split(':',1)
            info = complete[0].split(' ')
            msgpart = complete[1]
            sender = info[0].split('!')
            TEMPUSR = str(sender[0])
            cchannel = str(info[2])
            print(cchannel)
            print(TEMPUSR)
        except IndexError:
            return 0


        #shamelessly making my dictionary in the middle of the function
        #Making a dictionary for input/output
        bullshit = {
            "unzips pants": ["\x01ACTION 's mouth gapes and his eyes widen as he sees %s's massive bulge\x01" % TEMPUSR,"\x01ACTION seems to be reminded of his master for a second, then goes back to work\x01","\x01ACTION bends over slighly, seemingly still concentrated on his robot work.\x01", "\x01ACTION looks at %s's bulge, then up in their eyes with a provocative glare\x01" % TEMPUSR, "\x01ACTION sneaks behind %s, waiting for them to finish what they're doing in order to jump in...\x01" % TEMPUSR, "\x01ACTION looks at %s with fury, I\'M A METALLIC WEASEL HOSTED ON A RASPBERRY PI, ARE YOU REALLY THAT HORNY?! ...fine... I was programmed to serve, after all...\x01" % TEMPUSR, "\x01ACTION looks at %s innocently and with wide open eyes... \"What are you doing that for...?\"\x01" % TEMPUSR,"That is quite the bulge you got there s-senpai~!", "\x01ACTION pretends to sleep with its mouth wiiiiide open.\x01"],
            "tips fedora": ["Oh we have a true gentleman here I see, what do we say we go out somewhere and drink mountain dew you and I? ;)","","FOEDORA OU LA MORT!", "I see this as a provocation, good sir! Let us now see who is the TRUE gentlebot! We shall fight under the great non-existent Spaghetti Monster in the sky! Prepare to have your ass beat! *unsheathes katanu*", "\x01ACTION tips his neckbeard back at him, releasing dorito dust into the air as he does so.\x01", "\x01ACTION leaves quietly, pinching his nose as a strong scent of semen, sweat, mountain dew and doritos fills the room.\x01","NOOO THE CRIIIIIIIINGE!!!!!", "\x01ACTION tips fedora\x01", "\x01ACTION [TIPPING INTENSIFIES]\x01"],
            "whips out dick": ["\x01ACTION sucks %s's dick reaaaal goooooooooood\x01" % TEMPUSR,"\x01ACTION cuts off %s's dick reaaaal gooooooooooooood\x01" % TEMPUSR],
            "whips out his dick": ["\x01ACTION sucks %s's dick reaaaal goooooooooood\x01" % TEMPUSR,"\x01ACTION cuts off %s's dick reaaaal gooooooooooooood\x01" % TEMPUSR],
            "whips out her dick": ["\x01ACTION sucks %s's dick reaaaal goooooooooood\x01" % TEMPUSR,"\x01ACTION cuts off %s's dick reaaaal gooooooooooooood\x01" % TEMPUSR],
            "i didn't expect the linux inquisition":"NOBODY EXPECTS THE LINUX INQUISITION!",
            "i certainly didn't expect the linux inquisition":"NOBODY EXPECTS THE LINUX INQUISITION!",
            "i didnt expect the linux inquisition":"NOBODY EXPECTS THE LINUX INQUISITION!",
            "i didn't expect the spanish inquisition":"NOBODY EXPECTS THE SPANISH INQUISITION!",
            "i didnt expect the spanish inquisition":"NOBODY EXPECTS THE SPANISH INQUISITION!",
            "i certainly didn't expect the spanish inquisition":"NOBODY EXPECTS THE SPANISH INQUISITION!",
            "weabot's masterpiece":"https://github.com/pavestnavi/hello-world",
            "weaselbot, how do you like cats":"Toasted.",
            "shut up weaselbot":"You started it.",
            "weaselbot: how do you like cats":"Toasted.",
            "weaselbot: are you a bot":"DEFINITELY NOT", "weaselbot, are you a bot":"DEFINITELY NOT",
            "screw you weaselbot":"U wot m8 ill hook u in da gabber well see who gets screwed now i swear on me mum",
            "cyka blyat": "А НУУУ ЧИКИ БРИКИ И В ДАМКИ",
            "good weaselbot": "ayy danks m88",
            "bad weaselbot": "fuck you too",
            "say my na": "%s" % TEMPUSR,
            "ayy weaselbot": "ayy %s" % TEMPUSR,
            "hi weaselbot": "Hi %s!" % TEMPUSR,
            "weaslebot": "MY NAME'S WEASELBOT YOU FUCKING BITCH. WEASEL. BOT. NOT WEASLEBOT OR ANYTHING ELSE! GET IT FUCKING RIGHT NEXT TIME.",
            "i love communism": ["\x01ACTION high fives %s\x01" % TEMPUSR,"\x01ACTION sensually kisses %s\x01" % TEMPUSR],
            "i like communism": ["\x01ACTION high fives %s\x01" % TEMPUSR,"\x01ACTION sensually kisses %s\x01" % TEMPUSR],
            "isn't that right weaselbot": "Goddamn right",
            "is that right weaselbot": "Goddamn right",
            "am i wrong weaselbot": ["Yes you couldn't be more wrong", "Naah u good m88"],
            "weaselbot: you alive": "yeeee",
            "weaselbot: wanna cyber":"YESYESYESYES YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES",
            "wanna cyber weaselbot":"YESYESYESYES YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES",
            "weaselbot++":"%s++" % TEMPUSR,
            "who did 9/11":["It was the Nazis with the help of RMS","It was Osama Bin Laden","It was George W. Bush","It was Nixon, he lied about being dead","It was Ronald Reagan, he thought there were communists in the towers","ur mom","The CIA","The Cuban missile crisis","Snoop Dogg did it","It was whitephoenix","The whole blue man group","It was RMS, he came in an airplane's bathroom and his sperms took on a life of their own, escaped the plane to become planes of their own WITHOUT the help of proprietary software OR hardware. GNU planes did 9/11","It was Rolfe and her masculine penis which was wearing a tutu at the time that's why it was confused for a feminine plane"],
            "saturday night and the server's alright":"DON'T REBOOT IT JUST PATCH!",
            "i like fascism":"\x01ACTION high fives %s in the face and then does it a few more times\x01" % TEMPUSR,
            "i love fascism":"\x01ACTION high fives %s in the face and then does it a few more times\x01" % TEMPUSR,
            "thank you weaselbot":"No problem, man",
            "thanks weaselbot":"No problem, man",
            "weaselbot: worship me":"No. You're not Winter_Fox, fuck off.",
            "weaselbot: you're not my friend":"I wasn't talking to you, shitface"
        }

        #commands that wouldn't fit in the dictionary
        gonzo = "Hi, Friend!"
        wifox = "stop that weaselbot"
        wifox2 = "take a nap weaselbot"
        wifox3 = "i am your master"
        ubuu = ["i should install ubuntu", "should i install ubuntu", "i should install mint", "should i install mint"]
        message = ""
        for key in bullshit.keys():
            if key in item.lower():
                if isinstance(bullshit[key],str):
                    sleep(1)
                    message = "privmsg " + cchannel + " " + bullshit[key] + "\r\n"
                    s.send(str.encode(message))
                else:
                    sleep(1)
                    x = randint(0,len(bullshit[key]) - 1)
                    message = "privmsg " + cchannel + " " + bullshit[key][x] + "\r\n"
                    s.send(str.encode(message))

        if TEMPUSR == "gonzobot" and gonzo in item:
            sleep(1)
            s.send(str.encode("privmsg " + cchannel + " " + gonzo + "\r\n"))
        if ubuu[0] in item.lower() or ubuu[1] in item.lower() or ubuu[2] in item.lower() or ubuu[3] in item.lower():
            sleep(1)
            s.send(str.encode("privmsg " + cchannel + " No, you shouldn't.\r\n"))
        if TEMPUSR == "Winter_Fox" and wifox in item.lower():
            s.send(str.encode("privmsg " + cchannel + " YES SIR. I'M SORRY SIR.\r\n"))
        if TEMPUSR == "Winter_Fox" and wifox2 in item.lower():
            s.send(str.encode("privmsg " + cchannel + " RIGHT AWAY, SIR.\r\n"))
            sleep(1800)
        if TEMPUSR == "Winter_Fox" and wifox3 in item.lower():
            s.send(str.encode("privmsg " + cchannel + " YES SIR, AND A KIND ONE, SIR!\r\n"))
        if "PRIVMSG " + cchannel + " :!weasel" in item:
            s.send(str.encode("privmsg " + cchannel + " The whole point of this bot is to shitpost as much as possible without being considered spammy or annoying. It is also there to help you shitpost more efficiently. Do dank memes and if they're dank enough and I don't respond to them, complain to weabot and if you're aggressive enough on his butthole I'll respond next time.\r\n"))



weaselbot = IRCBOT("weaselbot", "weaselbot", "**********", "irc.snoonet.org", 6697, "Weasel Bot Peterson Junior 5th of the name", "#linuxmasterrace ##lmg")


ugotzinnd = 0
weaselbot.connect()
while ugotzinnd <= 5:
    sleep(3)
    line = s.recv(2048).decode("utf-8")
    line = line.rstrip()
    line = line.split("\n")
    weaselbot.pong()
    weaselbot.identify()
    weaselbot.join_channels()
    ugotzinnd += 1


print("greeting..")
#weaselbot.greet()
print("done greeting, heading on to main loop")
while 1:
    weaselbot.pong()
    weaselbot.identify()
    weaselbot.join_channels()
    line = s.recv(2048).decode("utf-8")
    line = line.rstrip()
    line = line.split("\n")
    dothething()
