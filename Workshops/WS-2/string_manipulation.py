s = input("Enter a sentence, I dare you:")

words = s.split(" ")
if len(words) > 1 or len(s.strip() < 5):
    print (f"Your sentence has {len(s)} characters")
   
    print (f"The highest alphabetical character is '{max(s)}' and the lowest is '{min(s)}'")
    print (f"The first five characters are '{s[:5]}' and the last five characters '{s[-5:]}'")
    print (f"The first five characters are '{s[:5]}' and the last five characters '{s[len(s)-5:]}'")

    print (f"The sentence in reverse is '{s[::-1]}'")       
    print (f"The sentence spoken quietly is '{s.lower()}'")
    print (f"The sentence shouted out amongst the treetops is '{s.upper()}'")
        
    c = input("Enter a character and I'll count if for you in from your sentence:")
    print (f"'{c}' occurs {s.count(c)} times")                                                                             

    print (f"The individual words in the sentence are: '{words}'")

    print (f"The shortest word is '{min(words, key=len)}' and the longest word is '{max(words, key=len)}'")

    newversion = s.replace(" ", "").lower()

    if newversion==newversion[::-1]:
        print ("The sentence is a palindrome.  It reads the same both forwards and backwards")
    else:
        print ("The sentence is not a palindrome.")
else:
    print ("Please enter at least two words and a minimum of 5 characters.")