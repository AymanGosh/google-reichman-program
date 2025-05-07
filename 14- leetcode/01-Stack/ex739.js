

function findNextHTempDay (dailyTempArr){
    let stack = [] 
    let res = new Array(dailyTempArr.length).fill(0) 

    for( let i = 0; i < dailyTempArr.length; i++ ){

        while( stack.length > 0 && dailyTempArr[stack[stack.length-1]] < dailyTempArr[i]){
            prev = stack.pop()
            res[prev] = i - prev
        }
        stack.push(i)
    }

    return res
}