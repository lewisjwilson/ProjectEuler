import java.math.BigInteger

fun sumDigits(number: BigInteger): Int {
    var digitSum = 0
    val s = number.toString()
    for(i in 1..s.length){
        digitSum += s.substring(i-1, i).toInt()
    }
    return digitSum
}

fun main() {
    
    var large = 0
    var largeA = 0
    var largeB = 0
    
    
    for (a in 1..100){
        for (b in 1..100){
            val aBI = a.toBigInteger()
            val power = aBI.pow(b)
            val sum = sumDigits(power)
            if(sum>large){
                large = sum
                largeA = a
                largeB = b
            }
        }
    }
    println("The sum of the digits of $largeA * $largeA  is $large.")
}
