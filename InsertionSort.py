-> Insertion Sort
object Main {
  def main(args: Array[String]): Unit = {
    var arr :Array[Int] = Array[Int](10)
    for(i <- 0 until 10){
      arr(i) = scala.io.StdIn.readInt()
    }
    
    for(i <- 0 until 10){
      current_element = arr(i)
      j = i-1
    }
    while(j >= 0 && arr(j) . current_element){
      arr(j+1) = arr(j)
      j = j - i
    }
    arr(j+1) = current_element
    
  }
}

