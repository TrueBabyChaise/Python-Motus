import color as clr
import random as rd
import signal as sg


def signalHandler(sig, frame):
    """
    Signal handler for Ctrl-C only
    :param sig:
    :param frame:
    :return:
    """
    print("Ctrl-C")
    exit(0)


def selectRandomWord(listWord):
    """
    Select a random word from the list given as parameter
    :param listWord: str
    :return: str
    """
    rd.seed(None)
    return listWord[rd.randint(0, len(listWord) - 1)]


def getWordsList(file):
    """
    Select a random word from the list given as parameter
    :param file: str
    :return: list[str]
    """
    wordList = []
    with open(file, mode="r", encoding='utf-8') as f:
        wordList = f.read().splitlines()
    return wordList


def getInputUser(wordChoose: str):
    """
    Get the user input, it will loop until the input is correct.
    :param wordChoose: str
    :return: list[str]
    """
    inputUser = ""
    
    while not inputUser.isalpha() or len(inputUser) != len(wordChoose):
        inputUser = input("Choissisez un mot de " + str(len(wordChoose)) + " lettre(s) : ")
    return inputUser


def writeOutput(inputStr: str, wordChoose: str):
    """
    Format the user input to put color on it to show him where he's wrong.
    :param inputStr: str
    :param wordChoose: str
    :return: str
    """
    letterCounter = {a: wordChoose.count(a) for a in wordChoose}
    outputResponse = [a for a in inputStr]
    
    for index in range(len(inputStr)):
        if inputStr[index] in letterCounter.keys() and letterCounter[inputStr[index]] == 0:
            outputResponse[index] = clr.Blue + outputResponse[index]
            continue
        if inputStr[index] == wordChoose[index]:
            outputResponse[index] = clr.Red + outputResponse[index]
            letterCounter[inputStr[index]] -= 1
        elif inputStr[index] in wordChoose:
            letterCounter[inputStr[index]] -= 1
            outputResponse[index] = clr.Yellow + outputResponse[index]
        else:
            outputResponse[index] = clr.Blue + outputResponse[index]
    return outputResponse


def gameLoop(wordChoose: str):
    """
    The game loop, it'll loop until the player wins or the players runs out of chance to guess
    :param wordChoose: str
    :return:
    """
    inputStr = ""
    chances = 8
    while inputStr != wordChoose and chances >= 0:
        inputStr = getInputUser(wordChoose)
        output = writeOutput(inputStr, wordChoose)
        print(*output, clr.Color_Off)
        print("Chance(s) remaining :", chances)
        chances -= 1
    if chances > 0:
        print("You won !")
    else:
        print("You lost, the word was :", wordChoose)


def main():
    """
    main function called if file is launched
    :return:
    """
    sg.signal(sg.SIGINT, signalHandler)
    gameLoop(selectRandomWord(getWordsList("list")))
    return 0


if __name__ == '__main__':
    main()
