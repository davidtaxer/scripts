def pig_latin(text):
  word = text.split()
  for word in text:
    # Create the pig latin word and add it to the list
    word.format({word[1:] + word[0] + "ay"})
    
    # Turn the list back into a phrase
  return word
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
