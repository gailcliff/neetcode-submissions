class Solution {
    /**
     * @param {string[]}
     * @return {string}
     */
    longestCommonPrefix(strs) {
        let prefix = "";

  for (let i = 0; i < strs[0].length; i++) {
    if (strs.every(s => s[i] === strs[0][i])) {
      prefix += strs[0][i];
    } else {
      break;
    }
  }

  return prefix;
    }
}