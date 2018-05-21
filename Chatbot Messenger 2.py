from fbchat import  Client, log
from fbchat.models import *
from Fonctions import *

class Jarvis(Client):        

    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        # Mark message as read
        self.markAsRead(author_id)

        # Message Text
        msgText = message_object.text
  
        # Get reply from the list
        reply = Répondre(msgText)

        # Send message
        if author_id!=self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        # Mark message as delivered
        self.markAsDelivered(author_id, thread_id)


# Create an object of our class, enter your email and password for facebook.
client = Jarvis("marc.partensky@free.fr", "CRAM69")

# Listen for new message
client.listen()
