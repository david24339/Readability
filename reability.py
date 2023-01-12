#define and implement the main function of our program
def main():
    #Prompt the user for the text
    text = input("Text: ")

    #Calculate the number of letter and store the result in the variable letters
    letters = count_letters(text)

    #Calculate the number of words and store the result in the variable words
    words = count_words(text)

    #Calculate the number of sentences and store the result in the variable sentences
    sentences = count_sentence(text)

    #Calculate the average number of letter per 100 words and store it in a variable
    L = Avgletterper100(letters, words)

    #Calculate the average number of letter per 100 words and store it in a variable
    S = Avgsentencesper100(sentences, words)

    #Compute the Coleman-Liau index using the formula below
    index = 0.0588 * L - 0.296 * S - 15.8

    #if the index is more than or equal to 16, then output grade 16+
    if round(index) >= 16:
        print("Grade 16+")

    #if the index is less than 0, then output before grade 1
    elif index < 0:
        print("Before Grade 1")

    #otherwise out the grade wich equal to the index
    else:
        print("Grade ", round(index))


# Implematention of the count_letter function
def count_letters(text):
    letter = 0
    #Iterate through each character and check whether it is a letter
    for character in text:
        #if the character is alphabetic, increment letter variable by 1
        if character.isalpha():
            letter += 1
    #return the number of letter
    return letter

# Implementation of the count_words function
def count_words(text):
    words = 1
    #Iterate through each character and check whether for spaces
    for character in text:
        #Increment the words variable by 1 each time a space is found
        if character == " ":
            words += 1
    #Return the number of words
    return words

#Implementation of the count_sentence function
def count_sentence(text):
    sentence = 0
    # Itereate throught each character and check for '.', '!' or '?'
    for character in text:

        # increment by 1 the sentence variable each time we find a '.', '!' or '?'
        if character == '.' or character == '!' or character == '?':
            sentence += 1
    #return the number of sentences
    return sentence

# Implement a function that calculates L
def Avgletterper100(letter,  word):
    return letter / word * 100

# Implement a function that calculates S
def Avgsentencesper100(sentence, word):
    return sentence / word * 100

main()