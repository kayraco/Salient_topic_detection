import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('f1')
    parser.add_argument('f2')
    # parser.add_argument('f3')
    # parser.add_argument('f4')
    # parser.add_argument('f5')
    # parser.add_argument('f6')
    parser.add_argument('outputfile')
    
    args = parser.parse_args()
    
    f1 = args.f1
    f2 = args.f2
    # f3 = args.f3
    # f4 = args.f4
    # f5 = args.f5
    # f6 = args.f6
    
    outputfile = args.outputfile
    
    filenames = [f1, f2]
    #filenames = [f1, f2, f3, f4, f5, f6]
    
    with open(outputfile, 'w', encoding='utf-8') as outputfile:
        for fname in filenames:
            with open(fname, 'r', encoding='utf-8') as inputfile:
                is_header = True
                if fname == filenames[0]:
                    is_header = False
                for line in inputfile:
                    if is_header:
                        is_header = False
                        continue
                    
                    outputfile.write(line)
    


if __name__ == '__main__':
    main()  
    
    
