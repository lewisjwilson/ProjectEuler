import java.util.*;

class Pentagon {
    
    public static int pentagonal(int n){
        return (int)(n*(3*n-1))/2;
    }
    
    public static void main(String[] args) {
        
        List<Integer> pentagonals = new ArrayList<Integer>();
        
        for(int n = 1 ; n<=3000 ; n++){
            pentagonals.add(pentagonal(n));
        }
        //System.out.println("Pentagonals: " + pentagonals.toString());
        
        boolean flag = false;
        
        for(Integer pj : pentagonals){
            for(Integer pk : pentagonals){
                if(pj != pk){
                    int pSum = pj + pk;
                    int pDiff = pk - pj;
                    if(pentagonals.contains(pSum) && pentagonals.contains(pDiff)){
                        flag = true;
                        System.out.print(pj + " is the " + pentagonals.indexOf(pj) + "th pentagonal number" + "\n");
                        System.out.print(pk + " is the " + pentagonals.indexOf(pk) + "th pentagonal number" + "\n");
                        System.out.print(pk + " + " + pj + " = " + pSum + ", the " + pentagonals.indexOf(pSum) + "th pentagonal number, and\n");
                        System.out.print(pk + " - " + pj + " = " + pDiff + ", the " + pentagonals.indexOf(pDiff) + "th pentagonal number."); 
                        break;
                    }
                }
            }
            if(flag){break;}
        }
        
    }
}
