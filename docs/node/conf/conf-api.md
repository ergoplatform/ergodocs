## api-dispatcher 

Controls the dispatcher for some API-related actors


### type
```
type = Dispatcher
```

The dispatcher is the name of the event-based dispatcher.

### executor
```
executor = "fork-join-executor"
```

What kind of ExecutionService to use

### fork-join-executor
#### parallelism-min
```
parallelism-min = 1
```

Min number of threads to cap factor-based parallelism number to
#### parallelism-factor
```
parallelism-factor = 2.0
```

Parallelism (threads) ... ceil(available processors * factor)

#### parallelism-max
```
parallelism-max
```
The maximum number of threads to limit the factor-based parallelism number to
### throughput
```
throughput = 4
```

Throughput defines the maximum number of messages 
processed per actor before the thread jumps to the next actor.
Set to 1 for as fair as possible.


## Full Code Snippet

```
api-dispatcher {
  # Dispatcher is the name of the event-based dispatcher
  type = Dispatcher
  # What kind of ExecutionService to use
  executor = "fork-join-executor"
  # Configuration for the fork-join pool
  fork-join-executor {
    # Min number of threads to cap factor-based parallelism number to
    parallelism-min = 1
    # Parallelism (threads) ... ceil(available processors * factor)
    parallelism-factor = 2.0
    # Max number of threads to cap factor-based parallelism number to
    parallelism-max = 2
  }
  # Throughput defines the maximum number of messages to be
  # processed per actor before the thread jumps to the next actor.
  # Set to 1 for as fair as possible.
  throughput = 4
}
```


