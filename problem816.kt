import kotlin.math.*
import java.math.*

fun generateNext(n: Int): Int {
    val power = n.toDouble().pow(2.0)
    val bigDec = BigDecimal.valueOf(power)
    val bigInt = bigDec.toBigInteger()
    val mod = bigInt.mod(50515093.toBigInteger())
    val output = mod.toInt()
    return (output)
}

fun distance(coord1: Pair<Int, Int>, coord2: Pair<Int, Int>): Double {
    val xDiff = (coord1.toList().get(0) - coord2.toList().get(0)).toDouble()
    val yDiff = (coord1.toList().get(1) - coord2.toList().get(1)).toDouble()
    return sqrt(xDiff.pow(2) + yDiff.pow(2))
}

fun main() {
    
    
    // Pair<x, y> (Coordinates)
    val pNArray = ArrayList<Pair<Int, Int>>()
    
    // Starting at 0,  k = n+1
    val k = 15
    
    // This is s0
    var sN = 290797
    
    for (i in 1..k){
    	var sN_1 = generateNext(sN)
        pNArray.add(Pair(sN, sN_1))
        sN = generateNext(sN_1)
    }
    
    var smallest = Double.MAX_VALUE
    
    for (pair1 in pNArray){
        for (pair2 in pNArray){
            val dist = distance(pair1, pair2)
           	if (dist == 0.0) { continue }
            if (dist < smallest){
                smallest = dist
                println("$smallest")
            }

        }
    }
    
}
