When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

Try using "Switch" statements.

This kata is meant for beginners. Rank and upvote to bring it out of beta
————————————————————————————————————————————————————————————————————————————————————————
Solution:
public class Kata
{
  public static String switchItUp(int number)
  {
    return "";
  }
}

————————————————————————————————————————————————————————————————————————————————————————
Example Tests:
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void basicTests() {
        assertEquals("One", Kata.switchItUp(1));
        assertEquals("Three", Kata.switchItUp(3));
        assertEquals("Five", Kata.switchItUp(5));
    }
}
————————————————————————————————————————————————————————————————————————————————————————
自己的答案 这个太简单了 只是想锻炼一下switch语句的用法 

public class Kata
{
  public static String switchItUp(int number)
  {
  
    //System.out.println(number);
    switch (number){
      case 1:
  			return "One";
  		case 2:
  			return "Two";		
  		case 3:
  			return "Three";
  		case 4:
  			return "Four";
  		case 5:
  			return "Five";
  		case 6:
  			return "Six";
  		case 7:
  			return "Seven";
  		case 8:
  			return "Eight";
  		case 9:
  			return "Nine";
  		case 0:
  			return "Zero";
  		case 10:
  			return "Ten";
      default:
        return "";
  }
}}
/*————————————————————————————————————————————————————————————————————————————————————————————————————————————*/
//答案
import java.util.HashMap;

public class Kata
{
    private static final HashMap<Integer, String> digits;
    static
    {
        digits = new HashMap<>();
        digits.put(0, "Zero");
        digits.put(1, "One");
        digits.put(2, "Two");
        digits.put(3, "Three");
        digits.put(4, "Four");
        digits.put(5, "Five");
        digits.put(6, "Six");
        digits.put(7, "Seven");
        digits.put(8, "Eight");
        digits.put(9, "Nine");
    }

    public static String switchItUp(int number)
    {
        return digits.get(number);
    }
}


/*————————————————————————————————————————————————————————————————————————————————————————————————————————————*/
//答案
public class Kata
{
  public static String switchItUp(int number)
  {
     String[] words = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
     String word = words[number];
     return word;
  }
}


/*————————————————————————————————————————————————————————————————————————————————————————————————————————————*/
//答案

public class Kata{
  public static String switchItUp(int number){
    String[] names = {"Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"};
    return names[number];
  }
}
