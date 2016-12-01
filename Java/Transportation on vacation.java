After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).

Solution:
public class Kata {
  public int rentalCarCost(int d) {
    // Your solution here
  }
}
————————————————————————————————————————————————————————————————————————————————————————————————
Example Tests:
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class RentalCarExampleTests {
  @Test
  public void under3Tests() {
    assertEquals(40, Kata.rentalCarCost(1));
    assertEquals(80, Kata.rentalCarCost(2));
  }
  
  @Test
  public void under7Tests() {
    assertEquals(100, Kata.rentalCarCost(3));
    assertEquals(140, Kata.rentalCarCost(4));
    assertEquals(180, Kata.rentalCarCost(5));
    assertEquals(220, Kata.rentalCarCost(6));
  }
  
  @Test
  public void over7Tests() {
    assertEquals(230, Kata.rentalCarCost(7));
    assertEquals(270, Kata.rentalCarCost(8));
    assertEquals(310, Kata.rentalCarCost(9));
    assertEquals(350, Kata.rentalCarCost(10));
  }
}
————————————————————————————————————————————————————————————————————————————————————————————————

自己的答案
public class Kata {
  public static int rentalCarCost(int d) {
    // Your solution here
    if (d < 3) 
      return d*40 ;
    else if (d < 7)
      return 40*d-20;
    else  
      return 40*d-50;
    
  }
}

————————————————————————————————————————————————————————————————————————————————————————————————
  private static final int COST_PER_DAY = 40;
  
  public static int rentalCarCost(int d) {
    if (d < 3)       return d * COST_PER_DAY;
    else if (d >= 7) return d * COST_PER_DAY - 50;
    else             return d * COST_PER_DAY - 20;
  }
}
————————————————————————————————————————————————————————————————————————————————————————————————
public class Kata {
  private static final int COST_PER_DAY = 40;
  private static final int SMALL_DISCOUNT_DAY_BOUNDARY = 2;
  private static final int BIG_DISCOUNT_DAY_BOUNDARY = 6;
  private static final int SEVEN_DAYS_PLUS_DISCOUNT = 50;
  private static final int THREE_DAYS_PLUS_DISCOUNT = 20;

  public static int rentalCarCost(int d) {
    return carCostsPerDays(d) - discountForDays(d);
  }
  
  private static int carCostsPerDays(int days) {
    return days * COST_PER_DAY;
  }
  
  private static int discountForDays(int days) {
    int discount = 0;
    if (days > BIG_DISCOUNT_DAY_BOUNDARY)
      discount = SEVEN_DAYS_PLUS_DISCOUNT;
    else if (days > SMALL_DISCOUNT_DAY_BOUNDARY)
      discount = THREE_DAYS_PLUS_DISCOUNT;
    return discount;      
  }
}
————————————————————————————————————————————————————————————————————————————————————————————————



