# Bounded Mailbox Configuration

The `bounded-mailbox` configuration specifies the settings for the bounded mailbox type, which limits the maximum number of messages that can be stored in an actor's mailbox.

## Mailbox Type
```conf
mailbox-type = "akka.dispatch.NonBlockingBoundedMailbox"
```
The `mailbox-type` setting determines the type of mailbox used. Here, the `NonBlockingBoundedMailbox` type is selected. This mailbox type provides a capacity-constrained, non-blocking, and thread-safe message queue for your actors.

## Mailbox Capacity
```conf
mailbox-capacity = 5000
```
The `mailbox-capacity` setting specifies the maximum number of messages that the mailbox can hold. In this configuration, the capacity is set to 5000 messages. Once this limit is reached, the mailbox refuses to accept more messages until space becomes available.

The `bounded-mailbox` configuration helps control the load on your actor system by limiting the number of unprocessed messages an actor can receive, preventing it from becoming overwhelmed. It is a vital configuration for ensuring the resilience and stability of your system.