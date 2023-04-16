with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        words = line.split()
        print("В строке {} {} слов(а)".format(i+1, len(words)))
    print("Всего строк: {}".format(len(lines)))