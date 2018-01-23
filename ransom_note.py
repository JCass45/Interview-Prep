def valid_ransom_note(ransom_note, article):
    article_words = {}
    for word in article:
        if word in article_words.keys():
            article_words[word] += 1
        else:
            article_words[word] = 1

    for word in ransom_note:
        if word not in article_words.keys() or article_words[word] == 0:
            return False

        article_words[word] -= 1

    return True


if __name__ == '__main__':
    test_ransom_note = ['This', 'is', 'a', 'ransom', 'note', 'note']
    test_article = ['This', 'is', 'news', 'article',
                    'weather', 'a', 'forecast', 'ransom', 'note', 'note']
    print(valid_ransom_note(test_ransom_note, test_article))
