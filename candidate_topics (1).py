import argparse
import json
import csv
import re
from collections import Counter
import math




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('annotated_file')
    args = parser.parse_args()
    
    annotated_file = args.annotated_file  
    
    topics = ['p', 't', 'r', 'w', 'e', 'c', 'o']
    candidates_topics = {'t':{topic:0 for topic in topics},
                         'j':{topic:0 for topic in topics},
                         'b':{topic:0 for topic in topics}}
    
    reader = csv.reader(open(annotated_file,'r', encoding='utf-8'), delimiter='\t') 
        
    is_header = True
    for line in reader:
        if is_header:
            is_header = False
            continue  

        name, title, coding, mentioned_candidate, upvote_ratio, ups, score, num_comments, total_awards_received = line
        #print(title, coding, mentioned_candidate, candidates_topics[mentioned_candidate][coding])
        candidates_topics[mentioned_candidate][coding] += 1
    
    for cand in candidates_topics:
        cand_topics = candidates_topics[cand]
        sorted_topics = {topic: counts for topic, counts in sorted(cand_topics.items(), key=lambda item:item[1], reverse=True)}
        print(cand, sorted_topics)

    
if __name__ == '__main__':
        main()
