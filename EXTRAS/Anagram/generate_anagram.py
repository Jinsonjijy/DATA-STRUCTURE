from collections import Counter


def find_anagrams(word):
    """
    Generates all unique anagrams of a given word using backtracking.
    """

    # Step 1: Count character frequencies
    char_counts = Counter(word)
    result = []

    def backtrack(current_path):
        # Base case: if the current path is the desired length, we found an anagram
        if len(current_path) == len(word):
            result.append("".join(current_path))
            return

        # Step 3: Loop through unique characters
        for char in sorted(char_counts.keys()):  # sorted() is optional, ensures consistent order
            # Step 4: Choose and act
            if char_counts[char] > 0:
                # Add character to our current permutation
                current_path.append(char)
                char_counts[char] -= 1

                # Step 5: Recurse
                backtrack(current_path)

                # Step 6: Backtrack (undo the choice)
                char_counts[char] += 1
                current_path.pop()

    backtrack([])
    return result


# --- Examples ---
print(f'Anagrams of "CAT": {find_anagrams("CAT")}')
# Output: Anagrams of "CAT": ['ACT', 'ATC', 'CAT', 'CTA', 'TAC', 'TCA']

print(f'Anagrams of "APP": {find_anagrams("APP")}')
# Output: Anagrams of "APP": ['APP', 'PAP', 'PPA']