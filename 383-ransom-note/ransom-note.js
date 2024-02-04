/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
   for (const char of magazine) {
    ransomNote = ransomNote.replace(char, "");
  }
  
  if (!ransomNote) return true;
  else return false;
};