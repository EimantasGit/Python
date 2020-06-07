punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
positive_words = []
positive_count = 0
negative_words = []
negative_count = 0

file_twitter = open("project_twitter_data.csv")
all_text = file_twitter.read()
#Creating a file for results
result_data = open("resulting_data.csv", "w")

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#Remove punctuation
def strip_punctuation(words):
    for y in punctuation_chars:
        words = words.replace(y, "")
    return words

#Count all positive words
def get_pos(all_text):
    text_data = strip_punctuation(all_text)
    text_data = text_data.lower()
    count = 0
    list_words = text_data.split()
    
    for word in list_words:
        for y in positive_words:
            if word == y:
                count += 1
    return count

#Count all negative words
def get_neg(all_text):
    text_data = strip_punctuation(all_text)
    text_data = text_data.lower()
    count = 0
    list_words = text_data.split()
    
    for word in list_words:
        for y in negative_words:
            if word == y:
                count += 1
    return count

#Writing results to csv file
def write_results(result_data):
    result_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
  
    line_list = file_twitter.readlines() #Creating a list of lines
    remove_header = line_list.pop(0) #Deleting first line because it's gibberish
    
    for line in line_list:
        list_data = line.strip().split(',')
        print(list_data)
        result_data.write("{}, {}, {}, {}, {}\n".format(list_data[1], list_data[2], get_pos(list_data[0]), get_neg(list_data[0]), (get_pos(list_data[0]) - get_neg(list_data[0]))))
#############################################################

positive_count = get_pos(all_text)
negative_count = get_neg(all_text)
write_results(result_data)
