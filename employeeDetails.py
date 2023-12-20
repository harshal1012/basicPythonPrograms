Define a class employee. Define methods accept() and display() and diplay details of employee having maximum salary.

class Employee(val id:Int, val name:String, val salary:Double){
  def display():Unit = {
    println("Employee id is: "+id)
    println("Employee Name is: "+name)
    println("Employee Salary is: "+salary)
  }
}
object Main{
  def acceptDetails():Employee = {
    print("Enter Employee id: ")
    var id = scala.io.StdIn.readInt()
    println()
    print("Enter Employee Name: ")
    var name = scala.io.StdIn.readLine()
    println()
    print("Enter Employee Salary: ")
    var salary = scala.io.StdIn.readDouble()

    new Employee(id, name, salary)
  }
  def main(args: Array[String]):Unit ={
    var employees: List[Employee] = List()

    print("Enter the no. of employee to be enter: ")
    var n = scala.io.StdIn.readInt()

    for(i <- 0 until n ){
      println(s"Enter details for emploee $i: ")
      var employee = acceptDetails()
      employees = employee :: employees
    }
    
    val maxSalary = employees.maxBy(_.salary)
    println("Details of Maximum salary of Employee: ")
    maxSalary.display()
  }
  
}

