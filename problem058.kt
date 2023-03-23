import java.util.*
import kotlin.math.*

var oddSquares = ArrayList<Int>()

fun generateSquares(upToNthSquare: Int) {
    for (i in 1..upToNthSquare) {
        if(i%2 != 0){
         oddSquares.add(i*i)
        }
    }
}

fun isPrime(num: Int): Boolean{
    if(num < 3){ return false }
    var flag = false
    for (i in 2..num / 2) {
        if (num % i == 0) {
            flag = true
            break
        }
    }

    if (!flag){
        return true
    }
    return false
}

fun generateSpiral(upToNumber: Int): Double {
    
    //var spiral = mutableListOf<MutableList<Int>>()    
    var layers = ceil(upToNumber.toDouble().pow(0.5)).toInt()
    if(layers % 2 == 0){
        layers++
    }
    val midpoint = floor(layers/2.0).toInt()
    
    val numsOnDiagonal = layers*2-1
    var primeCount = 0
    
    
    // Populating the spiral with empty lists
    for (i in 1..layers) {
        //spiral.add(MutableList(layers){0})
    }
    
    var row = midpoint
    var col = midpoint
    var increment = 1
    var direction = "u"
    var whichSquare = 3
    
    //spiral[row][col] = 1
    col++
    //spiral[row][col] = 2
        
    for (i in 3..upToNumber) {
        
        //println("dir: $direction")
        when(direction) {
            "r" -> col++
            "u" -> row--
            "l" -> col--
            "d" -> row++
        }
        //spiral[row][col] = i
        
        //println("$col $row")
        //println(spiral)
        
        if(col == whichSquare+midpoint-1-increment && row == midpoint-increment) {
            if(isPrime(i)){ primeCount++ }
            direction = "l"
        } else if (col == midpoint-increment && row == midpoint-increment){
            if(isPrime(i)){ primeCount++ }
            direction = "d"
        } else if (col == midpoint-increment && row == whichSquare+midpoint-1-increment){
            if(isPrime(i)){ primeCount++ }
            direction = "r"
        } else if (col == whichSquare+midpoint-increment){
            if(isPrime(i)){ primeCount++ }
            whichSquare+=2
            increment++
            direction = "u"
        }
          
    }
    
    val primePercentage = (primeCount.toDouble()/numsOnDiagonal.toDouble())*100
    
    println("${primeCount}/${numsOnDiagonal} (~$primePercentage%)")
    return primePercentage 
    
    //for (layer in spiral) {
        //println(layer)
    //}
        
}

fun main() {
    val generateTo = 1000000
    generateSquares(generateTo)
    val countOfSquares = oddSquares.size-1
    
    for (i in 1..countOfSquares) {
        val primePercentage = generateSpiral(oddSquares.get(i))
        println("")
        if(primePercentage < 10){
            println(ceil(oddSquares.get(i).toDouble().pow(0.5)).toInt())
            break
        }
    }
    
    
}
