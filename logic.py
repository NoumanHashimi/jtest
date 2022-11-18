def my_func(string):
    all_words = string.split()
    first_word= all_words[0]
    if first_word != "Hello":
        raise Exception("Hello Not Found!")
    else:
        print(string)
