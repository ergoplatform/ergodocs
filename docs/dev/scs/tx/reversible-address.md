# Reversible Addresses

A reversible address is an example of a multi-stage contract with anti-theft features. It works like this: if you send funds to this address, they can only be spent in a way that allows payments to be reversed for a certain time. This is useful for managing an exchange or mining pool's hot wallet for handling customer withdrawals. A hot wallet is an address for which the private key is stored on the server, making it susceptible to compromise and funds being stolen. To recover any stolen funds in the event of such a compromise, you need to have a trusted party with a private key stored offline. The reversible address is used in a two-stage protocol to ensure that withdrawals can only be made according to the desired rules. If an unauthorized transaction occurs, the abort procedure is triggered using the trusted party's private key, and the funds are diverted to a secure address. These addresses are useful for securing hot-wallet funds and automated-release escrow payments in online shopping.

Assuming that Alice is the public key of the hot wallet and Carol is the public key of the trusted party, the private key of Carol will be needed for reversing payments and must be stored offline. Let b be the estimated number of blocks in 24 hours.
Let Bob with public key Bob be a customer wishing to withdraw funds, which the hot wallet will pay out.
In Ethereum, we can do this by sending funds to an account having a contract C<sub>b</sub> that allows Carol to withdraw funds at least b blocks, and after that, they can only be withdrawn by Bob. We could use the same account (contract instance) for multiple withdrawals by Bob, but the optimal way is to have a new account for each withdrawal, emulating the UTXO model. The funds for this must also come from another account with a contract Ca, ensuring that a withdrawal can only be made to a contract with the structure of C<sub>b</sub>.

In Ergo, this is done by a two-stage protocol, where the second stage implements C<sub>b</sub> and the first stage implements Ca. The following script, called withdrawScript, implements the second stage. This will be the guarding script of the hot wallet's withdrawal transaction paying to Bob.

```java
val bob = SELF.R4[SigmaProp].get // public key of customer withdrawing 
val bobDeadline = SELF.R5[Int].get // max locking height 
(bob && HEIGHT > bobDeadline) || (carol && HEIGHT <= bobDeadline)
```

This above script is referenced in the first stage script given next.

```java
val isChange = {(b:Box) => b.propositionBytes == SELF.propositionBytes} 
val isWithdraw = {(b:Box) => b.R5[Int].get >= HEIGHT + blocksIn24h && b.propositionBytes == withdrawScript }
alice && OUTPUTS.forall({(b:Box) => isChange(b) || isWithdraw(b)})
```

The reversible address is the P2SH address of the above script. Any funds sent to this address are subject to our desired withdrawal rules. In the normal case, Bob will spend the box after roughly blocksIn24h blocks. Suppose an unauthorised transaction from the hot wallet is detected. In that case, an abort procedure is triggered using the private key of Carol, and funds in any unspent boxes sent from the hot wallet are diverted to a secure address. The trusted party (Carol) is bound to the hot wallet address, and a new address is needed for a different trusted party.

Although such addresses are designed for securing hot-wallet funds, they may have other applications. One example is for automated-release escrow payments in online shopping, where Carol can be the public key of any mutually agreed adjudicating party.
