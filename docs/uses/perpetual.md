In other words, a token that is guaranteed to exist forever, unless it gets garbage-collected!
```
    {
      val isPerpetual = {(b: Box) =>
        b.propositionBytes == SELF.propositionBytes && b.tokens == SELF.tokens
      }

      sigmaProp(OUTPUTS.exists(isPerpetual))
    }
```
(Actually, this is a perpetual collection of tokens (possibly of size zero). But if you protect a singleton token with this script, then it guarantees the token will never be destroyed other than by garbage collection.)

See [this thread](https://www.ergoforum.org/t/a-perpetual-token/205/3) for full discussion.


## Multi-stage
In multi-stage protocols, one script refers to the script of the next stage (example in `script1`, we have the statement `hash(OUTPUTS(0).propositionBytes) == script2Hash`).

But suppose we also want the `script2` to refer back to `script1`, (example we want `hash(OUTPUTS(0).propositionBytes) == script1Hash`), then its a cyclic reference. 

One solution is to store `script1Hash` in the register of the box containing `script2`. Additionally, `script1` is modified to ensure that the corresponding register of any box containing `script2` equals `hash(SELF.propositionBytes)`.

EDIT: While the "vanilla" perpetual token is interesting, the more powerful one is the "max-once-per-block-use" perpetual token, which should be a separate design pattern.