class Solution {
    /**
     * @param {string[]}
     * @return {string}
     */
    longestCommonPrefix(strs) {
        // strs.sort((a, b) => a.length < b.length);

        const shortestStr = strs[0];
        const subStrs = [];

        for (let i = 0; i < shortestStr.length; i++) {
            subStrs.push(shortestStr.slice(0, i+1));
        }

        let result = "";
        for (const subStr of subStrs) {
            if (strs.every(stri => stri.startsWith(subStr))) {
                result = subStr;
            } else {
                break;
            }
        }

        return result;
    }
}