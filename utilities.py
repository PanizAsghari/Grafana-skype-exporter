from skpy import Skype,chat

def add_thousand_seperator(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))


def translate_room_name(skype_connect,room_name):
   recent_chats=skype_connect.chats.recent()
   for chat in recent_chats:
       if 'topic' in dir(recent_chats[chat]):
           group_name=recent_chats[chat].__getattribute__('topic')
           if group_name==room_name:
               return chat
