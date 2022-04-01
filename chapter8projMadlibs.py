import re

madlibFile = open('D:\\pythonSTUFF\\madlibTemplate.txt')
madlibContent = madlibFile.read()
print(madlibContent)
madlibFile.close()

ADJECTIVE = re.compile(r'ADJECTIVE')
NOUN = re.compile(r'NOUN') 
VERB = re.compile(r'VERB') 
ADVERB = re.compile(r'ADVERB')

for x in range(len(ADJECTIVE.findall(madlibContent))):
    print("Input adjective number "+str(x+1))
    userInput = input()
    madlibContent = ADJECTIVE.sub(userInput, madlibContent, count=1)

for x in range(len(NOUN.findall(madlibContent))):
    print("Input noun number "+str(x+1))
    userInput = input()
    madlibContent = NOUN.sub(userInput, madlibContent, count=1)

for x in range(len(VERB.findall(madlibContent))):
    print("Input verb number "+str(x+1))
    userInput = input()
    madlibContent = VERB.sub(userInput, madlibContent, count=1)

for x in range(len(ADVERB.findall(madlibContent))):
    print("Input adverb number "+str(x+1))
    userInput = input()
    madlibContent = ADVERB.sub(userInput, madlibContent, count=1)

print(madlibContent)
madlibResult = open('madlibResult.txt', 'a')
madlibResult.write(madlibContent+'\n')
madlibResult.close()


