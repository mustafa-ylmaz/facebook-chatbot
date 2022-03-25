from fbchat import Client, log
from fbchat.models import *
import apiai, codecs, json
import string    
import random

class chatS(Client):
    
    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = "73580e41006b059a335338699382063ece5e607d" # Dialogflow Google api key 
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request()
        self.request.lang = 'en'
        self.request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
        
    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None, **kwargs):
        
        # self.markAsRead(author_id)

        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))

        self.apiaiCon()

        msgText = message_object.text

        self.request.query = msgText

        response = self.request.getresponse()

        obj = json.load(response)

        #reply = obj['result']['fulfillment']['speech']

        S = 10  
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
        msj = "Edit your message" + str(ran)

        if author_id != self.uid:
            self.send(Message(text=msj), thread_id=thread_id, thread_type=thread_type)

        self.markAsDelivered(author_id, thread_id)

Client = chatS("mail@mail.com", "password")
Client.listen()