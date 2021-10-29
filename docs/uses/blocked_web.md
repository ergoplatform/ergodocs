## [(E)mail Client for Limited or Blocked Internet](https://www.ergoforum.org/t/e-mail-client-for-limited-or-blocked-internet/134)

There are two motivations for this post

1. Some countries, such as China and Belarus are already blocking Tor. We can expect that in future some countries will try to block cryptocurrency protocols in a similar way. 

2. [Internet just being restored in Iran after week-long shutdown](https://netblocks.org/reports/internet-restored-in-iran-after-protest-shutdown-dAmqddA9) caused by unrest. Previously there were partial or complete shutdowns in Egypt, Ethiopia, Sudan, Turkey. 

However, people have right to store value available, whether the value is under threat from  monetary policies, political instability, or war. Happily, with digital communications and digital gold this problem could be solved. 


As possible solution for Bitcoin, [Blockstream satellite network](https://blockstream.com/satellite/) could be used, however, satellite signal could be jammed. Another workaround which I am going to propose is to use e-mail (which is last to be blocked usually) or other low-bandwidth and not very interactive means of communication (fax, modem call over a landline to a bulletin board system, mail).

So assume Alice is willing to buy *X* ergs from Bob (paying with cash), but internet is very limited or does not working in their area. Bob owns a box protected by a public key (stored locally). Then the protocol could be as follows.

1. Bob is creating transaction from his box which is creating a new box where *X* ergs are locked by the condition "Before deadline: Bob's signature and spending transaction has an output of *X* ergs which belongs to Alice's public key; After deadline: Bob's signature". I will refer to the new box as to the "deal box" further. Please note that for a signed transaction outputs with respective identifiers are known.

2. Bob sends the transaction over (e)mail to a gateway. Gateway sends efficient [NiPoPoW](https://nipopows.com/) proof for a header having enough confirmations + proof of box membership against state digest from the header. This proof is small, tens of kilobytes. for better security, Bob may ask another gateway for header proof as well. 

3. Bob shows proofs to Alice. Alice checks proofs and also that deadline will not likely met when a new transaction with their deal will reach the Ergo blockchain. Bob signs the new  transaction which is spending the deal box created on step 1 and creating the output box for Alice.

4. Now Alice sends the transaction signed by Bob  to the gateway and gets the proof of inclusion from it. 

With proofs of such size (tens of kilobytes), email / fax / ADSL modem or even paper work fine as means of communication between the users and the gateways.
