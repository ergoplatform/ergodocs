# Perpetual Tokens

You can use ErgoScript to create a '*perpetual token*', in other words, a token that is guaranteed to exist forever, unless it gets garbage-collected!


```scala
    {
      val isPerpetual = {(b: Box) =>
        b.propositionBytes == SELF.propositionBytes && b.tokens == SELF.tokens
      }

      sigmaProp(OUTPUTS.exists(isPerpetual))
    }
```
To clarify, this construct establishes a collection of perpetual tokens, even if the collection's size is zero. However, should you safeguard a singleton token using this script, it ensures the token will never be destroyed other than by garbage collection.

See [this thread](https://www.ergoforum.org/t/a-perpetual-token/205/3) for the full discussion.

<!--TODO: Segway?-->
## Multi-Stage Protocols

Multi-stage protocols are used in scenarios where multiple scripts interact with each other. In these protocols, one script can reference the script of a subsequent stage.

Consider the following example:

In `script1`, we have the statement:

```scala
hash(OUTPUTS(0).propositionBytes) == script2Hash
```

This means that `script1` is checking whether the hash of the first output's `propositionBytes` equals the hash of `script2`.

However, if we also want `script2` to refer back to `script1`, as in the example below:

```scala
hash(OUTPUTS(0).propositionBytes) == script1Hash
```

We encounter a cyclic reference issue, as both scripts are referring to each other.

To resolve this, we can store `script1Hash` in a register of the [box](box.md) containing `script2`. Additionally, we need to modify `script1` to ensure that the corresponding register of any box containing `script2` is equal to `hash(SELF.propositionBytes)`.

While this "vanilla" perpetual token is interesting, a more powerful and flexible approach is the "max-once-per-block-use" perpetual token, which should be considered a separate design pattern.