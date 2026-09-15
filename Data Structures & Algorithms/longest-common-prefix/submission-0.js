class Solution {
    /**
     * @param {string[]}
     * @return {string}
     */
    longestCommonPrefix(strs) {
        strs.sort((a, b) => a.length < b.length);

        const prefixCountMap = new Map();

        const shortestStr = strs[0];
        const subStrs = [];

        for (let i = 0; i < shortestStr.length; i++) {
            subStrs.push(shortestStr.slice(0, i+1));
        }

        for (const subStr of subStrs) {
            if (strs.every(stri => stri.startsWith(subStr))) {
                prefixCountMap.set(subStr, subStr.length);
            }
        }

        let bestK = null, bestV = 0;

        for (const [k, v] of prefixCountMap) {
            if (v > bestV) {
                bestK = k;
                bestV = v;
            }
        }

        return bestK ?? "";
    }
}