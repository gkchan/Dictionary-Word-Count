# put your code here.
def word_count(file_name):
    """ Prints number of space-separated words in a given file"""

    words = {}

    with open(file_name) as data:
        for line in data:
            line = line.strip().split()
            for item in line:
                words[item] = words.get(item, 0) + 1

    return words

print "Small data word count:"

counted_words = word_count("test.txt")
for key, value in counted_words.items():
    print key, value
print

raw_input()


def write_to_file(big_data, file_name):
    with open(file_name, "w+") as output:
        for key, value in big_data.iteritems():
            output.write("%s %s\n" % (key, value))

print "Bigger data word count:"

big_counted_words = word_count("twain.txt")

write_to_file(big_counted_words, "stat_for_twain.txt")

print "Check out stat_for_twain.txt"

# cat file_name - prints out file on screen
# touch file_name - creates new file
# with open(file_name) as f: - autoclosable interface for files
# for i, line in enumerate(open(file_name)): - iterate over lines in file_name
# print string, string - "," puts whitespace between arguments
