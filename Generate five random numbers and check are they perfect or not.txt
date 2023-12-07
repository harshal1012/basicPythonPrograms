Generate five random numbers and check are they perfect or not

import scala.util.Random
object Main {
  def main(args: Array[String]): Unit = {
    val random = new Random()

    for(i <- 1 to 5){
      val number = random.nextInt(200)+1
    
    if(isPerfectNumber(number)) {
      println(number+" is a Perfect Number")
    }
    else {
      println(number+" is not a Perfect Number")
    }
    println()
  }
  }

  def isPerfectNumber(num:Int):Boolean = {
   if(num <=1){
     return false
   }
   
  var sum : Int = 1
   for(i <- 2 until num){
     if(num % i == 0){
       sum += i
     }
   }
   return sum == num
 }
}
