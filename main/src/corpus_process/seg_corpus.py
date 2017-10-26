import argparse


# Parse args
parser = argparse.ArgumentParser(description='Segment Chinese corpus into characters')
parser.add_argument('input', metavar='FI', type=str,
                    help='file to be segmented')
parser.add_argument('--output', '-o', metavar='FO', type=str,
                    help='output file name')

args = parser.parse_args()


# Segment corpus, each line contains a phrase with characters separated by space
with open(args.input, 'r') as fin:
    with open(args.output, 'w') as fout:
        for line in fin:
            phrases = line.split('p')[1:-1]
            for phrase in phrases:
                chars = ' '.join(list(phrase))

                # punctuation as virtual character
                fout.write('p ')

                fout.write(chars)

                # punctuation as virtual character
                fout.write(' p')
                fout.write('\n')
