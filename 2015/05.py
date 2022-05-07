# Day 5: Doesn't He Have Intern-Elves For This?

puzzle = None

class NiceString:

    def __init__(self, word :str):
        self.word = word
        
    def isNice(self) -> bool:
        # print(nicestring.vowel_check)
        # print(nicestring.repeating_letters_check)
        # print(nicestring.sequential_letter_check)

        check1 = self.check_vowels()
        check2 = self.check_repeating_letters()
        check3 = self.check_sequential_letters()

        return (check1 and check2 and check3)

    def check_vowels(self) -> bool:
        vowels = ["a","e","i","o","u"]

        vowel_count = 0
        for letter in list(self.word):
            
            if letter in vowels:
                vowel_count += 1

        return (vowel_count >= 3)

    def check_repeating_letters(self) -> bool:
        result = 0

        for letter_index in range(0, len(self.word) - 1):
            letter = word[letter_index]
            next_letter = word[letter_index + 1]

            if next_letter == letter:
                result += 1

        return result >= 1

    def check_sequential_letters(self) -> bool:
        result = 0

        for combo in ["ab", "cd", "pq", "xy"]:
            if combo in self.word:
                result += 1

        return not(result > 0)

with open("puzzle_input.txt") as file:
    puzzle = file.readlines()

# Solution to Part One of puzzle
nice_count = 0
for word in puzzle:

    nicestring = NiceString(word.strip())

    if nicestring.isNice():
        nice_count += 1

print(nice_count)

# Solution to Part Two of puzzle

# not done yet