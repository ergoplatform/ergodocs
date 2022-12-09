# MultiSig

There are a few options to generate a Multi-Sig wallet on Ergo. The simplest is to download Minotaur Wallet and follow these steps;

Decide first how many people you want to have in your multi-sig, you can create 3-out-of-5, 5-7, or any other combination upto a total of 20 cosigners. 

1. Create a simple wallet for yourself. 
      1. Note that in Minotaur, you can change the settings to advance mode. Then you'll be able to create a wallet with more than 15 mnemonic words and with mnemonic extension phrase.
2. Go to the `Addresses` tab, copy your extended public key and send it to the people you plan to create the wallet with. 

Once you have everyone elses addresses;

1. Create a new multi-sig wallet
2. Set the required cosigner/signature settings (i,e 5 cosigners. 3 signature for 3-out-of-5)
3. Select your wallet from drop down list.
4. Import all other 4 extended public keys (order doesn't matter).
5. Verify if your multisig wallet address is the same as others. 