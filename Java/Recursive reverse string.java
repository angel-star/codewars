Do you know how to write a recursive function? Let's test it!

Definition: Recursive function is a function that calls itself during its execution

Classic factorial counting on Javascript
function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n-1) 
}
Your objective is to complete a recursive function reverse() that receives str as String and returns the same string in reverse order

Rules:

reverse function should be executed only N times. N = length of the input string
helper functions are not allowed
changing the signature of the function is not allowed
Examples:

reverse("hello world") = "dlrow olleh" (N = 11)
reverse("abcd") = "dcba" (N = 4)
reverse("12345") = "54321" (N = 5)
All tests for this Kata are randomly generated, besides checking the reverse logic they will count how many times the reverse() function has been executed. 

Please note that js and coffeescript tests show a wrong message. Expected and Actual message should be swapped. It can be changed only by moderator.



Solution:
public class Reverse {

    public String reverse(String str) {
       // your code here
    }
}

——————————————————————————————————————————————————————————————————————————————————————————
Test Driven Development (TDD)
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

// TODO: Replace examples and use TDD development by writing your own tests

public class SolutionTest {
    @Test
    public void testSomething() {
        // assertEquals("expected", "actual");
    }
}

——————————————————————————————————————————————————————————————————————————————————————————

/*
自己没做出来 
看看答案吧  
体会一下递归的思想
*/
ublic class Reverse 
{
    
    public String reverse(String str) 
    {
       if (str == null || str.length() <= 1)
       {
         return str;
       }
       
       return reverse(str.substring(1)) + str.charAt(0);
    }
}
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
public class Reverse {

    public String reverse(String str) {
        if (str.length() == 1)
            return str;
        return str.charAt(str.length()-1) + reverse(str.substring(0, str.length()-1));
    }
}
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
public class Reverse {
    public String reverse(String str) {
       return (str.length() > 1 ? reverse(str.substring(1)) : "") + str.charAt(0);
    }
}
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
public class Reverse {

    public String reverse(String str) {
       int len = str.length();
       if(len == 1) return str;
       return str.charAt(len - 1) + reverse(str.substring(0, len-1));
    }
}
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
public class Reverse {

    public String reverse(String str) {
        int len = str.length();
        /* This one was O(N) */
        return (len == 1) ? str : str.substring(len - 1) + reverse(str.substring(0, len - 1));
        /* This one was O(logN) */
        // return (len == 1) ? str : reverse(str.substring(len / 2)) + reverse(str.substring(0, len / 2));
    }
}

