/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    var count = 0
    const sum = nums.map((key)=>
    {
        count = key+count
        return count
    })
    return sum
};