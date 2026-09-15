class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        const countMap = new Map();
        const majority = Math.floor((nums.length / 2));

        for (const num of nums) {
            countMap.set(num, (countMap.get(num) ?? 0) + 1)
        }

        for (const [k, v] of countMap) {
            if (v > majority) {
                return k;
            }
        }

        return 0;
    }
}
