

-> Convert Integer to Binary and Octal


import scala.io.StdIn._
object Main {
  def main(args: Array[String]): Unit = {
    println("Enter an Integer Number: ")
    val input = scala.io.StdIn.readInt()

    val binary = convertToBinary(input)
    val octal = convertToOctal(input)

    println("Binary Representation : "+binary)
    println("Octal Representation : "+octal)
    
  }
  def convertToBinary(num : Int) : String = {
    Integer.toBinaryString(num)
  }
  def convertToOctal(num : Int) : String = {
    Integer.toOctalString(num)
  }
}
