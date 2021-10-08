import mccurdy
import austin
import gavin
import cole

from baseChat import CHAT_OBJECTS

def chat(text):
  if text.lower() == "help":
    helpStrings = []
    for obj in CHAT_OBJECTS:
      helpStrings.extend(obj.help())

    return "I know how to do the following:\n  * " + "\n  * ".join(helpStrings)

  for obj in CHAT_OBJECTS:
    response = obj.chat(text)

    if response:
      return response

    
  return "I'm still learning.  Try saying hello."

if __name__ == "__main__":
  while(True):
    userInput = input(">>> ")
    print(chat(userInput))