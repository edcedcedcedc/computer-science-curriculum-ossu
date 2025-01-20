/* Date.java */

import java.security.InvalidParameterException;

class Date {

  /* Put your private data fields here. */
  private int year;
  private int month;
  private int day;

  /**
   * Constructs a date with the given month, day and year. If the date is
   * not valid, the entire program will halt with an error message.
   * 
   * @param month is a month, numbered in the range 1...12.
   * @param day   is between 1 and the number of days in the given month.
   * @param year  is the year in question, with no digits omitted.
   */

  public Date(int month, int day, int year) {
    if (Date.isValidDate(month, day, year)) {
      this.month = month;
      this.day = day;
      this.year = year;
    } else {
      System.out.print(false);
      /* System.exit(0); */
    }
  }

  /**
   * Constructs a Date object corresponding to the given string.
   * 
   * @param s should be a string of the form "month/day/year" where month must
   *          be one or two digits, day must be one or two digits, and year must
   *          be
   *          between 1 and 4 digits. If s does not match these requirements or is
   *          not
   *          a valid date, the program halts with an error message.
   */
  public Date(String s) {
    this(Integer.parseInt(s.split("/")[0]),
        Integer.parseInt(s.split("/")[1]),
        Integer.parseInt(s.split("/")[2]));
  }

