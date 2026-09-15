class Solution {
    /**
     * @param {string[]}
     * @return {string}
     */
    longestCommonPrefix(strs) {
        
        // const firstStr = strs[0];
        // const subStrs = []

        // for (let i = 0; i < firstStr.length; i++) {
        //     subStrs.push(firstStr.slice(0, i+1));
        // }

        // let longestPrefix = "";
        // for (const subStr of subStrs) {
        //     if (strs.every(stri => stri.startsWith(subStr))) {
        //         longestPrefix = subStr;
        //     }
        // }

        // return longestPrefix;

        let longestPrefix = "";
        const firstStr = strs[0];

        for (let i = 0; i < firstStr.length; i++) {
            if (strs.every(stri => stri[i] === firstStr[i])) {
                longestPrefix += firstStr[i];
            } else {
                break;
            }
        }

        return longestPrefix;
    }
}