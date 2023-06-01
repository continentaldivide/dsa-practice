/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const dictionary = {};
  for (const letter of s) {
    if (!dictionary[letter]) {
      dictionary[letter] = 1;
    } else {
      dictionary[letter]++;
    }
  }
  
  for (const letter of t) {
    if (!dictionary[letter]) {
      return false;
    } else {
      dictionary[letter]--;
    }
  }

  for (const key in dictionary) {
    if (dictionary[key] !== 0) {
      return false;
    }
  }

  return true;
};
