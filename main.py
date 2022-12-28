print("===MAFIA NARRATOR HELPER===")
print()
print("In Mafia, there is someone who speaks as a narrator. The narrator is a player who is not a member of the mafia game, but tells the storyline, while the game is being played.")
print ()
print(" This program was created to help the Narrator tell the story with more creavity!")
print()
print("===Welcome to Mafia narrator helper!===")
print ("So, as narrator, it's your turn to tell the story of someone in the game who the mafia has targeted. Give me some details of the person who targeted. ")

Name = input ("Character name: ")

print("Great! Tell me more information, such as age, time period the story is in, a surreal setting this takes place at, a superpower, and quirky phrase they have.")

age = input("Age: ") 
      
gender = input ("Gender (He or She?): ") 

timePeriod = input("Time period: ")

setting = input ("Surreal setting: ")

superpower = input ("Superpower: ")

catchphrase = input ("Quirky catchphrase: ")

print() 
print("Great! Here's your story....")
print()
print(Name, " was targeted by the mafia. At the young age of only", age, "years old.")

print(gender, "was", "\033[31m", "killed.") 

print ("\033[37m", "It was around the time of", timePeriod, "in", setting, ".", "Unknowingly, the mafia did not know that", Name, "had superpowers. He had the power of", superpower, ".") 

print(Name, " was also known for his catchphrase, ", catchphrase, ".")

print()

print("All of a sudden, Param bursted forth using his", superpower, "power. He was able to escape. and he cried out", "\033[33m", catchphrase,) 

  