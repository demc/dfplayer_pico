from dfplayer import DFPlayer
from random import randint

print("-----------------")
print(" Derrick's DFPlayer MP3 ")
print("-----------------")

mp3 = DFPlayer(1, 4, 5)
#mp3.EnableLoopAll()

# Get number of files saved to / of sd card
count = mp3.GetFilesCount()
print("File count: " + str(count))

# Pick a random file index
file_index = randint(0, count)
print("Playing: " + str(file_index));

# Play file
mp3.PlaySpecific(file_index)