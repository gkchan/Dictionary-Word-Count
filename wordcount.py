
# Functions
def word_count(file_name = "test.txt"):
    """ Prints number of space-separated words in a given file"""

    words = {}

    with open(file_name) as data:
        for line in data:
            line = line.strip().split()
            for item in line:
                words[item] = words.get(item, 0) + 1

    return words


def write_to_file(big_data, output_file_name = "output_stat.txt"):
    with open(output_file_name, "w+") as output:
        for key, value in big_data.iteritems():
            output.write("%s %s\n" % (key, value))


while True:
    data_choice = raw_input("Print result on screen or in file (S/F):")

    file_name = raw_input("Type the file_name to work on or Enter for default choice: ")

    if data_choice == "S":
        counted_words = word_count("test.txt")
        for key, value in counted_words.items():
            print key, value
        break

    elif data_choice == "F":
        if file_name == "":
            file_name = "twain.txt"

        big_counted_words = word_count(file_name)
        write_to_file(big_counted_words)
        print "Check out output in file"
        break
    else:
        continue

# cat file_name - prints out file on screen
# touch file_name - creates new file
# with open(file_name) as f: - autoclosable interface for files
# for i, line in enumerate(open(file_name)): - iterate over lines in file_name
# print string, string - "," puts whitespace between arguments
