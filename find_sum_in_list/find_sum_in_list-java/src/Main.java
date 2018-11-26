/**
 * Find sums utility main program.
 */

import org.apache.commons.lang3.Range;

import java.util.Arrays;

public class Main {

    /**
     * Main program to demo {@link FindSum#findSumRange(int[], int)} to standard out.
     *
     * @param args not used
     */
    public static void main(String[] args) {
        FindSum findSum = new FindSum();
        demo(findSum, new int[]{}, 0);
        demo(findSum, new int[]{1}, 5);
        demo(findSum, new int[]{5}, 5);
        demo(findSum, new int[]{1, 5}, 5);
        demo(findSum, new int[]{1, 2, 3}, 5);
        demo(findSum, new int[]{1, 2, 3, 5}, 5);
        demo(findSum, new int[]{1, 2, 4, 5}, 5);
    }

    /**
     * Demonstrate {@link FindSum#findSumRange(int[], int)} for specific values using standard out.
     *
     * @param findSum the {@link FindSum} object.
     * @param data    array of integer data
     * @param sum     sum to find in array of integer data
     */
    private static void demo(FindSum findSum, int[] data, int sum) {
        Range sumInListRange = findSum.findSumRange(data, sum);
        String dataStr = String.join(
                ", ",
                Arrays.stream(data)
                        .mapToObj(String::valueOf)
                        .toArray(String[]::new));

        String out = new StringBuilder("findSumRange([").append(dataStr).append("], ").append(sum).append(") = ").append(sumInListRange).toString();
        System.out.println(out);
    }

}
