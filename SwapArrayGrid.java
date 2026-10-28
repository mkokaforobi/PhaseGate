import java.util.Scanner;

import java.util.Arrays;

public class SwapArrayGrid {

    public static int[][] arrayReverse (int[][] array) {
        for (int number = 0; number < array.length; number++) {
	
	    int start = 0;
            int end = array [number].length -1;

            while (start < end) {
                int temporaryArray = array[number][start];
                array[number][start] = array[number][end];
                array[number][end] = temporaryArray;

                start++;
                end--;
            }
        }
	return array;
    }

    public static void main(String... args) {
       
	int[][] array = {{1,2,3}, {4,5,6}, {7,8,9}};
       
        
        int[][] revesedArray = arrayReverse(array);

        
        System.out.println(Arrays.deepToString(revesedArray));        
    }
}
