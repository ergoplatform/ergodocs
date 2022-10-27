# ErgoScript Syntax

> 🔗 From [Deco Education - ErgoScript Developer Course](https://github.com/DeCo-Education/ErgoScript-Developer-Course/blob/main/Class-Documents/Class-1/Materials/Class1.MD)


## Basic Syntax In ErgoScript

```scala
val bool: Boolean = true

```

What’s going on here?

`val` - A keyword used to create a basic, immutable, value of any type

`bool` - The name used for the value created

`: Boolean` - Specifying the type of the value, this is not always necessary, but does make code more understandable

`= true` - We are setting our Boolean value bool equal to true

ErgoScript is strongly typed, you should always know what types you are dealing with

> Learn to think in `true` and `false` statements. Booleans (More specifically, Sigma Propositions) are the core of every ErgoScript contract

## More ErgoScript Syntax Examples:

```scala
  if(bool == true){
    val x = 0
    val y = 1
    val z = ((x * y) + 5) - (3 / 2)
  }else{
    val x = 2L
    val y: Coll[Long]  = Coll(0L, 1L, x) // You can build collections of elements
    val z: (Long, Long) = (3, 4)
    val a: (Long, Coll[Long]) = (x, y) // Build complex types by layering together pairs and colls
    val b: Coll[((Long, Long), Boolean)] = Coll(((2L, 4L), true), ((7L, 2L), false))
  }

```

ErgoScript is based off of Scala, which brings means we have some standard functional programming methods and syntax

```scala
// Wrap this val statement into a function that returns a collection of integers paired with longs
val myMap: Coll[(Int, Long)] = {      
val intCollection = Coll(0, 1, 2)
    // Use the map function, a standard FP method that iterates through the entire
    intCollection.map{
        // collection and inputs each element through a function to return a collection of outputs.                  
        (myInt: Int) =>                   
        (myInt, myInt.toLong)
        // We represent our mapping function using a Lambda expression, we define the
        // parameter to be the element of our collection (an Int), then use the
        // arrow operator (=>) in order to show how our parameter maps to an output.
        // We do not need to specify the return value with a keyword        
}                                      
    }

```

### Def vs Val?

```scala

  def computeAsDef(myInt: Int): Int = {
    myInt + 1
  }

  val computeAsVal: Int = {
    (myInt: Int) =>
      myInt + 1
  }

```

The two statements above **do the exact same thing**. The difference is that `val` statements are calculated when the script initializes itself to be run. `def` statements are instead calculated whenever the call is made.
In most instances, you will likely use `val` statements

