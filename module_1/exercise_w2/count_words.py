import gdown
import os


def count_words_in_file() -> dict[str, int]:
    path = 'module_1/download_content/P1_data.txt'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    gdown.download(
        'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko', output=path)

    f = open(path, 'r')
    result: dict[str, int] = {}
    for l in f.readlines():
        words = l.replace('\n', '').split(' ')
        for word in words:
            word = word.lower()
            if word in result:
                result[word] += 1
                continue

            result[word] = 1

    f.close()
    return result
