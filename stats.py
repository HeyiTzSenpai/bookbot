def count_num_of_words(text):
    words = text.split()
    count = 0

    for word in words:
        count += 1

    return count


def count_num_of_diff_char(text):
    count_dic = {}

    for char in text:
        if char.isalpha():

            if char.lower() not in count_dic:

                count_dic[char.lower()] = 1

            elif char.lower() in count_dic:
                count_dic[char.lower()] += 1

    return count_dic
