def valueGetter(item):
    return item[1]

def again():
    doItAgain = input('''Do you want to use it again?
Y or y, for Yes 
N or n, for No ''')
    if(doItAgain.upper() == 'Y'):
        topThreeWordsAppearing()
    elif(doItAgain.upper() == 'N'):
        print("See you soon!")
    else:
        again()

def topThreeWordsAppearing():
    inputSTR = input("Whrite the word that you want separated by spaces, to show the top three word that appeared the most: ")
    wordList = list(map(str, inputSTR.split()))
    myDic = {}
    for word in wordList:
        myDic[word] = 1 + myDic.get(word,0)
    sortedDic = sorted(myDic.items(), key = valueGetter, reverse = True)
    firstIndex = [sublist[0] for sublist in sortedDic]
    print(f"Output: {firstIndex[0:3]}")
    again()

topThreeWordsAppearing()