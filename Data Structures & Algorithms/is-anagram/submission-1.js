class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const sorted_s = [...s].sort().join('')
        const sorted_t = [...t].sort().join('')

        if (sorted_s !== sorted_t) {
            return false
        }
        return true
    }
}
