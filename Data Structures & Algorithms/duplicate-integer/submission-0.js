class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let n = nums.length;
        const numMap = new Map();

        for (let i = 0; i < n; i++) {
            if (numMap.has(nums[i])) {
                return true;
            } else {
                numMap.set(nums[i], nums[i])
            }
        }
        return false;
    }
}
