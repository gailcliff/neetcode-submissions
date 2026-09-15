class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        const originalLen = nums.length;
        let idx = nums.indexOf(val);
        let deletedTimes = 0;

        while (idx !== -1) {
            nums.splice(idx, 1);
            idx = nums.indexOf(val);
            deletedTimes++;
        }

        return originalLen - deletedTimes;
    }
}
