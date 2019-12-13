### HINT: Sorting is very useful here ###
with open("anagramList.txt", 'r') as file:
    input = file.readlines()
    result = []
                        ### INSERT YOUR CODE FROM HERE ###

                        ### TO HERE                    ###

### DONT CHANGE THIS LINE
with open("outAnagram.txt","w+") as output:
    output.write(str(result))