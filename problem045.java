import java.math.*;

class Problem045 {
    
    // T = n(n+1)/2 --> solving for n. If n is an integer, is Triangle
    public static boolean isTri(long x){
        double T = (Math.sqrt(1+(8*x))-1)/2;
        if (T == (int)T){
            return true;
        }
        return false;
    }
    
    // P = n(3n-1)/2 --> solving for n. If n is an integer, is Pentagon
    public static boolean isPent(long x){
        double P = (Math.sqrt(1+(24*x))+1)/6;
        if (P == (int)P){
            return true;
        }
        return false;
    }
    
    // H = n(2n-1) --> solving for n. If n is an integer, is Hexagonal
    public static boolean isHex(long x){
        double H = (Math.sqrt(1+(8*x))+1)/4;
        if (H == (int)H){
            return true;
        }
        return false;
    }
        
    public static void main(String[] args) {
        long n = 1;
        while(true){
            if(isTri(n) && isPent(n) && isHex(n)){
                System.out.print(n + " is Triangular, Pentagonal and Hexagonal!\n");
                if(n>40755){
                    break;
                }
            }
            n++;
        }
        
        System.out.println("Finished.");
        
    }
}
