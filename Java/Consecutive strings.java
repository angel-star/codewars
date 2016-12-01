You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
——————————————————————————————————————————————————————————————————————————————————————————
Solution:
class LongestConsec {
    
    public static String longestConsec(String[] strarr, int k) {
        // your code
    }
}

——————————————————————————————————————————————————————————————————————————————————————————
Example Tests:
import static org.junit.Assert.*;
import org.junit.Test;

public class LongestConsecTest {

    private static void testing(String actual, String expected) {
        assertEquals(expected, actual);
    }
    @Test
    public void test() {
        System.out.println("longestConsec Fixed Tests");
        testing(LongestConsec.longestConsec(new String[] {"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"}, 2), "abigailtheta");
        testing(LongestConsec.longestConsec(new String[] {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"}, 1), "oocccffuucccjjjkkkjyyyeehh");
        testing(LongestConsec.longestConsec(new String[] {}, 3), "");
        testing(LongestConsec.longestConsec(new String[] {"itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"}, 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck");
        testing(LongestConsec.longestConsec(new String[] {"wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"}, 2), "wlwsasphmxxowiaxujylentrklctozmymu");
        testing(LongestConsec.longestConsec(new String[] {"zone", "abigail", "theta", "form", "libe", "zas"}, -2), "");
        testing(LongestConsec.longestConsec(new String[] {"it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"}, 3), "ixoyx3452zzzzzzzzzzzz");
        testing(LongestConsec.longestConsec(new String[] {"it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"}, 15), "");
        testing(LongestConsec.longestConsec(new String[] {"it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"}, 0), "");
    }
}
——————————————————————————————————————————————————————————————————————————————————————————

自己写的。


    public static void main(String[] args) {
    	String[] strarr = {"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"};
    	int k = 2;
    	String [] number = new String[strarr.length];
    	
    	
        if (strarr.length < k || strarr.length == 0){
        	System.out.println(1);
        }
        else {
        	for (int i = 0;i<strarr.length;i++){
        		number[i] = strarr[i];
        		
        	}
        	
        	
        	//去重
        	
        	for(int x = 0;x<number.length;x++){
        		for(int y=0; y <number.length-1;y++){
        			if (number[y].length()< number[y+1].length()){
        				String z = number[y];
        				number[y] = number[y+1];
        				number[y+1] = z;
        			}
        		}
        	}

        	for (String x : number){
        		System.out.println(x);
        	}
        	System.out.println(2);
        }
	}
  
这个可以按照字符串数组中 单个元素的长度降序排列，这里没有完善的问题就是 1 去重 2 最后的组合（这个简单 ）   3.优化排序算法，现在的这个太傻了
那么看看标准答案吧
————————————————————————————————————————————————————————————————————————————————————
class LongestConsec {
    public static String longestConsec(String[] strarr, int k) {
        if (strarr.length == 0 || k > strarr.length || k <= 0)
            return "";

        String longestStr = "";
        for (int index = 0; index < strarr.length - k + 1; index++) {
            StringBuilder sb = new StringBuilder();
            for (int i = index; i < index + k; i++) {
                sb.append(strarr[i]);
            }
            if (sb.toString().length() > longestStr.length()) {
                longestStr = sb.toString();
            }
        }
        return longestStr;
    }
}

————————————————————————————————————————————————————————————————————————————————————

class LongestConsec {
    
    public static String longestConsec(String[] strarr, int k) {
        if (strarr.length == 0 || k > strarr.length || k <= 0) {
            return "";
        }
        StringBuilder maxWord = new StringBuilder();
        for (int i = 0; i <= strarr.length - k; i++) {
            StringBuilder currentWord = new StringBuilder();
            for (int j = i; j < i + k; j++) {
                currentWord.append(strarr[j]);
            }
            if (maxWord.length() < currentWord.length()) {
                maxWord = currentWord;
            }
        }

        return maxWord.toString();
    }
}
————————————————————————————————————————————————————————————————————————————————————

import java.util.stream.IntStream;
import java.util.stream.Collectors;

public class LongestConsec {

  public static String longestConsec(String[] strArr, int k) {
    return (k > 0 && strArr.length > 0 && k <= strArr.length) ?
      IntStream.rangeClosed(0, strArr.length - k)
        .mapToObj(i -> IntStream.range(0, k).mapToObj(j -> strArr[i + j]).collect(Collectors.joining()))
        .sorted((s1, s2) -> Integer.compare(s2.length(), s1.length()))
        .findFirst().get()
      : "";
  }
}
————————————————————————————————————————————————————————————————————————————————————

class LongestConsec {
    
    public static String longestConsec(String[] strarr, int k) {
        // your code
        
        int maxSum = 0;
        int start = 0;
        int end = 0;
        String text = "";
        
        if(!(strarr.length == 0 || k >strarr.length || k<= 0 ) )
        {
        
        for(int i = 0; i<=strarr.length-k; i++){
            int sum = 0;
          
            for(int j = i; j< i+k; j++){
            
              sum += strarr[j].length();
            }
            
            if(sum > maxSum)
            {
              maxSum = sum;
              start = i;
              end = i+k;
            }
            
        }
        
        
        for(int c = start; c<end; c++){
            text += strarr[c];
        }
     }
        
        return text;
    }
}
————————————————————————————————————————————————————————————————————————————————————
class LongestConsec {
    public static String longestConsec(String[] strarr, int k) {
        String longest = "";
        for (int i = 0; i <= strarr.length - k; i++) {
            StringBuilder candidate = new StringBuilder();
            for (int j = 0; j < k; j++) {
                candidate.append(strarr[i + j]);
            }
            if (candidate.length() > longest.length()) {
                longest = candidate.toString();
            }
        }
        return longest;
    }
}

