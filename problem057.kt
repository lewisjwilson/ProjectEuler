import java.util.*
import java.math.*

// Carefully inspecting cases k0, k1, k2 and k3, we can find a relationship
// 
// k0 = 3/2
// k1 = 7/5
// k2 = 17/12
// k3 = 41/29
// 
// Let's say n(k) is the numerator at k
// and d(k) is the denominator at k
// 
// We see that n(k+1) = 2*d(k) + n(k)
// and d(k+1) = d(k) + n(k)

fun rootTwo(iterations: Int): String {
    if(iterations<=0){ return "Invalid Number of Iterations" }
    
    var fractionArr = ArrayList<BigInteger>(2)
    fractionArr.add(3.toBigInteger())
    fractionArr.add(2.toBigInteger())
        
    for (i in 2..iterations){
        val n = 2.toBigInteger().multiply(fractionArr.get(1)).plus(fractionArr.get(0))
        val d = fractionArr.get(1).plus(fractionArr.get(0))
        fractionArr.set(0, n)
        fractionArr.set(1, d)
    }
    
	return "${fractionArr.get(0)}/${fractionArr.get(1)}"
}

fun main(){
    
    var count = 0
    for (i in 1..1000) {
        val rootTwo = rootTwo(i)
        val nLen = rootTwo.split("/")[0].length
        val dLen = rootTwo.split("/")[1].length
        if(nLen>dLen){ count++ }
    }
    
    println("The number of expansions in which the # of numerator digits")
    println("exceeds the # of denominator digits, is $count")
    
}
