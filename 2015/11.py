class Password:

    def __init__(self, password :str):
        self.value = list(password)

    def increment(self, position):
        if self.value[position] == "z":
            self.value[position] = "a"
            self.increment(position-1)
        else:
            letter = self.value[position]
            letter = ord(letter) + 1
            self.value[position] = chr(letter)

    def generate_next_password(self):
        print("Previously:", self.value)
        self.increment(len(self.value)-1)
        print("Currently:", self.value)

    def matches_requirements(self) -> bool:
        results = [ self.rule1(), self.rule2(), self.rule3() ]
        print("Rule 1:", results[0])
        print("Rule 2:", results[1])
        print("Rule 3:", results[2])
        
        if False in results:
            print("Password does not meet requirements")
            return False
        
        print("Password meets requirements")
        return True

    def rule1(self) -> bool:
        """
        Passwords must include one increasing straight of at least three letters.
        like 'abc', 'bcd', or 'cde'
        """
        passing = False

        for index in range(0, len(self.value) - 2):
            [char1, char2, char3] = self.value[index:index+3]
            
            check1 = ( (ord(char2) - ord(char1)) == 1)
            check2 = ( (ord(char3) - ord(char2)) == 1)
            
            if not(passing):
                passing = ( (check1 == True) and (check2 == True) ) 
                
                if passing:
                    print(char1, char2, char3)

        return passing

    def rule2(self) -> bool:
        """
        Passwords may not contain the letters 'i', 'o', or 'l'.
        """
        passing = True

        for bad_letter in ["i", "o", "l"]:

            if bad_letter in self.value:
                passing = False
                break

        return passing

    def rule3(self) -> bool:
        """
        Passwords must contain at least two different, non-overlapping pairs of letters.
        like 'aa', 'bb', or 'zz'
        """
        passing = []

        for index in range(0, len(self.value) - 1):
            [char1, char2] = self.value[index:index+2]

            if char1 == char2:
                if not(char1 in passing):
                    passing.append(char1)

        return len(passing) >= 2

if __name__=="__main__":

    password = Password("hxbxwxba")
    password.generate_next_password()
    
    def part_one_solution():
        result = password.matches_requirements()
        
        while(not(result)):
            print(result)

            if not(result):
                password.generate_next_password()
                result = password.matches_requirements()
        print("Next Best Password:", "".join(password.value))
        

    def part_two_solution():
        part_one_solution()
        password.generate_next_password()
        part_one_solution()


    part_one_solution()