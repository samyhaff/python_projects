from fbchat import Client, log
from fbchat.models import *

class Jarvis(Client):
    def onMessage(self, author_id=None, message_object=None, thread_type=TreadType.USER, **kwargs):
        self.markAsRead(author_id)
     
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))
        msgText = message_object.text
     
        reply = 'Hello world'
     
        if auther_id!=self.uid:
            self.send(Message(text=reply), thread_id=author_id, thread_type=thread_type)
     
        self.markAsDelivered(auther_id, thread_id)

client = Jarvis("marc.partensky@free.fr", "CRAM69")
client.listen()
