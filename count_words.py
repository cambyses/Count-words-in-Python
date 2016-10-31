def count_words(s, n):
    
    words = s.split(" ")
    # TODO: Count the number of occurences of each word in s
    counters = {}
    for word in words:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    top = sorted(counters.iteritems(), key=lambda d:(-d[1],d[0]))

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = top[:n]
    return top_n
 
 
def test_run():

    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)
 
 
if __name__ == '__main__':
    test_run()
