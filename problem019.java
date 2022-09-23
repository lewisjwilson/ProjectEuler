// Question
// You are given the following information, but you may prefer to do some research for yourself.
// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


// Solution

import java.time.DayOfWeek;
import java.time.LocalDate;

public class problem019 {

    public static String start = "1901-01-01";
    public static String end = "2000-12-31";

    public static void main(String[] args) {
        LocalDate startDate = LocalDate.parse(start);
        LocalDate endDate = LocalDate.parse(end);

        String[] months = {"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"};

        int sundays = 0;
        // For each year between the start and end dates
        for (int y = startDate.getYear(); y <= endDate.getYear(); y++) {
            //System.out.println(y);
            for(int m = 0 ; m < 12 ; m++){
                LocalDate first = LocalDate.parse(String.valueOf(y) + "-" + months[m] + "-01");
                if (first.getDayOfWeek() == DayOfWeek.SUNDAY){
                    sundays++;
                }
                
            }
            
        }
        System.out.println("Sundays: " + sundays);
    }
}
