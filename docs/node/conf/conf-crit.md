
# critical-dispatcher 

```
critical-dispatcher {
  type = Dispatcher
  executor = "thread-pool-executor"
  thread-pool-executor {
    fixed-pool-size = 2
  }
  throughput = 1
}
```
The dispatcher which is used for block candidate generator and `NodeViewHolder` actors only
