import java.math.*

fun main() {
    val p = BigInteger("28433").multiply(2.toBigInteger().pow(7830457)).plus(1.toBigInteger()).toString()
    print(p.substring(p.length-10, p.length))
}
