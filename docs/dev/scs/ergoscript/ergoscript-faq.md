# ErgoScript FAQ

## Why does Ergo use [Coll] instead of an Array?

"The reason for not using just Array as a name is to allow one to one correspondence between ErgoScript and Scala. Array is mutable in Scala, while everything in ErgoScript is immutable. This would be a source of confusion. There was discussion in our Slack (back in 2018-2019) about this name and no better than Coll were proposed. I tried Collection[Int], but it looked ugly and annoying to type. 

Seq is also not good as it is covariant in Scala and Coll is not covariant in ErgoScript."