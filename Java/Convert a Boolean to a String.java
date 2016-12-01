In this programming exercise, you're going to learn about functions, boolean (true/false) values, strings, and the if-statement.

A function is a block of code that takes an input and produces an output. In this example, boolean_to_string is a function whose input is either true or false, and whose output is the string representation of the input, either "true" or "false".

A common idea we often want to represent in code is the concept of true and false. A variable that can either be true or false is called a boolean variable. In this example, the input to boolean_to_string (represented by the variable b) is a boolean.

Lastly, when we want to take one action if a boolean is true, and another if it is false, we use an if-statement.

For this kata, don't worry about edge cases like where unexpected input is passed to the function. You'll get to worry about these enough in later exercises.

Solution:
public class BooleanToString {
  public static String convert(boolean b){
    if (true) {
      return "true";
    } else {
      return "false";
    }
  }

}

Example Tests:
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class BoolToStrTest{
  @Test public void testTrue(){
    assertEquals(BooleanToString.convert(true), "true");
  }
  
  @Test public void testFalse(){
    assertEquals(BooleanToString.convert(false), "false");
  }
}

——————————————————————————————————————————————————————————————————————————————————————
没看懂什么意思，拉倒吧。
public class BooleanToString {
  public static String convert(boolean b){
    return b ? "true" : "false";
  }
}

public class BooleanToString {
  public static String convert(boolean b){
    return Boolean.toString(b);
  }
}
原来是不用if
