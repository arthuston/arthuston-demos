/**
  * Find sums utility.
  */

package com.arthuston.demos

import org.scalatest.FlatSpec

/**
  * Find sums utility.
  */
class FindSumSpec extends FlatSpec {

  "findSumRange" should "be empty" in {
    assert(FindSum.findSumRange(Array(), 5).isEmpty)
    assert(FindSum.findSumRange(Array(1), 5).isEmpty)
  }

  "findSumRange" should "be EmptyRange" in {
    assert(FindSum.findSumRange(Array(), 0) === Option(FindSum.EmptyRange))
  }

  "findSumRange" should "be Option(0 to 0)" in {
    assert(FindSum.findSumRange(Array(5), 5) === Option(0 to 0))
    assert(FindSum.findSumRange(Array(5, 5), 5) === Option(0 to 0))
  }

  "findSumRange" should "be Option(0 to x)" in {
    assert(FindSum.findSumRange(Array(2, 3), 5) === Option(0 to 1))
    assert(FindSum.findSumRange(Array(2, 3, 5), 5) === Option(0 to 1))
  }

  "findSumRange" should "be Option(x to x)" in {
    assert(FindSum.findSumRange(Array(1, 5), 5) === Option(1 to 1))
    assert(FindSum.findSumRange(Array(1, 5, 5), 5) === Option(1 to 1))
  }

  "findSumRange" should "be Option(x to y)" in {
    assert(FindSum.findSumRange(Array(1, 2, 3), 5) === Option(1 to 2))
    assert(FindSum.findSumRange(Array(1, 2, 3, 5), 5) === Option(1 to 2))
  }

}
