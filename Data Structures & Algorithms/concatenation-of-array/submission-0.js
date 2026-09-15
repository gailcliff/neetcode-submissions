class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        let n = nums.length;
        let concatenated = new Array(n * 2);
        

        for (let i = 0; i < n; i++) {
            concatenated[i] = nums[i];
            concatenated[i+n] = nums[i];
        }

        return concatenated;
    }
}
