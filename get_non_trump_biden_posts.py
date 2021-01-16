import argparse
import re
import csv

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('inputfile')
    parser.add_argument('outputfile')
    
    args = parser.parse_args()
    
    inputfile = args.inputfile
    outputfile = args.outputfile
      
    
    with open(outputfile, 'w', encoding='utf-8') as f:
        f.write('Name\ttitle\tcoding\tmentioned_candidate\tupvote_ratio\tups\tscore\tnum_comments\ttotal_awards_received\n')
        input_reader = csv.reader(open(inputfile, 'r', encoding='utf-8'), delimiter='\t')
        is_header = True
        for line in input_reader:
            if is_header:
                is_header = False
                continue
            
            name, title, coding, mentioned_candidate, upvote_ratio, ups, score, num_comments, total_awards_received = line
            
            match2 = re.search('Donald Trump Jr|Ivanka Trump|Hunter Biden|Trump Jr.', title)
            if match2: 
                f.write(name + '\t' + title + '\t' + 'u' + '\t' + mentioned_candidate + '\t' + upvote_ratio + '\t' + ups + '\t' + score + '\t' + num_comments + '\t'+ total_awards_received + '\n')
            match = re.search('Trump|Biden', title)   # 'u' for unmentioned
            if match:
                continue
            else:
                f.write(name + '\t' + title + '\t' + 'u' + '\t' + mentioned_candidate + '\t' + upvote_ratio + '\t' + ups + '\t' + score + '\t' + num_comments + '\t'+ total_awards_received + '\n')

if __name__ == '__main__':
    main()  
    
            