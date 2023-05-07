import java.io.File
import kotlin.collections.mutableListOf

fun main(){

    // Reading contents of the file    
    val fileContents = File("p059_cipher.txt").readText()  // String
    val dataStrArray = fileContents.split(",")
    val dataIntArray = dataStrArray.map{ it.toInt() }.toIntArray()
    

    // Checking possible lowercase keys
    var keyArray = intArrayOf(97, 97, 97)
    var keySum = keyArray.sum()
    
    while(keySum < 366){ // 122 + 122 + 122

        val decrypted = xORDecrypt(dataIntArray, keyArray)

        keyArray = nextKey(keyArray)
        keySum = keyArray.sum()

        if(decrypted.isEmpty()){ continue }

        val decryptedString = decrypted.map{ it.toChar() }.toString()

        println(decryptedString)    

    }


}

fun nextKey(key: IntArray): IntArray {

    var newKey = key

    val key0 = key.get(0)
    val key1 = key.get(1)
    val key2 = key.get(2)

    newKey.set(2, key2+1)

    if(key2>=122){
        newKey.set(1, key1+1)
        newKey.set(2, 97)
    }

    if(key1>=122){
        if(key0>=122){
            newKey.set(2, key2+1)
        } else if(key1!=key2) {
            newKey.set(2, key2+1)
        } else {
            newKey.set(1, 97)
            newKey.set(0, key0+1)
        }
    }

    return newKey

}

fun xORDecrypt(data: IntArray, key: IntArray): IntArray {

    var decrypted = intArrayOf()

    var keyIdx = 0
    var keyVal = key.get(keyIdx)
    for(c in data){

        val newVal = c.xor(keyVal)

        val valid = (newVal >= 97 && newVal <= 122) || // a-z
                (newVal >= 65 && newVal <= 90) ||  // A-Z
                (newVal >= 48 && newVal <= 57) || // 0-9
                (newVal == 32 || newVal == 44 || newVal == 46 || newVal == 63 || newVal == 33) || // <space> , . ? !
                (newVal == 59 || newVal == 45 || newVal == 92) || // ; - \
                (newVal == 40 || newVal == 41) // ( )

        if (!valid){ return intArrayOf() }

        decrypted += newVal
        keyIdx++
        if(keyIdx>2){
            keyIdx = 0
        }
        keyVal = key.get(keyIdx)
    }

    return decrypted    
}
