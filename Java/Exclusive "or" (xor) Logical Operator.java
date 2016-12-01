Exclusive "or" (xor) Logical Operator

Overview

In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns true if exactly one of the two expressions are true, false otherwise. For example:

false xor false == false // since both are false
true xor false == true // exactly one of the two expressions are true
false xor true == true // exactly one of the two expressions are true
true xor true == false // Both are true.  "xor" only returns true if EXACTLY one of the two expressions evaluate to true.
Task

Since we cannot define keywords in Javascript (well, at least I don't know how to do it), your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated. Your xor function should have the behaviour described above, returning true if exactly one of the two expressions evaluate to true, false otherwise.
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
Solution:
public class XOR {
    
    public static boolean xor(boolean a, boolean b) {
        //your code here:
        return false;
    }
}
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
Example Tests:
import static org.junit.Assert.*;
import org.junit.Test;

public class XORTest {

    private static void testing(boolean actual, boolean expected) {
        assertEquals(expected, actual);
    }
    
    @Test
    public void testBasic() {
        System.out.println("Testing basics.");
        testing(XOR.xor(false, false), false);
        testing(XOR.xor(true, false), true);
        testing(XOR.xor(false, true), true);
        testing(XOR.xor(true, true), false);
    }
    @Test
    public void testNested() {
        System.out.println("Testing nested calls.");
        testing(XOR.xor(false, XOR.xor(false, false)), false);
        testing(XOR.xor(XOR.xor(true, false), false), true);
        testing(XOR.xor(XOR.xor(true, true), false), false);
        testing(XOR.xor(true, XOR.xor(true, true)), true);
        testing(XOR.xor(XOR.xor(false, false), XOR.xor(false, false)), false);
        testing(XOR.xor(XOR.xor(false, false), XOR.xor(false, true)), true);
        testing(XOR.xor(XOR.xor(true, false), XOR.xor(false, false)), true);
        testing(XOR.xor(XOR.xor(true, false), XOR.xor(true, false)), false);
        testing(XOR.xor(XOR.xor(true, true), XOR.xor(true, false)), true);
        testing(XOR.xor(XOR.xor(true, XOR.xor(true, true)), XOR.xor(XOR.xor(true, true), false)), true);
    }
}
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
return a!=b;
return a^=b;
return a^b;
