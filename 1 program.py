# Assumptions:

# The file contains one sentence per line.
# The racial slurs are provided as a set of words.


def calculate_profanity_degree(sentence, racial_slurs):
    sentence = sentence.lower()
    words = sentence.split()
    total_words = len(words)
    profane_words = len([word for word in words if word in racial_slurs])
    profanity_degree = profane_words / total_words if total_words > 0 else 0
    return profanity_degree


def analyze_file(file_path, racial_slurs):
    with open(file_path, 'r') as file:
        for line in file:
            sentence = line.strip()
            profanity_degree = calculate_profanity_degree(
                sentence, racial_slurs)
            print(f"Sentence: {sentence}")
            print(f"Profanity Degree: {profanity_degree}")
            print()


# Assuming the racial slurs are provided as a set of words
racial_slurs = {'slur1', 'slur2', 'slur3'}

file_path = 'tweets.txt'  # Replace with the actual path to your file
analyze_file(file_path, racial_slurs)
