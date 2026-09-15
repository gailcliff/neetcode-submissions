class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

  const counts = new Map();

  for (const char of s) counts.set(char, (counts.get(char) ?? 0) + 1);
  for (const char of t) counts.set(char, (counts.get(char) ?? 0) - 1);

  for (const count of counts.values()) {
    if (count !== 0) return false;
  }

  return true;
    }
}
