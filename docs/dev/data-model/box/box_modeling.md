# Ergo Box Modeling

> [From Keith Lim](https://keitodot.medium.com/ergo-box-m-f58f444e00d5)


## Details of a Box

Boxes are a core element within a UTXO system. It can be seen as an object that carries the value of currency within a blockchain. The beauty of the Ergo blockchain is that it provides boxes with [registers](registers.md) that are guarded by a contract.

The registers allow the storage of data and information that is stored at addresses in the blockchain. If compared to a component, in the real world, these boxes can be seen in forms like remote control, or a piggy bank on steroids, or a basic cup that allows only liquid to be poured in. If we were to take a cup to be used as an example.

**A cup**

- Used mainly to store liquid
- Store up to a certain amount of liquid

If we were to replicate it into a box, we can do something similar like

**A cup box**

- Can store only Ergs, or a specific token
- Store up to a certain amount of it (guard script)

The guard script or the contract essentially forces a function to be placed onto the box. Without the guard script, a box is essentially a storage box that allows you to store information or an amount of currency. The implementation of guard scripts that sets specific rules for the boxes, gives the boxes a form of rigidity which in turn, gives it its function. Like a remote control for instance. We do not care about how the internal system (guard script) of a remote control works or the data that is transmitted (registers and data storage). All we care about is that when we press a button on the remote control, it transmits the data needed to the TV and changes to the desired channel.
What is Box Modeling?

Box modelling is a framework that allows developers or box designers to design a box to carry out specific functions. Having a framework allows structured and easily followable instructions to design and to comprehend the functions that are carried by a box, and how the functions operate.
Rules to Modeling

A blockchain is essentially a financial canvas. It provides developers, engineers, and designers to design financial systems on top of it. However, a flawed design will cause a system to be susceptible to security attacks, unscalable designs, and inefficient processes. To prevent these flaws, we have to consider the opposite of it when designing.
Three rules to box design

##### Security

Ensuring that the box can not be abused by outsiders

##### Scalability

Allowing the system or design to be carried out in a format where it can process multiple requests simultaneously

#####  Efficient

Simplistic design to allow engineers to easily comprehend and improve on the design

## Box Modeling Framework

Before considering the three rules. We should understand the basics of modelling a box.

When modelling a box, we should first ask ourselves these questions:

##### What is the function of this box?

For example, a lending box is a box that facilitates the process of getting a loan

##### What data should the box store?

In regards to the function of the box, we should consider what data should be stored in the box for it to carry out its function. For example, a lending box will store details about the lending information in its registers

##### How can the box carry out its function?

This part has a complication that comes with it. As we have to start thinking about it in terms of the overall transaction as a whole rather than the box itself. This is also the part where we write the guard script (aka smart contract) so that it carries out the function that it is supposed to carry through the usage of the data stored in the registers.
Registers

Registers stores data in a few formats. These can be separated into, single data or multiple entries.

**Single data:**

- `Long`
- `Coll[Byte]` aka *String*
- `Bool`

**Multiple entries:**

- `Coll[Long]`
- `Coll[Coll[Byte]]`
- `Coll[Bool]`

As we move forward, we’ll look into how we can use these ideas and concepts to create replicability and a framework to design boxes efficiently and blow the shrouds of confusion and overwhelming information into a simple step by step guide to modelling boxes.
