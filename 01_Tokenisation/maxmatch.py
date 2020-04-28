import sys

#get the file and read each line to get the word
#then put each word into a dictionary.
def makeDictionary(filePath):

    with open(filePath, "r") as f:

        sample = f.read()

        sample = sample.split('\n')
    #print(sample)
    return sample

# we read each sentence and get the length of the sentence.
# Then get the part of the sentence from biggest to smallest
# until we find the word which is in dictionary.
def maxmatch(sentence, dictionary):
    if len(sentence) == 0:
        return ''
 
    for i in reversed(range(2, len(sentence) + 1)):
        left = sentence[i : len(sentence)]

        if (sentence[0 : i] in dictionary) or sentence[0 : i].isdigit():
            return sentence[0 : i] + '\n' + maxmatch(left, dictionary)

    left = sentence[1 : len(sentence)]
    return '\n' + maxmatch(left, dictionary)
       
#it the argument is not enought
if len(sys.argv) != 2 :
    print('error: not enough args\nWe need 2 argument!!!')

else :
    dictionary = makeDictionary(sys.argv[1])

    content = sys.stdin.read()
    lines = content.split('\n')
    # we get the sentence and check if there are any words in  dictionary
    # When we find the word in dictionary, we write it out.
    for key in lines:
        tokens = maxmatch(key, dictionary)
        sys.stdout.write(tokens)
