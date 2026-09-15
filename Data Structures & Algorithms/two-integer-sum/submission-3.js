class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = new Map();

        for (let i = 0; i < nums.length; i++) {
            let complement = target - nums[i];

            if (seen.has(complement)) {
                if (complement < nums[i] || complement === nums[i]) {
                    return [seen.get(complement), i]
                } else {
                    return [i, seen.get(complement)];
                }
            }

            seen.set(nums[i], i);
        }

        return [];
    }
}
