from flask import Flask, request, json
from skpy import Skype, SkypeChats, SkypeGroupChat,SkypeMsg
import base64
import traceback

from utilities import add_thousand_seperator, translate_room_name

app = Flask(__name__)


@app.route('/SkypeNotifier/<room_name>',methods=['POST'])
def grafanaSkype(room_name):
    username = "user_name"
    password = "password"
    skype_connect = Skype(username, password)
    chat_id=translate_room_name(skype_connect,room_name)
    data = request.json
    try:
        msg=''
        msg=msg+'\n'
        url=str(data['ruleUrl'])
        msg=msg+SkypeMsg.link(url,data['title'])
        msg=msg+'\n'
        evals=data['evalMatches']

        for i in range(0,len(evals)):
            value=evals[i]['value']
            if  isinstance(value,int):
                value=add_thousand_seperator(value)
            extra_msg='\n '+SkypeMsg.bold(evals[i]['metric'])+' '+str(value)+'\n '
            msg += extra_msg

        #chat_id = '19:9ef2e91063114050898b4f468b04428a@thread.skype'
        channel = skype_connect.chats.chat(chat_id)
        channel.sendMsg("<at id=\" * \">all</at> \n"+msg, rich=True)

    except Exception as e:
        print("An exception occurred")
        print(e)
        traceback.print_exc()
    return data



@app.route('/')
def hello():
    return 'Grafana Listener\n Use SkypeNotifier URI to receive messages on Skype on alerts'



if __name__ == '__main__':
    app.run(debug=True)