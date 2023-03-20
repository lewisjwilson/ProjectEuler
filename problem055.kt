import java.math.BigInteger

fun isPalindromic(number: BigInteger): Boolean {
    val s = number.toString()
    return (s == s.reversed())
}

fun palindrome(number: BigInteger): BigInteger {
    return number.toString().reversed().toBigInteger()
}

fun main() {
    val MAX_ITERATIONS = 50
    var lychrelCount = 0
    
    baseNumberLoop@ for (i in 1..10000){
        var toCheck = i.toBigInteger()
        iterativeLoop@ for (iter in 1..MAX_ITERATIONS){
            if(isPalindromic(toCheck) && iter != 1){
                break@iterativeLoop
            } else if(iter == MAX_ITERATIONS){
                lychrelCount++
                //println("$i is a lychrel number!")
            } else {
                toCheck = toCheck.plus(palindrome(toCheck))
            }
        }
    }
    println("There are $lychrelCount Lychrel Numbers below 10000")
}
