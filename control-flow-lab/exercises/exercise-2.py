# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase=input("please enter a word or phrase:")
if phrase == "quit":
        print("thank you for playing")
else:
    print("What you entered is", len(phrase), "characters long")

# CREATED INFINETLY RUNNING LOOP WITH THE BELOW SO PLAYED IT SAFE WITH THE ABOVE WHICHS ANSWERS 1 & 2

# while inp !="quit":
#     print("What you entered is", len(phrase), "characters long")
# else:
#   print("thank you word or phrase")