import numpy as np
import tensorflow as tf
import io

INPUT_DATA_PATH = '../../../dataset/nlp/shakespeare.txt'


def load_inputs():
    # load raw inputs
    with io.open(INPUT_DATA_PATH, encoding='utf-8') as fp:
        text = fp.read().lower()
        print text

    chars = sorted(list(set(text)))
    print('total chars:', len(chars))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))

    print char_indices
    print indices_char


if __name__ == '__main__':
    load_inputs()