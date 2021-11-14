## Proof-of-Work Backed Tokens

In Ergo, one token per transaction can be issued, and the token id must be the same as id of the box of the first input. 

Thus if you have generated a box you know id of the future token. And this id is calculated via hashing.

Thus via iterating over a register (e.g. `R4`) used as a nonce, you can create a token with specific id properties, e.g. starting with certain number of zeroes. So some work could be required in order to make such a token. Something like VanityGen-adress in Bitcoin, but now VanityGen token )

Then some contracts may accept such PoW-backed NFTs only. 

I haven't thought about use-cases though. Maybe some related to filtering out spam.

Full discussions [here](https://www.ergoforum.org/t/proof-of-work-backed-tokens/224)