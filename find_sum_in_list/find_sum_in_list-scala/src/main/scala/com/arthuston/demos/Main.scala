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
    // isEmpty
    demo(Array(), 5)
    demo(Array(1), 5)
    
    // EmptyRange
    demo(Array(), 0)
    
    // Option(0 to 0)
    demo(Array(5), 5)
    demo(Array(5, 5), 5)
    
    // Option(0 to 1)
    demo(Array(2, 3), 5)
    demo(Array(2, 3, 5), 5)
    
    // Option(1 to 1)
    demo(Array(1, 5), 5)
    demo(Array(1, 5, 5), 5)
    
    // Option(1 to 2)
    demo(Array(1, 2, 3), 5)
    demo(Array(1, 2, 3, 5), 5)
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
