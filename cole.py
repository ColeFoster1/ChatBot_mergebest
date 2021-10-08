import random
import re
from baseChat import BaseChat,addChatObject

class coleChat(BaseChat):
  def chat(self, text):

    greetingOptions = ["hello", "hi", "hey", "sup", "greetings"]

    byeOptions = ["bye", "goodbye", "cya", "adios"]
    
    myFavorites = {"color": "blood", 
                  "food": "the souls of children",
                  "activity": "homicide!",
                  "cheese": "chedder"}
                  
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace(".", "")
    text = text.replace("?", "")

    words = text.split(" ")

    textLower = text.lower()

    myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
    if myMatchObject:
      favoriteIndex = myMatchObject.group(4)
      return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])

    for word in words:
      if word.lower() in greetingOptions:
        return random.choice(greetingOptions).capitalize()

    if word.lower() in byeOptions:
      return random.choice(byeOptions).capitalize()

    if word.lower() == "bee":
      return "According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."

    numbers = text.split("*")
    print (numbers)
    if numbers[0].isnumeric():
      return int(numbers[0])*int(numbers[1])


    numbers = text.split("+")
    print (numbers)
    if numbers[0].isnumeric():
      return int(numbers[0])+int(numbers[1])

  
    return None

chatObject = coleChat()
addChatObject(chatObject)
