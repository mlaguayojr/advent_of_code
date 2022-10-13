# --- Day 5: Doesn't He Have Intern-Elves For This? ---

class NiceString:
    
    def __init__(self, value :str):
        self.value = value.rstrip()

    def has_three_vowels(self) -> bool:
        """
        Contains at least 3 vowels
        """
        vowels = { "a": 0, "e": 0, "i": 0, "o": 0, "u": 0 }

        for letter in list(self.value):
            try:
                vowels[letter] += 1
            except Exception as e:
                # not a vowel
                pass

        return ( sum(vowels.values()) >= 3 )

    def has_letter_twice_in_a_row(self) -> bool:
        """
        Contains at least one letter that appears twice in a row,
        """

        for index in range(0, len(self.value)):
            try:
                current_letter = self.value[index]
                next_letter = self.value[index + 1]

                if current_letter == next_letter:
                    return True

            except Exception as e:
                pass
        
        return False

    def has_bad_pairs(self) -> bool:
        bad_pairs = [ "ab", "cd", "pq", "xy"]

        for pair in bad_pairs:
            if pair in self.value:
                return True

        return False

    def is_nice(self) -> bool:
        """
        Logic for solution to part one of puzzle
        """
        return (
            self.has_letter_twice_in_a_row()
            and self.has_three_vowels()
            and not(self.has_bad_pairs())
        )

    def has_duplicate_pair(self) -> bool:
        """
        It contains a pair of any two letters that appears at least twice in the string without overlapping
        """
        pairs = {}

        for index in range(0, len(self.value)):
            key = self.value[index:index+2]
            
            if key in pairs.keys():
                pairs[key] += 1
            else:

                if len(key) == 2:
                    pairs[key] = 0

        # print(pairs)
        return ( sum(pairs.values()) >= 1 )

    def has_one_letter_gap(self) -> bool:
        """
        It contains at least one letter which repeats with exactly one letter between them
        """
        pairs = {}

        for index in range(0, len(self.value)):
            key = self.value[index:index+3]

            if len(key) != 3:
                continue

            if key in pairs.keys():
                pairs[key] += 1
            else:
                pairs[key] = 0

        # print(pairs)

        mirror_count = 0

        for pair in pairs.keys():
            if str(pair).endswith(str(pair)[0]):
                mirror_count += 1

        return (mirror_count >= 1)

    def is_nice2(self) -> bool:
        return (
            self.has_one_letter_gap()
            and self.has_duplicate_pair()
        ) == True

if __name__=="__main__":

    # Read puzzle input
    words = []
    with open("puzzle_input.txt") as f:
        words = f.readlines()
    
    # answer for puzzle
    part_one = 0
    part_two = 0

    for word in words:
        a = NiceString(word)
        is_nice = a.is_nice()
        is_nice2 = a.is_nice2()

        if is_nice:
            part_one += 1

        if is_nice2:
            part_two += 1
        
        # print(a.value, " ", is_nice2)

    print("part_one", part_one)
    print("part_two", part_two)