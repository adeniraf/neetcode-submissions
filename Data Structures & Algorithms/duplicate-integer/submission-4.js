class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let nums_dict = {}
        for (let num of nums){
            if (num in nums_dict) {
                return true
            } else {
                nums_dict[num] = 1
            }
        }

        return false
    }
}
