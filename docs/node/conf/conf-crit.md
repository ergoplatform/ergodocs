# Critical-Dispatcher Configuration Settings

The `critical-dispatcher` is a dedicated actor dispatcher, utilized exclusively by the block candidate generator and `NodeViewHolder` actors within the system. This dispatcher is integral to maintaining critical tasks which require isolation from other non-critical activities.

## Dispatcher Type
```conf
type = Dispatcher
```
This configuration sets the type of the dispatcher. In this case, it is set as `Dispatcher`.

## Executor
```conf
executor = "thread-pool-executor"
```
The `executor` is the mechanism responsible for running tasks given to it by the dispatcher. Here, it is configured to use the `"thread-pool-executor"`, which creates a pool of worker threads for executing tasks.

## Thread-Pool-Executor
### fixed-pool-size
```conf
fixed-pool-size = 2
```
This configuration specifies the number of threads in the thread pool for the `thread-pool-executor`. It is set to a fixed size of 2 in this configuration.

## Throughput
```conf
throughput = 1
```
`throughput` is the maximum number of messages to be processed per actor before the thread is made available to other actors. This setting helps control how long a thread can be occupied by an actor. In this case, it is set to 1.

## Complete Configuration Code

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
This configuration ensures that critical tasks handled by the block candidate generator and `NodeViewHolder` actors are allocated dedicated threads, thereby promoting efficient execution.