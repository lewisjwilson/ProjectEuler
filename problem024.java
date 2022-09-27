// This will help... https://leetcode.com/media/original_images/31_Next_Permutation.gif

import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.*;


class problem024{

    public static String swap(String str, String one, String two){
        return Arrays.stream(str.split(one, -1))
            .map(s -> s.replaceAll(two, one))
            .collect(Collectors.joining(two));
    }

    public static void main(String[] args) {

        String digits = "012";
        int l = digits.length();

        ArrayList<String> perms = new ArrayList<>();

        String temp = "012";
        perms.add(temp);
        
        while(temp.equals("120") == false){
            String final_char = temp.substring(l-1, l);
            
            System.out.println("Final: " + final_char);
            
            String oldTemp = temp;
            System.out.println("OldTemp: " + oldTemp);


            int temp_idx = l-1;
            boolean broken = false;
            while(temp_idx >= 1){   
                String temp_char = temp.substring(temp_idx-1, temp_idx);
                temp = swap(temp, final_char, temp_char);
                System.out.println("Temp: " + temp);
                if(Integer.parseInt(temp) > Integer.parseInt(oldTemp)){
                    perms.add(temp);
                    System.out.println("Added " + temp);
                    broken = true;
                    break;
                } else {
                    temp_idx--;
                }
            }
          
        }

        System.out.println(String.join(", ", perms));        
    }
}
