
  
# eventually we may want to implement a plugin manager like this:
# https://www.guidodiepen.nl/2019/02/implementing-a-simple-plugin-framework-in-python/
#
# this will make it easier for students to add chatObjects without having to call
# addChatObject() and without us ever having to modify the imports in main.py.  
# The problem, though, is that the chatObjects would all have to be
# initialized using the same parameters.

CHAT_OBJECTS = []

def addChatObject(chatObject):
  CHAT_OBJECTS.append(chatObject)

class BaseChat:
  def chat(self, text):
    return None

  def help(self):
    return []
