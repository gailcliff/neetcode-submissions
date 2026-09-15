class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }

        let countMap = new Map();

        for (let strS of s) {
            countMap.set(strS, (countMap.get(strS) ?? 0) + 1);
        }
        for (let strT of t) {
            countMap.set(strT, (countMap.get(strT) ?? 0) - 1)
        }

        for (const count of countMap.values()) {
            if (count !== 0) {
                return false;
            }
        }
        return true;
    }
}
