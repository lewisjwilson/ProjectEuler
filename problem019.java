
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class problem019 {

    public static String start = "1901-01-01";
    public static String end = "2000-12-31";

    public static void main(String[] args) {
        LocalDate startDate = LocalDate.parse(start);
        LocalDate endDate = LocalDate.parse(end);

        System.out.println("Start Date : " + startDate);
        System.out.println("This date was a: " + startDate.getDayOfWeek());
        System.out.println("End Date : " + endDate);
        System.out.println("This date was a: " + endDate.getDayOfWeek());

        // If not a leap year, the following year, same date is the next weekday
        // Leap year pushes the days forward by one

        // 31 days in January. In year 1901 (not a leap year), staring on a tuesday
        // If 1st, 2nd, 3rd, 4th are a Sunday, there are 5 Sundays in the Month, else 4

        int janSundays = 0;
        // For each year between the start and end dates
        for (int y = startDate.getYear(); y <= endDate.getYear(); y++) {
            System.out.println(y);
            LocalDate first = LocalDate.parse(String.valueOf(y) + "-01-01");
            LocalDate second = LocalDate.parse(String.valueOf(y) + "-01-02");
            LocalDate third = LocalDate.parse(String.valueOf(y) + "-01-03");
            LocalDate fourth = LocalDate.parse(String.valueOf(y) + "-01-04");
            System.out.println(first.getDayOfWeek() + " " + second.getDayOfWeek() + " " + third.getDayOfWeek() + " "
                    + fourth.getDayOfWeek());
            boolean sundayFound = false;
            if (first.getDayOfWeek() == DayOfWeek.SUNDAY ||
                    second.getDayOfWeek() == DayOfWeek.SUNDAY ||
                    third.getDayOfWeek() == DayOfWeek.SUNDAY ||
                    fourth.getDayOfWeek() == DayOfWeek.SUNDAY) {
                sundayFound = true;
            }

            if (sundayFound) {
                janSundays += 5;
            } else {
                janSundays += 4;
            }

            System.out.println("January Sundays: " + janSundays);
        }

    }
}