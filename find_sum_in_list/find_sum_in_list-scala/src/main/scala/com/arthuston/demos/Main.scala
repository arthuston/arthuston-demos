/**
  * Find sums utility main program.
  */

package com.arthuston.demos

import com.arthuston.demos.FindSum.findSumRange

object Main extends App {

  /**
    * Main program to demo  to standard out.
    *
    * @param args not used
    */
  override def main(args: Array[String]): Unit = {
    demo(Array(), 0)
    demo(Array(1), 5)
    demo(Array(5), 5)
    demo(Array(1, 5), 5)
    demo(Array(1, 2, 3), 5)
    demo(Array(1, 2, 3, 5), 5)
    demo(Array(1, 2, 4, 5), 5)
  }

  /**
    * Demonstrate  for specific values using standard out.
    *
    * @param data array of integer data
    * @param sum  sum to find in array of integer data
    */
  def demo(data: Array[Int], sum: Int): Unit = {
    val sumRange = findSumRange(data, sum)
    val sumRangeStr: String = sumRange.toString
    println(new StringBuilder("findSumRange([")
      .append(data.mkString(","))
      .append("], ")
      .append(sum)
      .append(") = ")
      .append(sumRangeStr)
    )
  }

}
