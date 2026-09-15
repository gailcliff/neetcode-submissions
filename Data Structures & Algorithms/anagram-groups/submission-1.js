class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    isAnagram(str1, str2) {
        if (str1.length !== str2.length) {
            return false;
        }

        const countMap = new Map();

        for (let i = 0; i < str1.length; i++) {
            countMap.set(str1[i], (countMap.get(str1[i]) ?? 0) + 1);
        }
        for (let i = 0; i < str2.length; i++) {
            countMap.set(str2[i], (countMap.get(str2[i]) ?? 0) - 1);
        }

        for (const val of countMap.values()) {
            if (val !== 0) {
                return false;
            }
        }

        return true;
    }
    groupAnagrams(strs) {        
        const anagramMap = new Map();
        const allAnagrams = []

        for (let i = 0; i < strs.length; i++) {
            let stri = [...strs[i]].sort().join("");
            
            if (anagramMap.has(stri)) {
                anagramMap.get(stri).push(strs[i]);
            } else {
                anagramMap.set(stri, [strs[i]]);
            }
        }

        for (const [k, v] of anagramMap) {
            allAnagrams.push(v);
        }
        return allAnagrams;
    }
}
