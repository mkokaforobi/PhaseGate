import java.util.Scanner;

import java.util.Arrays;

public class SwapArrayGrid {

    public static void arrayReverse (int[][] array) {
        for (int number = 0; number < array.length; number++) {
            int start = 0;
            int end = array [number].length;

            while (start < end) {
                int temporaryArray = array[number][start];
                array[number][start] = array[number][end];
                array[number][end] = temporaryArray;

                start++;
                end--;
            }
        }
    }

    public static void main(String... args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter number of rows: ");
        int rows = input.nextInt();

        System.out.print("Enter number of columns: ");
        int columns = input.nextInt();

        int[][] array = new int[rows][columns];

       
        for (int number = 0; number < rows; number++) {
            for (int count = 0; count < columns; count++) {
                System.out.print("Enter number: ");
                array[number][count] = input.nextInt();
            }
        }


        arrayReverse(array);

        
        System.out.println("Reversed array:");

        for (int number = 0; number < rows; number++) {
            System.out.println(Arrays.toString(array[number]));
        }

        
    }
}
