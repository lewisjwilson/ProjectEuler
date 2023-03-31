import kotlin.math.*
import java.math.*

fun checkPowers(base: Int): Int {
    
    var output = 0
    
    for (power in 1..100){
        val n = base.toBigInteger().pow(power)
        val digits = n.toString().length
        if(power == digits){
            println("${n} = ${base}^${power}, digits: $digits")
            output++
        }
        
    }
    return output
}

fun main() {
    var result = 0
    for (base in 1..1000){
    	result += checkPowers(base)
    }
    println("$result n-digit positive integers exist which are also an nth power.")
}
