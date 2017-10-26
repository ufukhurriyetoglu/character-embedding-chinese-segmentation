import argparse
import re


# Parse args
parser = argparse.ArgumentParser(description='Clean Chinese corpus')
parser.add_argument('filename', metavar='F', type=str,
                    help='file to be cleaned')

args = parser.parse_args()


# Clean corpus
with open(args.filename) as f:
    for line in f:
        # punctuation at start of line (indicate seg)
        print('p', end='')

        # main content
        line_clean = re.findall(r'[\u4e00-\u9fff]+', line)
        line_rm_space = 'p'.join(line_clean) 
        for c in line_rm_space:
            print(c, end='')
        
        # punctuation at end of line (indicate seg)
        print('p')
