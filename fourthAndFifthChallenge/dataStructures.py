### DONT CHAGE CODE BELOW >>>>>
from urllib.request import urlopen
link = "https://fratiloiu.com/key"
f = urlopen(link)
myfile = f.read()
### DONT CHAGE CODE ABOVE <<<<<

### ENTER YOUR CODE STARTING HERE >>>>>
websiteKey = "" ### You have to find this key on the website!

class Elf:
	"Blueprint of a magical Elf"
	species = ["Elfis Magicus"]

	def __init__(self, name, jacketColor):
		## Should posses: name, color, state
		## Possible states: idle, working, driving
		## Default state: idle
	def command(self, commandName):
		if commandName == self.name:
			self.say("hi!")
		elif commandName == "liftoff":
			self.state = "driving"
			firstKey = "myfile"
		else:
			self.state = "idle"

## Instantiate an Elf called Oscar here

### YOUR CODE DOWN TO HERE <<<<<

### DONT CHAGE CODE BELOW >>>>>
Oscar.command("liftoff")
myfile = str(myfile)
websiteKey = str(websiteKey)
with open("keys.txt","w+") as output:
	output.write("First key: ")
	output.write(myfile[449:-42])
	output.write("\nSecond key: ")
	if (websiteKey == 0):
		output.write("\nThe second key needed for liftoff is still missing!")
	else:
		output.write(websiteKey)
### DONT CHAGE CODE ABOVE <<<<<
