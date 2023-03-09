
# critical-dispatcher 

The `critical-dispatcher` is used only for the block candidate generator and `NodeViewHolder` actors. 


## type
```conf
type = Dispatcher
```

## executor
```conf
executor = "thread-pool-executor"
```

## thread-pool-executor
### fixed-pool-size
```conf
fixed-pool-size = 2
```
## throughput
```
throughput = 1
```


## Full Code Snippet


```conf
critical-dispatcher {
  type = Dispatcher
  executor = "thread-pool-executor"
  thread-pool-executor {
    fixed-pool-size = 2
  }
  throughput = 1
}
```