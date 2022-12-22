# Identifiability

ErgoUtils now support obfuscating entry points for ErgoMixer.

When you withdraw from the mixer to a wallet, it is obvious that that person has received some funds from the mixer, and when he spends those boxes, it is also obvious that those boxes are from the mixer.

Those who care about privacy and use ErgoMixer, also probably care about not anyone being able to tell that they are using the mixer easily when they interact with their wallets. This tool is designed to address this issue.

Just create an (or more if you wish) obfuscating address with your desired hop number [here](https://ergoutils.org/#/others) and use it permanently. To use it, withdraw from the mixer to the address that is created for you; your received funds in that address will automatically go through some random addresses (randomly created outputs, both number of outputs and output amounts) and finally be received in your wallet.

As an example, try to figure out if this [transaction](https://explorer.ergoplatform.com/en/transactions/9cf412c71fc49a53f7f6ae498f22730be474127436334e5a38da92ce0d40530b) is from the mixer or not - a lot harder to figure out.

As always, utilities in ErgoUtils are completely free to use!

- [ergoutils GitHub](https://github.com/anon-real/ergoutils)
- [mixerHop.js](https://github.com/anon-real/ErgoUtils/blob/master/src/utils/mixerHop.js)