
# critical-dispatcher 

The `critical-dispatcher` is used only for the block candidate generator and `NodeViewHolder` actors. 


## type
```
type = Dispatcher
```

## executor
```
executor = "thread-pool-executor"
```

## thread-pool-executor
### fixed-pool-size
```
fixed-pool-size = 2
```
## throughput
```
throughput = 1
```


## Full Code Snippet


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