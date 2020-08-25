import synonyms


class FindSyns(object):

    def __init__(self):
        pass

    @staticmethod
    def rec_func(word, *sen):
        if sen:
            return synonyms.compare(word, sen[0])
        else:
            return synonyms.nearby(word)


if __name__ == "__main__":
    fs = FindSyns()
    print(fs.rec_func('旗帜引领方向', '道路决定命运'))
    print(fs.rec_func('人脸')[0])

    print(fs.rec_func('人脸')[0])
    print(fs.rec_func('人脸')[0])
