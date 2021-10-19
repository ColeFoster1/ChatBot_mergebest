import re
import random 
from baseChat import BaseChat, addChatObject

class LeiloshChat(BaseChat):
  def chat(self, text):

    byeOptions = [ "bye", "byebye", "byeeeeeeee", "see ya", "goodbye", "goodbye good sameritan", "bye looser"] 

    myFavorites = {"animal":"puffins", 
                  "dessert": "kunefe",
                  "student": "Definitly not you (✿≧_≦)⌐╦╦═─",
                  "movie": "Thor Ragnarok",}

    myWhoObjects = {"hero":"My Mom",
                "Mom":"Frida Kahlo",
                "Dad":"You",
                "bestfriend":"Ana Kasparian",
                "archnemisis":"Luigi",}


    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    textLower = text.lower()   

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      favoriteIndex = myMatchObject.group(4)
      if favoriteIndex in myFavorites:
        return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])

    myWhoObjects = re.match("who(('s)|([\s]+is))[\s]+your[\s]+(.+)", textLower) 
    if myWhoObjects:
      WhoIndex = myWhoObjects.group(5)
      if WhoIndex in myWhoObjects: 
        return "My {} is {}".format(WhoIndex, myWhoObjects[WhoIndex])


    if text == "how do i contact a teacher":
        return "your already on google chat you idiot. :( you should look up their last name and see if you can find them. and because your so dumb you probaly won't figure out you need to make sure it's a set high email. duhhhhh "
      

    if text == "im lost":
      return "well get unlost"

    if text == "dick":
      return "hello Mr. Greyson"
    
    import random 

    helpOptions = ["wut" , "why" , "this sucks"]
    
    awnserOptions = ["Contact a teacher idiot" , "uhhh get an adult already!" , "your brain is aperently not working because all you need to do is ASK FOR HELP!!!"]

    words = text.split(" ")
    for word in words:
      if word.lower() in helpOptions:
        return random.choice(awnserOptions).capitalize()

    words = text.split(" ")
    for word in words:
      if word.lower() in byeOptions:
        return random.choice(byeOptions).capitalize()
  
  def help(self):
    return ["yo"]
    
chatObject = LeiloshChat()
addChatObject(chatObject) 