  /**
   * Checks whether the given year is a leap year.
   * 
   * @return true if and only if the input year is a leap year.
   */
  public static boolean isLeapYear(int year) {
    return (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
  }

  /**
   * Returns the number of days in a given month.
   * 
   * @param month is a month, numbered in the range 1...12.
   * @param year  is the year in question, with no digits omitted.
   * @return the number of days in the given month.
   */
  public static int daysInMonth(int month, int year) throws InvalidParameterException {
    if (year < 1) {
      throw new InvalidParameterException("Invalid Year: Year prior to A.D. 1");
    }

    switch (month) {
      case 1, 3, 5, 7, 8, 10, 12 -> {
        return 31;
      }
      case 4, 6, 9, 11 -> {
        return 30;
      }
      case 2 -> {
        if (Date.isLeapYear(year)) {
          return 29;
        } else {
          return 28;
        }
      }
      default -> throw new InvalidParameterException("Invalid Month: Must be between 1 and 12");
    }
  }

  /**
   * Checks whether the given date is valid.
   * 
   * @return true if and only if month/day/year constitute a valid date.
   *
   *         Years prior to A.D. 1 are NOT valid.
   */
  public static boolean isValidDate(int month, int day, int year) throws InvalidParameterException {
    if (month < 1 || month > 12 || day < 1 || day > 31) {
      return false;
    }

    int maxDay = Date.daysInMonth(month, year);

    return day <= maxDay;

  }

  /**
   * Returns a string representation of this date in the form month/day/year.
   * The month, day, and year are expressed in full as integers; for example,
   * 12/7/2006 or 3/21/407.
   * 
   * @return a String representation of this date.
   */
  @Override
  public String toString() {
    return month + "/" + day + "/" + year; // replace this line with your solution
  }

  /**
   * Determines whether this Date is before the Date d.
   * 
   * @return true if and only if this Date is before d.
   */
  public boolean isBefore(Date d) {
    if (this.year < d.year) {
      return true;
    } else if (this.year == d.year && this.month < d.month) {
      return true;
    } else
      return this.month == d.month && this.day < d.day;
  }

  /**
   * Determines whether this Date is after the Date d.
   * 
   * @return true if and only if this Date is after d.
   */
  public boolean isAfter(Date d) {
    if (this.year > d.year) {
      return true;
    } else if (this.year == d.year && this.month > d.month) {
      return true;
    } else
      return this.month == d.month && this.day > d.day;
  }

  /**
   * Returns the number of this Date in the year. // I switched it to static
   * method
   * 
   * @return a number n in the range 1...366, inclusive, such that this Date
   *         is the nth day of its year. (366 is used only for December 31 in a
   *         leap
   *         year.)
   */
  public static int dayInYear(int year) {
    if (Date.isLeapYear(year)) {
      return 366;
    } else {
      return 365;
    }
  }

  /**
   * Determines the difference in days between d and this Date. For example,
   * if this Date is 12/15/2012 and d is 12/14/2012, the difference is 1.
   * If this Date occurs before d, the result is negative.
   * 
   * @return the difference in days between d and this date, i.e date2 - date1.
   */
  public int difference(Date d) {
    int date2 = Date.elapsedTime(this);
    int date1 = Date.elapsedTime(d);
    return date2 - date1;
  }

  public static int elapsedTime(Date d) {
    int elapsedTime = 0;

    for (int i = 1; i < d.year; i++) {
      elapsedTime += Date.dayInYear(i);
    }

    for (int i = 1; i < d.month; i++) {
      elapsedTime += Date.daysInMonth(i, d.year);
    }

    elapsedTime += d.day;
    return elapsedTime;

  }

  public static void main(String[] argv) {
    try {
      System.out.println("\nTesting constructors.");
      Date d1 = new Date(1, 1, 1);
      System.out.println("Date should be 1/1/1: " + d1);
      d1 = new Date("2/4/2");
      System.out.println("Date should be 2/4/2: " + d1);
      d1 = new Date("2/29/2000");
      System.out.println("Date should be 2/29/2000: " + d1);
      d1 = new Date("2/29/1904");
      System.out.println("Date should be 2/29/1904: " + d1);

      d1 = new Date(12, 31, 1);
      System.out.println("Date should be 12/31/1975: " + d1);
      Date d2 = new Date("1/1/2");
      System.out.println("Date should be 1/1/1976: " + d2);
      Date d3 = new Date("1/2/1976");
      System.out.println("Date should be 1/2/1976: " + d3);

      Date d4 = new Date("2/27/1977");
      Date d5 = new Date("8/31/2110");
      Date d6 = new Date("8/29/2000");
      Date d7 = new Date("7/25/2024");
      Date d8 = new Date("6/19/2025");

      /* I recommend you write code to test the isLeapYear function! */
      System.out.println("\nTesting Leap Year.");
      System.out.println(d6.year + " Should be true: " + Date.isLeapYear(d6.year));
      System.out.println(d7.year + " Should be true: " + Date.isLeapYear(d7.year));
      System.out.println(d8.year + " Should be false: " + Date.isLeapYear(d8.year));

      System.out.println("\nTesting before and after.");
      System.out.println(d2 + " after " + d1 + " should be true: " +
          d2.isAfter(d1));
      System.out.println(d3 + " after " + d2 + " should be true: " +
          d3.isAfter(d2));
      System.out.println(d1 + " after " + d1 + " should be false: " +
          d1.isAfter(d1));
      System.out.println(d1 + " after " + d2 + " should be false: " +
          d1.isAfter(d2));
      System.out.println(d2 + " after " + d3 + " should be false: " +
          d2.isAfter(d3));

      System.out.println(d1 + " before " + d2 + " should be true: " +
          d1.isBefore(d2));
      System.out.println(d2 + " before " + d3 + " should be true: " +
          d2.isBefore(d3));
      System.out.println(d1 + " before " + d1 + " should be false: " +
          d1.isBefore(d1));
      System.out.println(d2 + " before " + d1 + " should be false: " +
          d2.isBefore(d1));
      System.out.println(d3 + " before " + d2 + " should be false: " +
          d3.isBefore(d2));

      System.out.println("\nTesting Elapsed time since 1/1/1.");
      System.out.println("1/1/1" + " + " + d1 + " should be 365: " + Date.elapsedTime(d1));
      System.out.println("1/1/1" + " + " + d2 + " should be 365 + 1: " + Date.elapsedTime(d2));

      System.out.println("\nTesting difference.");
      System.out.println(d1 + " - " + d1 + " should be 0: " + d1.difference(d1));
      System.out.println(d2 + " - " + d1 + " should be 1: " + d2.difference(d1));
      System.out.println(d5 + " - " + d4 + " should be 48762: " + d5.difference(d4));
      System.out.println(d3 + " - " + d4 + " should be -422: " + d3.difference(d4));

    } catch (InvalidParameterException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }
}
