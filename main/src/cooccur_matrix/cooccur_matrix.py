import logging
import argparse
import pickle
import word2vec


def parse_args():
    parser = argparse.ArgumentParser(description='Cooccurrence matrix (clusters)')
    parser.add_argument('--model', metavar='M', type=str,
                    help='model file')
    parser.add_argument('--clusters', metavar='CL', type=str,
                    help='cluster file')
    parser.add_argument('--corpus', metavar='CO', type=str,
                    help='corpus file (unsegmented)')
    parser.add_argument('--output', '-o', metavar='O', type=str, default='cooccur.txt',
                    help='output file name')
    parser.add_argument('-n', metavar='N', type=int, default=2,
                    help='n-gram')

    return parser.parse_args()

def save_matrix(cooccur_matrix, output):
    with open(output, 'wb') as fout:
        pickle.dump(cooccur_matrix, fout)

def load_pickle(f):
    with open(f, 'rb') as fin:
        data = pickle.load(fin)

    return data 

def get_cooccur_matrix(model, clusters, corpus_filename, n=2):
    # init matrix - (n-1)_distances x num_of_clusters x num_of_clusters
    size = len(set(clusters))
    cooccur_matrix = [[[0 for _ in range(size)] for _ in range(size)] for _ in range(n-1)]

    with open(corpus_filename, 'r') as fin:
        for l_no, line in enumerate(fin):
            if l_no % 1000 == 0:
                logging.info('Processing line {}...'.format(l_no))

            # slide window over each line
            for w_no in range(len(line) - n):
                window = line[w_no:w_no+n]
                char_idxs = []
                cluster_idxs = []

                # get cluster info in each window
                for char in window:
                    try:
                        char_idx = model.ix(char)

                        char_idxs.append(char_idx)
                        cluster_idxs.append(clusters[char_idx])

                    except Exception as e:
                        continue

                # accumulate cooccur info
                w_size = len(char_idxs)
                for step in range(n-1):
                    for i, cluster_idx in enumerate(cluster_idxs):
                        for next_cluster_idx in cluster_idxs[i+1:w_size:step+1]:
                            cooccur_matrix[step][cluster_idx][next_cluster_idx] += 1

    return cooccur_matrix

def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_args()

    model = word2vec.load(args.model)
    clusters = load_pickle(args.clusters) 

    cooccur_matrix = get_cooccur_matrix(model, clusters, args.corpus, n=args.n)
    
    save_matrix(cooccur_matrix, args.output)

if __name__ == '__main__':
    main()
