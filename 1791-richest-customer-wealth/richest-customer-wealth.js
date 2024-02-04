/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function (accounts) {

  var richest = 0
  for (i = 0; i < accounts.length; i++) {
    var sum = 0
    for (j = 0; j < accounts[i].length; j++) {
      sum = sum + accounts[i][j]
      if (sum > richest) {
        richest = sum
      }
    }
  }
  return richest
};