import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
 
public class DayOccurTime {
 
    public static void dayOccurTime(int year) {
 
        // stores days in a week
        String[] days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
 
        // Initialize all counts as 52
        int[] L = new int[7];
        for (int i = 0; i < 7; i++) {
            L[i] = 52;
        }
 
        // Find the index of the first day of the year
        LocalDate date = LocalDate.of(year, 1, 1);
        String day = date.format(DateTimeFormatter.ofPattern("EEEE"));
        int pos = -1;
        for (int i = 0; i < 7; i++) {
            if (day.equals(days[i])) {
                pos = i;
            }
        }
 
        // mark the occurrence to be 53 of 1st day and 2nd day if the year is leap year
        if (date.isLeapYear()) {
            L[pos] += 1;
            L[(pos + 1) % 7] += 1;
        } else {
            L[pos] += 1;
        }
 
        // Print the days
        for (int i = 0; i < 7; i++) {
            System.out.println(days[i] + " " + L[i]);
        }
    }
 
    public static void main(String[] args) {
        int year = 2019;
        dayOccurTime(year);
    }
}
