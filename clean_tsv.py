import argparse
import re
import csv


def clean(in_file, output_file):
    with open(output_file, 'a') as out_file:
        lines = [line.strip() for line in open(in_file)]
        header = 'Name\ttitle\tcoding\tmentioned_candidate\tupvote_ratio\tups\tscore\tnum_comments\ttotal_awards_received\n'
        out_file.write(header)

        counter = 0  # counts the number of posts we end up
        counter0 = 0  # counts the number of posts that refer to both Trump and Biden
        counter1 = 0  # counts the number of posts that refer to Trump multiple times in one sentence
        counter2 = 0  # counts the number of posts that refer to Biden multiple times in one sentence
        counter3 = 0  # counts the number of posts that refer to Trump
        counter4 = 0  # counts the number of posts that refer to Biden

        for x in lines:
            match2 = re.search('Donald Trump Jr|Ivanka Trump|Hunter Biden|Trump Jr.', x)
            if match2: continue;
            match = re.search('Trump|Biden', x)
            if match:
                out_file.write(x + '\n')
                counter += 1

            if ('Trump' in x) & ('Biden' in x): counter0 += 1
            if x.count('Trump') >= 2: counter1 += 1
            if x.count('Biden') >= 2: counter2 += 1
            for m in re.finditer('Trump', x): counter3 += 1
            for m in re.finditer('Biden', x): counter4 += 1

    print("for " + output_file)
    print("Total number of posts: " + str(counter))
    print("Number of posts that refer to both Trump and Biden: " + str(counter0))
    print("Number of posts that refer to Trump: " + str(counter3 - counter0 - counter1))
    print("Number of posts that refer to Biden: " + str(counter4 - counter0 - counter2))
    print("Number of posts that refer to Trump multiple times in one sentence: " + str(counter1))
    print("Number of posts that refer to Biden multiple times in one sentence: " + str(counter2))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--outfile', help='output filepath')
    parser.add_argument('infile', help='name of the input file to be cleaned')
    args = parser.parse_args()
    output_file = args.outfile
    in_file = args.infile

    clean(in_file, output_file)


if __name__ == '__main__':
    main()
