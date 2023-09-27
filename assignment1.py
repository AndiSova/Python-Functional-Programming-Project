with open("sherlock.txt", "r") as file:
    encryptedWords = file.read().split()
    decryptedWords = map(lambda w: w.translate(w.maketrans("!@#$%^&*", "sherlock")), encryptedWords)
    result = filter(lambda w: w[0] == 'a', decryptedWords)
    print(list(result))
