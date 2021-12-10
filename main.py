import color as clr
import random as rd


def selectRandomWord(listWord) -> str:
    rd.seed(None)
    return listWord[rd.randint(0, len(listWord) - 1)]

def getWordsList() -> list[str]:
    wordList = []
    with open("list", mode="r", encoding='utf-8') as f:
        wordList = f.read().splitlines()
    return wordList

def getInputUser(wordChoose: str):
    inputUser = ""

    while not inputUser.isalpha() or len(inputUser) != len(wordChoose):
        inputUser = input("Choissisez un mot de " + str(len(wordChoose)) + " lettre(s) : ")
    return inputUser

def writeOutput(inputStr: str, wordChoose: str):
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

def main():
    gameLoop(selectRandomWord(getWordsList()))
    return 0


def gameLoop(wordChoose: str):
    inputStr = ""
    while inputStr != wordChoose:
        inputStr = getInputUser(wordChoose)
        output = writeOutput(inputStr, wordChoose)
        print(*output, clr.Color_Off)


if __name__ == '__main__':
    main()
