class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // If the strings are not the same length, they can't be anagrams
        if (s.length !== t.length) return false;

        const char_dict = {};

        // Count characters in string s
        for (let char of s) {
            char_dict[char] = (char_dict[char] || 0) + 1;
        }

        // Compare against string t
        for (let char of t) {
            if (char_dict[char]) {
                char_dict[char] -= 1;
                if (char_dict[char] === 0) {
                    delete char_dict[char];
                }
            } else {
                // If char doesn't exist in char_dict or has been depleted, return false
                return false;
            }
        }

        // If there are no extra characters left, it's an anagram
        return Object.keys(char_dict).length === 0;
    }
}
