#define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere
#in the word. (Hint: remember the .replace() method for strings.)

#define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered
#positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are 
#of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

#define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative
#words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative
#words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

#write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number
#of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above,
#and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies,
#Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score
#(how positive or negative the text is overall) for each tweet. 

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(s):
    for c in punctuation_chars:
        s=s.replace(c,"")
    return s  

def get_neg(s):
    ss=strip_punctuation(s)
    t=ss.lower()
    st=t.split()
    c=0
    for i in st:
        if i in negative_words:
            c+=1
    return -c

def get_pos(s):
    ss=strip_punctuation(s)
    t=ss.lower()
    st=t.split()
    c=0
    for i in st:
        if i in positive_words:
            c+=1
    return c

f=open('project_twitter_data.csv','r')
rd=f.readline()
file=open('resulting_data.csv','w')
file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
file.write('\n')
for data in f.readlines():
    data1=data.split(",")
    row_string = '{},{},{},{},{}'.format(int(data1[1]),int(data1[2]),get_pos(data),get_neg(data),(get_pos(data)+get_neg(data)) )
    file.write(row_string)
    file.write('\n')
file.close()
f.close()
