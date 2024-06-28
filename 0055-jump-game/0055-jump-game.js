/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let curPos = 0
    while(curPos < nums.length - 1) {
        const curJumpLength = nums[curPos]
        if(curJumpLength == 0) {
            return false
        }
        const nextCandidates = nums.slice(curPos + 1, curPos + curJumpLength + 1)
        if(nextCandidates.length == 1) {curPos +=1; continue}
        console.log(nextCandidates)
        const maxDistWithCandidate = nextCandidates
          .map((val, idx) => ({val: idx + val, idx: idx + 1}))
          .reduce((prev, cur) => {
            if(cur.val > prev.val) {
                return cur
            }
            return prev
          })
        curPos += maxDistWithCandidate.idx
    }
    
    return true
};