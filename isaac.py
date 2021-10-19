import random
import re 
from baseChat import BaseChat, addChatObject


badOptions = ["fuck", "shit", "ass", "damn"]

class IsaacChat(BaseChat):
  def chat(self, text):
    endOptions=["bye", "goodbye", "sayonara", "farewell", "see ya", "see you later", "byebye", "godspeed", "ciao", "cheerio"]


    
    myFavorites = {"animal":"a dog", 
                    "dessert": "dark chocolate",
                    "student": "you, of course!",
                    "pokemon": "porygon-z",
                    "game": "metal gear soid 3",
                    "show": "hellsing ultimate"}

    myLeastFavorites = {"animal":"a spider", 
                    "dessert": "anything with peanut butter",
                    "student": "i love them all!",
                    "pokemon": "pidove",
                    "game": "kingdom hearts",
                    "show":"darling in the franxx"}
      

    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    words = text.split(" ")

    for word in words:
      if text.lower() in endOptions:
        return random.choice(endOptions).capitalize() 
      elif text.lower() == "how are you":

        return "I am good"
      
      
      for word in words:  
        if word.lower() in badOptions:
          return "please watch your language"
      
      textLower = text.lower()

      myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
      if myMatchObject:
          favoriteIndex = myMatchObject.group(4)
          if favoriteIndex in myFavorites:
            return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])
      myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+least[\s]+favorite[\s]+(.+)", textLower)
      if myMatchObject:
          favoriteIndex = myMatchObject.group(4)
          if favoriteIndex in myFavorites:
            return "My least favorite {} is {}".format(favoriteIndex, myLeastFavorites[favoriteIndex])

      return None

  def help(self):
    return["what is your favorite","what is your least favorite","how are you"]

chatObject = IsaacChat()
addChatObject(chatObject)
