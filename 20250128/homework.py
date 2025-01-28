handle = open( 'para.txt' , 'r' )
paragraph = handle.read()
wordList = paragraph.split()
wordCount = { }

for word in wordList:
 #method One
 wordCount[word] = wordCount.get( word , 0 ) + 1
 #Method Two
 # if word in wordCount:
 #  wordCount[word] = wordCount[word] + 1 
 # else:
 #  wordCount[word] = 1
  
print(wordCount)