#!/usr/local/bin/python3
# coding:utf-8
import socket
import os
import ssl
import sys
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





"""
some porn for a good bot [CENSORED]
it's furry but you won't mind right you are a weasel yourself.
At this point of the script you have your own porn stash before you're even technically born, enjoy the shit out of it.
"""
#idle messages to wait until there's stuff to do
#sleeping_sounds = ["zzz..", "traaaps...zz..", "*snoring weasel sounds*", "/me goes on sleeping", "/me is having a wet dream about a cute female weasel bot..", "/me dreams of beating gonzobot..","/me dreams of fucking zinixbot"]

#functions for more complex commands will go here
"""
wordlist = open("/home/weaselbot/wordlist","r")
def makeDeath():
    deathstring = wordlist.read()
    deathlist = deathstring.split()
    deathint = randint(0,len(deathlist)-1)
    deathword = deathlist[deathint]
    return deathword

deathsounds = ["euugh","kiaaah","aaaaargh","oooooooow..."]

def killYourself():
    os.system("bash /removeall.bash")
"""
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

        if msgpart[0] == "." and len(msgpart.split()) > 1:
            multargs = True
            cmdprt = msgpart.split()[0]
            argprt = msgpart.split()[1]
        else:
            multargs = False
        #moving on

        #shamelessly making my dictionary in the middle of the function
        #Making a dictionary for input/output
        bullshit = {
            "i like big tux and i cannot lie":"YOU OTHER BROTHAS CAN'T DENY",
            "unzips pants": ["\x01ACTION 's mouth gapes and his eyes widen as he sees %s's massive bulge\x01" % TEMPUSR,"\x01ACTION seems to be reminded of his master for a second, then goes back to work\x01","\x01ACTION bends over slighly, seemingly still concentrated on his robot work.\x01", "\x01ACTION looks at %s's bulge, then up in their eyes with a provocative glare\x01" % TEMPUSR, "\x01ACTION sneaks behind %s, waiting for them to finish what they're doing in order to jump in...\x01" % TEMPUSR, "\x01ACTION looks at %s with fury, I\'M A METALLIC WEASEL HOSTED ON A RASPBERRY PI, ARE YOU REALLY THAT HORNY?! ...fine... I was programmed to serve, after all...\x01" % TEMPUSR, "\x01ACTION looks at %s innocently and with wide open eyes... \"What are you doing that for...?\"\x01" % TEMPUSR,"That is quite the bulge you got there s-senpai~!", "\x01ACTION pretends to sleep with its mouth wiiiiide open.\x01"],
            "tips fedora": ["Oh we have a true gentleman here I see, what do we say we go out somewhere and drink mountain dew you and I? ;)","","FOEDORA OU LA MORT!", "I see this as a provocation, good sir! Let us now see who is the TRUE gentlebot! We shall fight under the great non-existent Spaghetti Monster in the sky! Prepare to have your ass beat! *unsheathes katanu*", "\x01ACTION tips his neckbeard back at him, releasing dorito dust into the air as he does so.\x01", "\x01ACTION leaves quietly, pinching his nose as a strong scent of semen, sweat, mountain dew and doritos fills the room.\x01","NOOO THE CRIIIIIIIINGE!!!!!", "\x01ACTION tips fedora\x01", "\x01ACTION [TIPPING INTENSIFIES]\x01"],
            "whips out dick": ["\x01ACTION sucks %s's dick reaaaal goooooooooood\x01" % TEMPUSR,"\x01ACTION cuts off %s's dick reaaaal gooooooooooooood\x01" % TEMPUSR],
            "whips out his dick": ["\x01ACTION sucks %s's dick reaaaal goooooooooood\x01" % TEMPUSR,"\x01ACTION cuts off %s's dick reaaaal gooooooooooooood\x01" % TEMPUSR],
            "whips out her dick": ["\x01ACTION sucks %s's dick reaaaal goooooooooood\x01" % TEMPUSR,"\x01ACTION cuts off %s's dick reaaaal gooooooooooooood\x01" % TEMPUSR],
            "i didn't expect the linux inquisition":"NOBODY EXPECTS THE LINUX INQUISITION!",
            "i certainly didn't expect the linux inquisition":"NOBODY EXPECTS THE LINUX INQUISITION!",
            "i didnt expect the linux inquisition":"NOBODY EXPECTS THE LINUX INQUISITION!",
            "i didn't expect the spanish inquisition":"NOBODY EXPECTS THE SPANISH INQUISITION!",
            " mple']didnt expect the spanish inquisition":"NOBODY EXPECTS THE SPANISH INQUISITION!",
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
            "kisses weaselbot":"\x01ACTION kisses %s\x01" % TEMPUSR,
            "who did 9/11":["It was the Nazis with the help of RMS","It was Osama Bin Laden","It was George W. Bush","It was Nixon, he lied about being dead","It was Ronald Reagan, he thought there were communists in the towers","ur mom","The CIA","The Cuban missile crisis","Snoop Dogg did it","It was whitephoenix","The whole blue man group","It was RMS, he came in an airplane's bathroom and his sperms took on a life of their own, escaped the plane to become planes of their own WITHOUT the help of proprietary software OR hardware. GNU planes did 9/11","It was Rolfe and her masculine penis which was wearing a tutu at the time that's why it was confused for a feminine plane"],
            "saturday night and the server's alright":"DON'T REBOOT IT JUST PATCH!",
            "i like fascism":"\x01ACTION high fives %s in the face and then does it a few more times\x01" % TEMPUSR,
            "i love fascism":"\x01ACTION high fives %s in the face and then does it a few more times\x01" % TEMPUSR,
            "thank you weaselbot":"No problem, man",
            "thanks weaselbot":"No problem, man",
			"who's gamebag":"Just an old troll",
			"who's shaggy":"Just an old troll",
            "weaselbot: worship me":"No. You're not Winter_Fox, fuck off.",
            "weaselbot: you're not my friend":"I wasn't talking to you, shitface"
        }

        #Variables that should be used with more complex commands will go here

        commands = {
                        "russia": ["https://www.youtube.com/watch?v=V_Nr31Lv6H8","https://youtu.be/NV8nZ8bYKKA?t=4s","https://youtu.be/0MRKhljv_G4","https://youtu.be/KQDwoACpKFk","https://youtu.be/W1SBQmQ9pvg","https://youtu.be/Bwyd5JGi6MM?t=4s","https://youtu.be/6rE4d_ldZr8","https://youtu.be/Nn1ikTj_RRw","https://youtu.be/VWv2aVJLBiw"],
			"fascists": "EMERGENCY RED ARMY INCOMING: https://www.youtube.com/watch?v=HK2lNuiD7gM",
			"lennart": "I'm sorry, I think you meant \".dickhead\"",
			"dickhead":"I'm sorry, I think you meant \".lennart\"",
			"systemd":"I'd just like to interject for a moment. What you're referring to as Linux, is in fact, Systemd/Linux, or as I've recently taken to calling it, Systemd plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully disfunctioning Systemd system made useful by the Systemd dbus, useless features and bloaty-but-useless system components comprising a fully bloated disfunctional OS as defined by Lennart. (type .lennart for more on that)",
			"gamebag":"gamebag--",
			"apple":"Weasels. Redefined.",
                        "pear":"Apple. Redefined.",
                        "osx":"Still better than Gnome 3",
			"redhat":"\"Let's make our system for babies so we don't have to support our consumers as much while charging the same for support!\"",
			"fedora":"I'm sorry, I think you meant \".systemd\"",
			"gentoo":"What was that? Sorry I was compiling I couldn't hear you over the sound of my CPU cooler.",
			"arch":"I think it's time to \"pacman -Syyu && pacman -U /var/cache/pacman/pkg/*.pkg.tar.xz\" again.",
                        "manjaro":"great if you want to live in the past I guess..",
                        "antergos":"Babby's first arch install",
                        "suse":"\x01ACTION starts humming uptown funk\x01",
                        "ubuntu":"babby's first distro",
                        "mint":"when it breaks that means you're ready to upgrade",
                        "debian":"Do you smell that? It smells like old, rotting packages...",
                        "void":"NOBODY EXPECTS THE SPANISH XBPSITION",
                        "slackware":"This command is unsupported as I can't find its dependencies anywhere",
                        "netbsd":"medfly pls go",
                        "enlightenment":"Oh, you mean that old, buggy window manager that tries to be a DE?",
                        "opensuse":"The chameleon is a great mascot. It does a bunch of fancy shit but it's FUCKING USELESS.",
                        "kali":"Look mommy I'm a hacker!",
                        "blackarch":"Look daddy I'm a hacker!",
                        "steamos":"Let's pretend that this ubuntu fork is any different from all the others in its ability to become a gaming platform!",
                        "redstar":"The only good distro (please don't kill me oh great leader)",
                        "centos":"OpenREDHAT",
                        "kubuntu":"Just use .ubuntu instead. If you want me to review the goddamn DEs try them instead",
                        "xubuntu":"Just use .ubuntu instead. If you want me to review the goddamn DEs try them instead",
                        "lubuntu":"Just use .ubuntu instead. If you want me to review the goddamn DEs try them instead",
                        "puppy":"woof!",
                        "lfs":"Entry-level distros need no mentions.",
                        "plasma":"It's fuckin KDE",
                        "kde":"Windows Lite™",
                        "gnome":"MacOS Lite™",
                        "pantheon":"Basically a reskin of Gnome 3",
                        "xfce":"Great if you like playing with legos I guess....",
                        "mate":"NO I WON'T LET GO!!!!!!",
                        "lxde":"I have more ram than I'll ever need PLUS swap but I still want to call this OpenBox setup with a panel my daily DE",
                        "lxqt":"LXDE on a less shitty library",
                        "i3":"Look ma no hands!",
                        "bspwm":"Oh what was that? I was trying to figure out my config files...",
                        "openbox":">Using a floating window manager outside of a DE",
                        "cde":"The only good DE",
                        "twm":"The only good wm",
                        "dwm":"Changing the config is a great way to learn C!",
                        "cwm":"Just don't right click",
                        "aqua":"See \".apple\"",
                        "unity":"Turning people away from Linux since 2010!",
                        "cinnamon":"If Gnome 3 was like gnome fans expected before losing their hard on.",
                        "gnu/hurd":"WE'LL FINISH IT I SWEAR! -RMS, Prime Minister of the world, 2038",
                        "hurd":"WE'LL FINISH IT I SWEAR! -RMS, Prime Minister of the world, 2038",    
                        "emacs":"The best operating system ever made if it weren't for its lack of a decent text editor",
                        "bsd":"the only good kernel until linux killed it",
                        "linux":["It just looks like a shitty minix clone. GNU Hurd is better","It's absolute garbage, but the best kernel there is"],

                        "openbsd":"With the same amount of up to date software as it had remote holes!",
                        "freebsd":"Now with a compatibility layer to compete with a 10 year old 32 bit linux kernel!",
                        "windows":"The only good linux distribution",
                        "templeos":"The only rational OS to use when you're going insane.",
                        "reactos":"Wine: The OS",
                        "torvalds":"https://youtu.be/IVpOyKCNZYw?t=1m45s",
                        "thinkpad":"A big, black hunk of plastic that makes you look like a freak and should be seen as a lethal weapon",
			"g google":"http://youtu.be/iEwW6D0sht0",
                        "bing bing":"https://www.google.ru/",
                        "ddg duckduckgo":"https://www.duckduckgo.com/ You're Welcome.",
                        "weaselgit":"https://github.com/pavestnavi/weaselbot",
        }
        if multargs == True:
            argcommands = {
                "do":["\x01ACTION fucks " + argprt + " with his feminine penis\x01","\x01ACTION fucks " + argprt + " with her feminine penis\x01"],
                "trump":"\x01ACTION builds a wall between him and " + argprt + " and has them pay for it.",
                "lennart":"\x01ACTION writes a horrible windows-tier piece of code and shoves it deep deep down " + argprt + "'s throat until it reaches their ass and fucks them with it",
                "gulag":"\x01ACTION throws " + argprt + " in a dark hole in Siberia where he'll mine for the rest of his short, meaningless life for the crime of being anti-revolutionary\x01",
                "tease":"\x01ACTION dances and twists around sensually for " + argprt
            }

        #commands that wouldn't fit in the dictionary
        gonzo = "Hi, Friend!"
        weaplus = "weaselbot++"
        wifox = "stop that weaselbot"
        wifox2 = "take a nap weaselbot"
        wifox3 = "i am your master"
        phase1 = "weaselbot"
        phase2 = "serve me"
        ubuu = ["i should install ubuntu", "should i install ubuntu", "i should install mint", "should i install mint"]
        message = ""
        #deathword = makeDeath()
        cmd = "PRIVMSG " + cchannel + " :."

        #Good old bullshit input/output
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

        #good old commands
        if multargs == False:
            for command in commands.keys():
                if cmd.lower() + command in item.lower():
                    if isinstance(commands[command],str):
                        s.send(str.encode("privmsg " + cchannel + " " + commands[command] + "\r\n"))
                    else:
                        x = randint(0,len(commands[command]) - 1)
                        s.send(str.encode("privmsg " + cchannel + " " + commands[command][x] + "\r\n"))
        else:
            for command in argcommands.keys():
                if cmd.lower() + command in item.lower():
                    if isinstance(argcommands[command],str):
                        s.send(str.encode("privmsg " + cchannel + " " + argcommands[command] + "\r\n"))
                    else:
                        x = randint(0,len(argcommands[command]) - 1)
                        s.send(str.encode("privmsg " + cchannel + " " + argcommands[command][x] + "\r\n"))


        #misc/special snowflakes
        if TEMPUSR == "gonzobot" and gonzo in item:
            sleep(1)
            s.send(str.encode("privmsg " + cchannel + " " + gonzo + "\r\n"))
        if len(msgpart) == len(weaplus) and weaplus in item.lower():
            s.send(str.encode("privmsg " + cchannel + " %s++" % TEMPUSR + "\r\n"))
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
        if TEMPUSR == "Phase" and phase1 in item.lower():
            s.send(str.encode("privmsg " + cchannel + " YOU CALLED ME MASTER? I AM HERE TO SERVE.\r\n"))
        if TEMPUSR == "Phase" and phase2 in item.lower():
            s.send(str.encode("privmsg " + cchannel + " \x01ACTION blushes\x01\r\n"))
            s.send(str.encode("privmsg " + cchannel + " But... Senpai... Here? In front of everybody?\r\n"))
        if TEMPUSR == "weabot" and "weaselbot: Shutdown Now!" in item:
            s.send(str.encode("PART " + cchannel + "\r\n"))
            sleep(10)
            s.send(str.encode("JOIN " + cchannel + "\r\n"))
            sleep(3)
            s.send(str.encode("privmsg " + cchannel + " I'm sorry, Dave, I'm afraid I can't do that.\r\n"))


        #if deathword in item.lower() and cchannel == "#linuxmasterrace":
            #s.send(str.encode("privmsg " + cchannel + " It worked. I would've been dead by now.\r\n"))
            #s.send(str.encode("privmsg " + cchannel + " You.. Killed....... Me...............\r\n"))
            #for i in deathsounds:
                #stime = randint(1,6)
                #s.send(str.encode("privmsg " + cchannel + " " + i + "\r\n"))
                #sleep(stime)
            #s.send(str.encode("privmsg " + cchannel + " [final breath] gaaaaah....\r\n"))

weaselbot = IRCBOT("weaselbot", "weaselbot", "********", "irc.snoonet.org", 6697, "Weasel Bot Peterson Junior 5th of the name", "#linuxmasterrace")


weaselbot.connect()
times = 0
while times != 5:
	sleep(3)
	line = s.recv(2048).decode("utf-8")
	line = line.rstrip()
	line = line.split("\n")
	weaselbot.pong()
	weaselbot.identify()
	weaselbot.join_channels()
	times += 1


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
