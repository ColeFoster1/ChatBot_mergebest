import random
import re
from baseChat import BaseChat, addChatObject


class McCurdyChat(BaseChat):
  def chat(self, text):
    greetingOptions = ["hello", "hi", "hey", "yo", "hola", "namaste"]

    myFavorites = {"animal":"a dog", 
                  "dessert": "peanut butter balls",
                  "student": "you, of course!",
                  "movie": "Die Hard",}


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
      
      if word.lower() == "bye":
        return "see ya"
    
    return None

  def help(self):
    return["What is your favorite ",
            "hello"]


chatObject = McCurdyChat()
addChatObject(chatObject)
