---
tags:
  - Stealth Address
---
# Stealth Addresses

Stealth Addresses are crafted to ensure *recipient* privacy during transactions. Leveraging a non-interactive [Diffie-Hellman key exchange](diffie.md), they facilitate the creation of distinct one-time addresses for every transaction. While enabling recipients to securely receive funds, the linkage between the transactions and their original public address remains concealed, thereby significantly enhancing the recipient's privacy throughout the transactions.

With the advent of [ErgoMixer](ergomixer.md) version 4.4.0, support for Stealth Addresses has been rolled out. ErgoMixer assists in the creation and management of your Stealth Addresses for receiving payments. It's pivotal to note that Stealth Addresses aren’t directly payable. The sender is required to use [this tool](https://ergomixer.github.io/stealth/) to generate a *Stealth Payment Address*, which can thereafter be used like any standard address.

## Example: Stealth Addresses for Donations

Consider a scenario where you wish to place a donation address on your website. Traditionally, all transactions to this address are visible on the blockchain, revealing the donation amounts you receive. A common workaround has been generating a new donation address for every user, a tedious task. Stealth Addresses simplify this. By sharing your stealth address, individuals can generate a unique Stealth Payment Address to send funds. You can then locate the UTXO boxes associated with these Stealth Payment Addresses and collect the funds. This mechanism keeps your transactions hidden on the blockchain, preserving your privacy without the need to generate new addresses for everyone.

## Covert vs Stealth Addresses

Covert and Stealth Addresses in Ergo cater to differing levels of privacy. Covert Addresses enable users to receive funds at a public address, not directly tethered to their actual wallet, aiding in obscuring the transaction trail. Conversely, Stealth Addresses amplify privacy by generating unique, one-time addresses for every transaction. In this arrangement, a recipient shares a public address, which a sender leverages to create a unique address for every transaction. This distinct address encases the payment in a secure box, which remains unlinkable to the recipient's shared public address. While both address types strive to bolster privacy by mitigating the linkage of transactions to the original address, Stealth Addresseses excel by ensuring that every transaction utilizes a new, one-time address, considerably impeding the ability to trace transactions.


## How Stealth Addresses Work

Stealth Addresses in Ergo are engineered to maintain transaction confidentiality. Here’s a streamlined outline of their functioning based on the [EIP-41 standard](https://raw.githubusercontent.com/ergoplatform/eips/d21280977f2c21dc733632c48c98d0f614bc6123/eip-0041.md):

1. **Stealth Address Generation**:
      - Alice, a seller, crafts a Stealth Address and shares it, perhaps on her website. This address embodies her public key, without exposing any identifiable information on the blockchain.
      
2. **Stealth Payment Address Creation**:
      - Bob, a buyer, intending to pay Alice, utilizes the shared Stealth Address to generate a unique Stealth Payment Address for the transaction at hand.
   
3. **Payment Transaction**:
      - Bob initiates a payment to the Stealth Payment Address, triggering the creation of a specialized box on the blockchain to harbor the payment. This box is accessible solely by Alice and bears no link to the shared Stealth Address.
      
4. **Unique Identifiers**:
      - As the transaction unfolds, unique identifiers are crafted and stowed in the payment box, ensuring only Alice can access it.
      
5. **Verification**:
      - When Alice wants to access the payment, a script checks the identifiers to ensure everything is correct and allows Alice to open the box and receive her payment.
      
6. **Discovering Payments**:
      - Alice's wallet autonomously scouts for any new payments directed to her by scanning for such boxes, enabling her to securely and privately access her funds.

This mechanism empowers Bob to pay Alice securely and privately by establishing a unique one-time payment address for each transaction, assuring that the payment details are veiled from everyone except Alice.

