Write a program to merge two sets and calculate product and average of all elements of the Set. (PPL)

object HelloWorld {
	def main(args: Array[String]): Unit = {
  val Num1 = Set(1,2,3,4)
  val Num2 = Set(5,6,7)
  var Num = Num1++Num2
  println(Num)
  
  val pro=Num.product 
  println(pro)
  
  val len=Num.size
  println(len)
	}
}
