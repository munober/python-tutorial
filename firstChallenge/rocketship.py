with open('rocketshipInput.txt', 'r') as file:
    mass = file.readlines() 
    fuel = []               ### INSERT YOUR CODE FROM HERE ###
    
                            ### TO HERE                    ###

### DONT CHANGE CODE BELOW
with open("outRocket.txt","w+") as output:
    output.write(str(totalFuel))