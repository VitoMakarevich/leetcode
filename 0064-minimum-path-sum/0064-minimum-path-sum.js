/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    const xSize = grid[0].length
    const ySize = grid.length
    const sums = new Array(ySize)
    for (let i = 0; i < grid.length; i++) {
        sums[i] = new Array(xSize).fill(0)
    }
    const val = findPrice(xSize - 1, ySize - 1, xSize, ySize, sums, grid)

    return val
};

function isCorrectPos(i, j, xSize, ySize) {
    return i >= 0 && i < xSize && j >= 0 && j < ySize
}

function findPrice (i, j, xSize, ySize, sums, grid, curSum) {
    if(i == 0 && j == 0) return grid[0][0]
    const topJ = j - 1
    const leftI = i - 1
    let sumVars = []
    if(isCorrectPos(i, topJ, xSize, ySize)) {
        const sumVal = sums[topJ][i]
        if(sums[topJ][i] == 0)
            sums[topJ][i] = findPrice(i, topJ, xSize, ySize, sums, grid)
        sumVars.push(sums[topJ][i])
    }
    if(isCorrectPos(leftI, j, xSize, ySize)) {
        const sumVal = sums[j][leftI]
        if(sums[j][leftI] == 0)
            sums[j][leftI] = findPrice(leftI, j, xSize, ySize, sums, grid)
        sumVars.push(sums[j][leftI])
    }
    
    return Math.min(...sumVars) + grid[j][i] 
}