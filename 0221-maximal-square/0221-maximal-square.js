/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    const memo = new Array(matrix.length)
    for(let i = 0; i < matrix.length; i++) {
        memo[i] = new Array(matrix[0].length)
    }
    for(let i = 0; i < matrix[0].length; i++) {
        memo[0][i] = matrix[0][i]
    }
    if(matrix.length == 0) return Math.max(...matrix[0])
    for(let i = 0; i < matrix.length; i++) {
        memo[i][0] = matrix[i][0]
    }
    for(let i = 1; i < matrix.length; i++) {
        for(let j = 1; j < matrix[0].length; j++) {
            if(matrix[i][j] === '0') memo[i][j] = 0
            else {
                memo[i][j] = Math.min(memo[i - 1][j], memo[i - 1][j - 1], memo[i][j - 1]) + 1
            }
        }
    }
    let max = -1
    for(let i = 0; i < matrix.length; i++) {
        for(let j = 0; j < matrix[0].length; j++) {
            if(memo[i][j] > max) max = memo[i][j]
        }
    }
    
    
    return max * max
};