from edith_class import *

server = "irc.freenode.net"
port = 6667
botname = "edith_"
botnickpass = "iamironman"
botpass = "tonystark"
channel = "#testedith"
admin_name = ['nightwarrior-xxx']
users = [
'ryzokuken', 'sidntrivedi012', 'nightwarrior-xxx','rogers_'
'shermisaurus','weirdwiz'
]

irc = help_edith()

irc.connect(server, port, channel, botname)


while True:
    msg = irc.get_message()
    print(msg)
    try :

        if "PRIVMSG" in msg and channel in msg:
            real_msg = msg.split('PRIVMSG')[1].split(':')[1]
            name = msg.split('!')[0][1:]           

            if name not in users:
                welcome_msg = "Welcome {name} to the IRC channel of OSDC. You are save here from NSA".format(name=name)
                irc.send_message(channel, welcome_msg)
                print('Welcome message send')
                users.append(name)

            if real_msg.find("fuck") != -1 or \
                real_msg.find("asshole") != -1 or \
                real_msg.find("ass") != -1 or \
                real_msg.find("bitch") != -1 or \
                real_msg.find("fuckoff") != -1 or \
                real_msg.find("motherfucker") != -1:
                
                warn_msg = "This is warning {name}, next time you will kicked out.".format(name=name)
                irc.send_message(channel, warn_msg)
                print('warning sent !!')


            elif real_msg.find("#edith") != -1 :
                message  = "Hello {name}. You are save here from NSA. How can I help you ?".format(name=name)
                irc.send_message(channel, message)
                print('message send !!')

            elif real_msg.find("#stopedith") != -1:
                if name in admin_name:
                    irc.send_message(channel, "I am going for a sleep. But I will be back soon. Till then save your ass from NSA")
                    irc.stop()


                  
                 
                 
            


            # for word in real_msg.split():
            #     if word == "#edith":
            #         message  = "Hello {name}. How can I help you ? ".format(name=name)
            #         irc.send_message(channel, message)
            #         print('message send !!')
                
            #     elif word == "#stopedith":
            #         if name in admin_name:
            #             irc.send_message(channel, "I am going for a sleep. But I will be back soon. Till then save yourself from NSA")
            #             irc.stop()
                
            #     elif word in bad_words:
            #         warn_msg = "This is warning {name}, next time you will be thrown out and I will also ask NSA to breach your privacy which they love to :|".format(name=name)
            #         irc.send_message(channel, warn_msg)
            #         print('warning sent !!')
            #         break



    except Exception:
        print('Something is wrong. NSA is watching you')
    
    
    