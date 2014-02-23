"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""

def common_words(filename):
    f = open(filename)
    text = f.read().lower()
    import re
    words = re.findall(r"\w+", text)
    from collections import Counter
    commonlist = Counter(words).most_common()
    words_list = []
    for t in commonlist:
        words_list.append(t[0])
    print words_list
    f.close()

def common_words_min(filename, min_chars):
    f = open(filename)
    text = f.read().lower()
    import re
    words = re.findall(r"\w+", text)
    from collections import Counter
    commonlist = Counter(words).most_common()
    words_list = []
    for t in commonlist:
        words_list.append(t[0])
    print [word for word in words_list if len(word) >= min_chars]
    f.close()

def common_words_tuple(filename, min_chars):
    f = open(filename)
    text = f.read().lower()
    import re
    words = re.findall(r"\w+", text)
    from collections import Counter
    commonlist = Counter(words).most_common()
    print [tup for tup in commonlist if len(tup[0]) >= min_chars]
    f.close()

def common_words_safe(filename, min_chars):
    try:
        f = open(filename)
        text = f.read().lower()
        import re
        words = re.findall(r"\w+", text)
        from collections import Counter
        commonlist = Counter(words).most_common()
        print [tup for tup in commonlist if len(tup[0]) >= min_chars]
        f.close()
    except IOError:
        print "File not found!"