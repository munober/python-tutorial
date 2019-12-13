with open('rocketshipInput.txt', 'r') as file:
    mass = file.readlines() 
    totalFuel = []               ### INSERT YOUR CODE FROM HERE ###
    
                            ### TO HERE                    ###

### DONT CHANGE CODE BELOW
with open("outRocket.txt","w+") as output:
    output.write(str(totalFuel))