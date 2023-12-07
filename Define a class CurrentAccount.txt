1-> Define a class CurrentAccount. Define constructors and operations withdraw(), deposit(), viewBalance(). Create an object and perform operations 

class Current_Acount(acc_no:Int, name:String, var balance:Float) {
  var min_bal:Float = 5000
  def withdraw(amt:Float) = {
    if(balance - amt < min_bal){
      println("can't be withdrawn")
    }
    else {
      balance = balance - amt
    }
  }

  def deposit(amt : Float) = {
    balance += amt
  }

  def viewBalance() = {
    println("Total Balance is: "+balance)
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    var A = new Current_Acount(123, "Pritee", 40000)
    A.viewBalance()
    A.withdraw(10000)
    A.viewBalance()
    A.deposit(20000)
    A.viewBalance()
  }
}
