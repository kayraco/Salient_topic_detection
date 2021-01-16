import argparse
import json
import csv
import re
from collections import Counter
import math

def title_to_clean_words(title):
    words = re.sub('(\'s)|(\’s)|[^\w\s\-]+', '', title).strip(' ').split(' ')
    word_list = []
    for w in words:
        if w == '':
            continue
        word_list.append(w.lower())
    return word_list

# returns a dict of topic: [word_list]    
def load_topics_words(filename):
    topics = ['p', 't', 'r', 'w', 'e', 'c', 'o', 'u']
    topic_words = {topic: [] for topic in topics}
    
    reader = csv.reader(open(filename,'r', encoding='utf-8'), delimiter='\t') 
        
    is_header = True
    for line in reader:
        if is_header:
            is_header = False
            continue
                
        name, title, coding, mentioned_candidate, upvote_ratio, ups, score, num_comments, total_awards_received = line
        if coding in topics:
            clean_title_words = title_to_clean_words(title)
            topic_words[coding].extend(clean_title_words)
    return topic_words

def load_2000_posts_words(filename):
    word_list = []
    reader = csv.reader(open(filename,'r', encoding='utf8'), delimiter='\t') 
    
    is_header = True
    for line in reader:
        if is_header:
            is_header = False
            continue    
    
        name, title, coding, mentioned_candidate, upvote_ratio, ups, score, num_comments, total_awards_received = line
        clean_title_words = title_to_clean_words(title)
        word_list.extend(clean_title_words)
    return word_list
               
def count_word_occurrences(list):
    word_count_list = {}
    word_counts = Counter(list)
    for word in word_counts:
        word_count_list[word] = word_counts[word]
    return word_count_list  

# assume corpus is a dict of topic: [word_list]
def compute_total_word_counts(corpus):
    total_sum = 0
    for topic in corpus:
        topic_word_counts = sum(corpus[topic].values())
        total_sum += topic_word_counts
    #print(total_sum)
    return total_sum

def highest_score_words(word_scores, num_words):
    highest_score_words = [word for word in list(word_scores.keys())[:num_words]]
    return highest_score_words

def tf(word, topic_word_count):
    return topic_word_count[word]


# # of total categories/ # of categories has the w
def idf(word, topics_word_counts):   
    num_topics_has_w = 0
    for topic in topics_word_counts:
        if word in topics_word_counts[topic].keys():    
            num_topics_has_w += 1
    num_topics = len(topics_word_counts)
    idf = math.log(num_topics/num_topics_has_w)
    return idf

def highest_score_words(word_scores, num_words):
    highest_score_words = [word for word in list(word_scores.keys())[:num_words]]
    return highest_score_words

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('annotated_file') 
    args = parser.parse_args()
    
    annotated_file = args.annotated_file  # the raw file that contains 2000 posts
    
    unannotated_word_list = load_2000_posts_words(annotated_file)
    unannotated_word_counts = count_word_occurrences(unannotated_word_list)

    topics_words = load_topics_words(annotated_file)
    
    topics_word_counts = {}
    for topic in topics_words:
        topics_word_counts[topic] = count_word_occurrences(topics_words[topic])
      
    topics = ['p', 't', 'r', 'w', 'e', 'c', 'o', 'u']
    
    total_word_counts = compute_total_word_counts(topics_word_counts)
    
    topics_highest_10_words = {topic:[] for topic in topics}
    
    
    for topic in topics:
        topic_word_scores = {}
        topic_word_count = topics_word_counts[topic]
        for word in topic_word_count:
            topic_word_scores[word] = tf(word, topic_word_count) * idf(word, topics_word_counts)
        sorted_word_scores = {word: score for word, score in sorted(topic_word_scores.items(), key=lambda item:item[1], reverse=True)}
        topics_highest_10_words[topic] = highest_score_words(sorted_word_scores, 10)
    print(topics_highest_10_words)
        
if __name__ == '__main__':
        main()
