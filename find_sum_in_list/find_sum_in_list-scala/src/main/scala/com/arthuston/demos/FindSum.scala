/**
  * Find sums utility.
  */

package com.arthuston.demos

import scala.collection.mutable

/**
  * Find sums utility.
  */
object FindSum {
  /**
    * Empty range.
    */
  val EmptyRange = 0 to -1

  /**
    * Find first consecutive values in a list that total to a sum and return the range.
    * Allow empty range to be returned.
    *
    * @param data integer array of data
    * @param sum  integer sum to find in data
    * @return Range in data that totals sum or null if not found, or Range(0, -1) for empty range.
    */
  def findSumRange(data: Array[Int], sum: Int): Option[Range.Inclusive] = {
    if (sum == 0) {
      return Option(EmptyRange)
    }
    // store sums and positions
    val sumPositions = new mutable.HashMap[Int, Int]
    var currentSum = 0
    sumPositions(currentSum) = -1

    for (currentPos <- data.indices) {
      currentSum += data(currentPos)
      val previousSum = currentSum - sum

      val previousSumPos = sumPositions.get(previousSum)
      if (previousSumPos.isDefined) {
        return Option(previousSumPos.get + 1 to currentPos)
      }
      sumPositions(currentSum) = currentPos
    }

    None
  }
}
