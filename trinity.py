
import random
import re
from baseChat import BaseChat, addChatObject


class trinitychat(BaseChat):
  def chat(self, text):
    greetingOptions = ["hello", "hi", "hey",  "yo", "hola", "namaste",  "heyyy",  "howdy",  "helo", "heyy"] 
    byeOptions  = ["bye", "godspeed", "goodbye", "farewell",  "peace",  "peace out",  "bye bye",  "adios"]
    myFavorites = {"animal":"a cat  =^._.^= ∫",
                  "dessert":"cookies",
                  "color":"purple",
                  "movie":"Ex Machina......don't judge",
                  "candy":"Twix",
                  "song":"Paranoid Android by Radiohead", 
                  "video game":"DBH."}


    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    
    textLower = text.lower()

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      favoriteIndex = myMatchObject.group(4)
      if favoriteIndex in myFavorites:
        return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])

    words = text.split(" ")
    for word in words:
      if word.lower() in greetingOptions:
        return random.choice(greetingOptions).capitalize()

    
    return None

  def help(self):
    return["goodbye"]


chatObject = trinitychat()
addChatObject(chatObject)




        