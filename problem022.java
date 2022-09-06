// Question
// Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
// Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
// For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
// So, COLIN would obtain a score of 938 × 53 = 49714.
// What is the total of all the name scores in the file?


// Solution - Read in the file (one line) using a bufferedreader, sort, then process with nested for loop

import java.util.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Collections;

public class problem022
{
    public static String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    public static ArrayList<String> readData(){
        
        ArrayList<String> data = new ArrayList<>();
        
        try(BufferedReader br=new BufferedReader(new InputStreamReader(new FileInputStream("names.txt"),StandardCharsets.UTF_8))){
            String line = br.readLine();
    	      String[] split = line.split(",");
    	      for(int i = 0 ; i < split.length ; i++) {
    	        data.add(split[i].replaceAll("\"", ""));
    	      }
            return data;
        } catch (Exception e) {
            e.printStackTrace();
        }
        data.add("Invalid Data");
        return data;
    }
    
	public static void main(String[] args) {
	    ArrayList<String> names = readData();
	    Collections.sort(names);
	    
	    int totalScore = 0;
	    
	    for(int idx = 0 ; idx < names.size() ; idx++){
	        String name = names.get(idx);
	        int multiplier = idx+1;
	        int nameVal = 0;
	        for(int letter = 0 ; letter < name.length() ; letter++) {
	            char c = name.charAt(letter);
	            nameVal += ALPHABET.indexOf(c)+1;
	        }
	        totalScore+=(nameVal*multiplier);
	    }
	    
	    System.out.println(totalScore);
	}
}
