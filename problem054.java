import java.math.*;
import java.util.*;

class Problem054 {
    
    public static Hashtable<String, Integer> numbers = new Hashtable<String, Integer>();
    
    public static Hashtable<String, Integer> winTypes = new Hashtable<String, Integer>();
    
    public static void populateNumbers(){
        numbers.put("2", 2);
        numbers.put("3", 3);
        numbers.put("4", 4);
        numbers.put("5", 5);
        numbers.put("6", 6);
        numbers.put("7", 7);
        numbers.put("8", 8);
        numbers.put("9", 9);
        numbers.put("T", 10);
        numbers.put("J", 11);
        numbers.put("Q", 12);
        numbers.put("K", 13);
        numbers.put("A", 14);
    }
    
    public static void populateWinTypes(){
        // Win Type, Score
        winTypes.put("High Card", 1);
        winTypes.put("One Pair", 2);
        winTypes.put("Two Pairs", 3);
        winTypes.put("Three of a Kind", 4);
        winTypes.put("Straight", 5);
        winTypes.put("Flush", 6);
        winTypes.put("Full House", 7);
        winTypes.put("Four of a Kind", 8);
        winTypes.put("Straight Flush", 9);
        winTypes.put("Royal Flush", 10);
    }
    
    public static boolean areConsecutive(List<String> al){
        List<Integer> iaL = new ArrayList<Integer>();
        for(String s : al){
            iaL.add(numbers.get(s));
        }
        
        Collections.sort(iaL);
        
        boolean flag = true;
        for(int x = 1; x<iaL.size(); x++){
            if(iaL.get(x) != iaL.get(x-1) + 1){
                flag = false;
                break;
            }
        }
        return flag;
    }
    
    public static String calculateWinType(List<String> cards){
        
        List<String> v = new ArrayList<String>();
        Set<String> s = new HashSet<String>();
        
        List<String> topFive = new ArrayList<String>();
        topFive.add("T");
        topFive.add("J");
        topFive.add("Q");
        topFive.add("K");
        topFive.add("A");
        
        for(String c : cards){
            v.add(c.substring(0, 1));
            s.add(c.substring(1));
        }
        
        int card1 = Collections.frequency(v, v.get(0));
        int card2 = Collections.frequency(v, v.get(1));
        int card3 = Collections.frequency(v, v.get(2));
        int card4 = Collections.frequency(v, v.get(3));
        int card5 = Collections.frequency(v, v.get(4));
        
        System.out.println(v);
        System.out.println(s);
        
        if( s.size() == 1 && v.containsAll(topFive) ){
            return "Royal Flush";
        } else if( s.size() == 1 && areConsecutive(v) ){
            return "Straight Flush";
        } else if( card1 == 4 || card2 == 4 ){
            return "Four of a Kind";
        } else if( (card1 == 3 || card2 == 3 || card3 == 3) && (card1 == 2 || card2 == 2 || card3 == 2 || card4 == 2) ){
            return "Full House";
        } else if( s.size() == 1 ){
            return "Flush";
        } else if ( areConsecutive(v) ){
            return "Straight";
        } else if(card1 == 3 || card2 == 3 || card3 == 3){
            return "Three of a Kind";
        } else if(card1*card2*card3*card4*card5 == 16){
            return "Two Pairs";
        } else if(card1 == 2 || card2 == 2 || card3 == 2 || card4 == 2){
            return "One Pair";
        } else {
            return "High Card";
        }
    }
    
    public static void main(String[] args) {
        
        populateNumbers();
        populateWinTypes();
        
        String cards[] = "8C TS KC 9H 4S 7D 2S 5D 3S AC".split(" ");
        //String cards[] = "3H TH 6S 4H 7D 7D 2S 5D 3S AC".split(" ");
        List<String> cardsP1 = Arrays.asList(cards).subList(0, 5);
        List<String> cardsP2 = Arrays.asList(cards).subList(5, 10);
        
        String p1Result = calculateWinType(cardsP1);
        String p2Result = calculateWinType(cardsP2);
        
        int p1Score = winTypes.get(p1Result);
        int p2Score = winTypes.get(p2Result);
        
        if(p1Score == p2Score){
            // calculute scores on card values
        }
        
        System.out.println("P1: " + p1Score);
        System.out.println("P2: " + p2Score);
        
    }
}
