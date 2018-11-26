/**
 * Find sums utility.
 */

import org.apache.commons.lang3.Range;

import java.util.Map;
import java.util.HashMap;

/**
 * Find sums utility.
 */
public class FindSum {
    /**
     * Empty range.
     */
    public static Range EMPTY_RANGE = Range.between(0, -1);

    /**
     * Find first consecutive values in a list that total to a sum and return the range.
     *
     * @param data       integer array of data
     * @param sum        integer sum to find in data
     * @param allowempty allow empty range to be returned
     * @return Range in data that totals sum or null if not found, or Range(0, -1) for empty range.
     */
    public Range findSumRange(int[] data, int sum, boolean allowEmpty) {
        if (sum == 0 && allowEmpty) {
            return EMPTY_RANGE;
        }

        // store sums and positions
        Map<Integer, Integer> sumPositions = new HashMap<>();
        int currentSum = 0;
        sumPositions.put(currentSum, -1);

        for (int currentPos = 0; currentPos < data.length; currentPos++) {
            // calculate current sum and delta from sum
            // and lookup in previous sum positions
            currentSum += data[currentPos];
            int deltaSum = currentSum - sum;
            Integer deltaSumPos = sumPositions.get(deltaSum);
            if (deltaSumPos != null) {
                // return range after delta sum position
                return Range.between(deltaSumPos + 1, currentPos);
            }
            sumPositions.put(currentSum, currentPos);
        }

        return null;
    }

    /**
     * Find first consecutive values in a list that total to a sum and return the range.
     * Allow empty range to be returned.
     *
     * @param data integer array of data
     * @param sum  integer sum to find in data
     * @return Range in data that totals sum or null if not found, or Range(0, -1) for empty range.
     */
    public Range findSumRange(int[] data, int sum) {
        return findSumRange(data, sum, true);
    }
}
