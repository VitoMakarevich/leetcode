/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    const memo = new Array(obstacleGrid.length)
    let obstFound = false
    for(let i = 0; i < obstacleGrid.length; i++) {
        const isObst = obstacleGrid[i][0] == 1
        if(!obstFound && isObst) {
            obstFound = true
        }
        memo[i] = obstFound ? 0 : 1
    }
    
    for(let j = 1; j < obstacleGrid[0].length; j++) {
        for(let i = 0; i < obstacleGrid.length; i++) {
            if(i == 0) {
                memo[0] = obstacleGrid[i][j] == 1 ? 0 : memo[0]
                continue
            }
            memo[i] = obstacleGrid[i][j] == 1 ? 0 : (memo[i] + memo[i - 1])
        }
    }
    return memo[obstacleGrid.length - 1]
};