In other words, a token that is guaranteed to exist forever, unless it gets garbage-collected!


```scala
    {
      val isPerpetual = {(b: Box) =>
        b.propositionBytes == SELF.propositionBytes && b.tokens == SELF.tokens
      }

      sigmaProp(OUTPUTS.exists(isPerpetual))
    }
```

To be precise, this is a perpetual collection of tokens (possibly of size zero). But if you protect a singleton token with this script, then it guarantees the token will never be destroyed other than by garbage collection

See [this thread](https://www.ergoforum.org/t/a-perpetual-token/205/3) for the full discussion.

I apologize for the confusion. Here's the explanation with more details and code blocks to make it easier for a beginner programmer to understand:

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