text = '''You take a mortal man
And put him in control
Watch him become a god
Watch people's heads a'roll
A'roll, a' roll
Just like the Pied Piper
Led rats through the streets
We dance like marionettes
Swaying to the symphony
Of destruction
Acting like a robot
Its metal brain corrodes
You try to take its pulse
Before the head explodes
Explodes, explodes
Just like the Pied Piper
Led rats through the streets
We dance like marionettes
Swaying to the symphony
Just like the Pied Piper
Led rats through the streets
We dance like marionettes
Swaying to the symphony
Swaying to the symphony
Of destruction
The earth starts to rumble
World powers fall
A'warring for the heavens
A peaceful man stands tall
Tall, tall
Just like the Pied Piper
Led rats through the streets
We dance like marionettes
Swaying to the symphony
Just like the Pied Piper
Led rats through the streets
We dance like marionettes
Swaying to the symphony
Swaying to the symphony
Of destruction'''

def count_words(text):
   words = text.replace("\n"," ").replace("/"," ").split(" ")
   num_words = len(words)
   return num_words

num_words = count_words(text)

print(num_words)
