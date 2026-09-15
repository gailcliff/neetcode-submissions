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

        // const countMap = new Map();

        // for (const strS of s) {
        //     countMap.set(strS, (countMap.get(strS) ?? 0) + 1);
        // }
        // for (const strT of t) {
        //     countMap.set(strT, (countMap.get(strT) ?? 0) - 1)
        // }

        // for (const count of countMap.values()) {
        //     if (count !== 0) {
        //         return false;
        //     }
        // }
        // return true;

        let s2 = [...s].sort().join("");
        let t2 = [...t].sort().join("");

        return s2 === t2;
    }
}
