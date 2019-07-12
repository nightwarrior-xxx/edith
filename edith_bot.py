from edith_class import *

server = "irc.freenode.net"
port = 6667
botname = "edith_"
botnickpass = "iamironman"
botpass = "tonystark"
channel = "#testedith"
admin_name = ['nightwarrior-xxx']
warn_user = {}
bad_words = ['ass', 'asshole', 'fuckoff', 'pussy', 'fuck', 'wtf', 'bitch']

irc = help_edith()

irc.connect(server, port, channel, botname)


while True:
    msg = irc.get_message()
    print(msg)
    try :

        if "PRIVMSG" in msg and channel in msg:
            real_msg = msg.split('PRIVMSG')[1].split(':')[1]
            name = msg.split('!')[0][1:]

            # if real_msg.find("#edith") != -1 :
            #     message  = "Hello {name}. How can I help you ? ".format(name=name)
            #     irc.send_message(channel, message)
            #     print('message send !!')

            # if real_msg.find("#stopedith") != -1:
            #     if name in admin_name:
            #         irc.send_message(channel, "I am going for a sleep. But I will be back soon. Till then save your ass from NSA")
            #         irc.stop()

            for word in real_msg.split():
                if word == "#edith":
                    message  = "Hello {name}. How can I help you ? ".format(name=name)
                    irc.send_message(channel, message)
                    print('message send !!')
                
                elif word == "#stopedith":
                    if name in admin_name:
                        irc.send_message(channel, "I am going for a sleep. But I will be back soon. Till then save yourself from NSA")
                        irc.stop()
                
                elif word in bad_words:
                    warn_msg = "This is warning {name}, next time you will be thrown out and I will also ask NSA to breach your privacy which they love to :|".format(name=name)
                    irc.send_message(channel, warn_msg)
                    print('warning sent !!')
                    break



    except Exception:
        print('Something is wrong. NSA is watching you')
    
    
    