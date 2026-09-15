class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let mapS = new Map();
        let mapT = new Map();

        for (let str of s) {
            if (mapS.has(str)) {
                mapS.set(str, mapS.get(str) + 1);
            } else {
                mapS.set(str, 0);
            }
        }
        for (let str of t) {
            if (mapT.has(str)) {
                mapT.set(str, mapT.get(str) + 1);
            } else {
                mapT.set(str, 0);
            }
        }

        if (mapS.size !== mapT.size) {
            return false;
        }

        for (let [k, v] of mapS) {
            if (!(mapT.get(k) == v)) {
                return false;
            }
        }

        return true;
    }
}
