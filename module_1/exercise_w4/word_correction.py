import streamlit as st


def load_vocab(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def get_levenshtein_distance(token1, token2):
    distances = [[0] * (len(token2) + 1) for i in range(len(token1) + 1)]

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1 - 1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]


def main():
    vocabList = load_vocab('./data/vocab.txt')
    st.title('Word Correction using Levenshtein Distance')
    world = st.text_input('Enter a word:')

    if st.button("Compute"):
        leven_distances = dict()
        for vocab in vocabList:
            leven_distances[vocab] = get_levenshtein_distance(world, vocab)

        sorted_dst = dict(sorted(leven_distances.items(), key=lambda x: x[1]))
        corrected_word = list(sorted_dst.keys())[0]
        st.write('Corrected word:', corrected_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabList)

        col2.write('Distances:')
        col2.write(sorted_dst)


main()
