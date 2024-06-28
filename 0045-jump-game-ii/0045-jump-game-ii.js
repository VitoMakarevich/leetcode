/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let curPos = 0
    let numOfJumps = 0
    while(curPos < nums.length - 1) {
        if(curPos + nums[curPos] >= nums.length - 1) return numOfJumps + 1
        const curJumpLength = nums[curPos]
        const nextCandidates = nums.slice(curPos + 1, curPos + curJumpLength + 1)
        if(nextCandidates.length == 1) {curPos +=1; numOfJumps++; continue}
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
        numOfJumps++
    }
    
    return numOfJumps
};