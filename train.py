from textgenrnn import textgenrnn

textFile = input("Enter txt file name: ")
numEpochs = int(input("Enter number of epochs: "))

pathToFile = "\\Users\yoonp\independentCS\MLTEST\textFiles\\" + textFile + ".txt"


t = textgenrnn()


t.train_from_file(pathToFile, num_epochs=numEpochs)