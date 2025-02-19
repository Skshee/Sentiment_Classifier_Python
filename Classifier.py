# Function to remove all the punctuation marks from the tweets as they're not words
def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word


positive_words = []
negative_words = []

# Read positive words from file
with open("assets/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# Read negative words from file
with open("assets/negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Function to get all the positive words from the tweet
def get_pos(word):
    positive=0
    l=strip_punctuation(word.lower())
    list1 = l.split()
    for i in positive_words:
        for j in list1:
            if(i==j):
                positive=positive+1
    return positive

# Function to get all the negative words from the tweet
def get_neg(word):
    negative=0
    l=strip_punctuation(word.lower())
    list2 = l.split()
    for i in negative_words:
        for j in list2:
            if(i==j):
                negative = negative+1
    return negative

# Appending the output to file : resulting_data.csv 
# Format : Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score respectively
TwitterFile = open("assets/project_twitter_data.csv","r")
resultFile = open("resulting_data.csv","w")
resultFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
resultFile.write("\n")
linesTwitter = TwitterFile.readlines()
noHeader = linesTwitter.pop(0)
for lines in linesTwitter:
    lst = lines.strip().split(',')
    resultFile.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], get_pos(lst[0]), get_neg(lst[0]), (get_pos(lst[0])-get_neg(lst[0]))))    
    resultFile.write("\n")