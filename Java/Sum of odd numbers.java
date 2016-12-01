Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

rowSumOddNumbers(1); // 1
rowSumOddNumbers(2); // 3 + 5 = 8
——————————————————————————————————————————————————————————————————————————————————————
Solution:
class RowSumOddNumbers {
    public static int rowSumOddNumbers(int n) {
        //TODO
    }
}
——————————————————————————————————————————————————————————————————————————————————————
Example Tests:
import static org.junit.Assert.*;
import org.junit.Test;

public class RowSumOddNumbersTest {

    @Test
    public void test1() {
        assertEquals(1, RowSumOddNumbers.rowSumOddNumbers(1));
        assertEquals(74088, RowSumOddNumbers.rowSumOddNumbers(42));
    }
}
——————————————————————————————————————————————————————————————————————————————————————

自己的答案 找到的规律 不知道正常应该怎么做；

class RowSumOddNumbers {
    public static int rowSumOddNumbers(int n) {
        //TODO
        System.out.println(n);

        return n*n*n;
    }
}
——————————————————————————————————————————————————————————————————————————————————————

——————————————————————————————————————————————————————————————————————————————————————

——————————————————————————————————————————————————————————————————————————————————————
