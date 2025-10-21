---
tags:
  - EIP
---

# EIP-0001: UTXO-Set Scanning Wallet API

Motivation
----------

Currently, the Ergo node wallet is able to search for boxes protected only by simplest scripts associated with P2PK
addresses which is a large barrier for dApps. This makes development of external applications which use smart contracts
quite challenging. Development would involve scanning the blockchain state independently by the off-chain portion of
the dApp itself with handling forks, confirmation numbers, and so on.

This Ergo Improvement Proposal focused on extending the wallet to be able to serve the needs of external applications by providing
a flexible scanning interface and the possibility for applications to register scans with the wallet to ensure that they are tracked. Scans that have successfully passed are considered to belong to the application.

Each scan has a given scan ID, and each box found that matches said scan is tracked by the wallet and thus is associated with the scan ID. Among possible scans, there are some pre-defined scans
implemented by the node wallet, to track wallet's public keys and also mining rewards. Other scans are not directly implemented inside of
the wallet but can be added by a user or an external application.

Specification: Scanning
-----------------------

A new request to scan is initiated which [registers](registers.md) said scan to be checked for all future UTXO-set changes (thus it is forward-looking).

A predicate (function which returns a boolean value for a box) is required to register a scan.
Predicates available are:

* `CONTAINS(register, value)` returns true if certain register contains given value. If *register* argument is missed, R1 (script register) will be scanned
* `EQUALS(register, value)`returns true if certain register contains only given value. If *register* argument is missed, R1 will be scanned
* `CONTAINS_ASSET(assetId)`- if a box contains asset with a given id
* `AND(predicate1, predicate2, ..., predicateN)` - if all the children predicates are true
* `OR(predicate1, predicate2, ..., predicateN)` - if one of the children predicates is true

*value* field in the predicates above is about encoded sigma value, *assetId* is about just 32-bytes long byte array.

The following is an example of a predicate which states that the registered scan will search for boxes that contain a
given asset and also the provided bytes in R1 (*"0e24..."* in the example is a byte array which contains a script
represented in ErgoTree form).

```haskell
AND(
    CONTAINS_ASSET("bc01de24311298068c07857d3860625abf3277997e2a2b8ff8ea91dda28d47a5"), 
    CONTAINS("0e240008cd029f2230dbe53f6b84d8a884a3407c3dffe43daf8037445441be7cdcd261feeaa4")
   )
```

This must be formatted in JSON and sent as a request to register the scan.
This is done via the endpoint: `/scan/register`.
In addition to root predicate the scheme also requires a scan name
(UTF-8 characters requiring for up to 255 bytes to be encoded).

The following is an example of valid JSON for a scan register request for the previous predicate.

```json
{
    "scanName": "Asset and script tracker",
    "trackingRule" : {
        "predicate": "and",
        "args":[
            {"predicate": "contains", "value": "0e240008cd029f2230dbe53f6b84d8a884a3407c3dffe43daf8037445441be7cdcd261feeaa4"},
            {"predicate": "containsAsset", "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"}
        ]
    }
}
```

The node API returns an error if something wrong with request. If it is well formed then the wallet will return a new scan ID which the user/dApp can use to reference said scan. The scan identifier(ID) is encoded as 16-bit long signed but always positive integer.

Other basic endpoints include:

* `/scan/listAll` returns all the registered scans
* `/scan/deregister` stops tracking a given scan based on the ID provided

Specification: Interaction With the Wallet
------------------------------------------

If a scan has found a box which also could be spent by the node wallet, there is a question whether the box should be
shared with the wallet or not. There are three options for corresponding *walletInteraction* :

* **off** - add found boxes to the scan only
* **shared** - add found boxes to the scan if they belong to the wallet (so associated with P2PK scripts)
* **forced** - add found boxes to the wallet

example:

```json
{
    "scanName": "Script tracker",
    "trackingRule" : {
        "predicate": "contains", 
        "value": "0e240008cd029f2230dbe53f6b84d8a884a3407c3dffe43daf8037445441be7cdcd261feeaa4"       
    },
    "walletInteraction": "forced"
}
```

Specification: Adding Boxes Externally
--------------------------------------

Sometimes it is simpler for an external application to find relevant boxes itself without using the
wallet scanner. For that we have the following endpoint:  

* `/scan/addBox`

Specification: Removing False Positive Boxes
--------------------------------------------

The wallet collects boxes according to the scanning rules used. However, a box which passes the predicate filter may still not
necessarily be wanted as part of a scan. As such, an application can inform the wallet if a box is not needed to be
tracked and can be ignored.

* `/scan/stopTracking/{scanId}/{boxId}` - to inform the wallet that a box does not belong to a given scan and
       thus should not be tracked anymore

Specification: Reading Boxes
-----------------------------

Once boxes are recognized, an external application can use them. To get all of the boxes that have ever been tracked by a scan, or
current tracked unspent boxes, the following API methods are proposed:

* `/scan/boxes/{scanId}`
* `/scan/boxesUnspent/{scanId}`

Specification: List Of All Proposed Endpoints
-----------------------------

* POST: `/scan/register` - Registers/begins tracking a scan based on a provided predicate
* POST: `/scan/deregister` - Stops tracking a given scan based on the ID provided
* POST: `/scan/addBox` - Manually add box
* POST: `/scan/stopTracking` - To inform the wallet that a box does not belong to a given scan
* GET: `/scan/listAll` - Returns all the registered scans
* GET: `/scan/boxes/{scanId}` - List all boxes that have ever been tracked by the scan
* GET: `/scan/boxesUnspent/{scanId}` - List all boxes that have been tracked by the scan and are still unspent/part of the UTXO set

Specification: List Of Implemented Endpoints
--------------------------------------------

* POST: `/scan/register` - 3.3.0
* POST: `/scan/deregister` - 3.3.0
* POST: `/scan/addBox`
* POST: `/scan/stopTracking` - 3.3.0
* GET: `/scan/listAll` - 3.3.0
* GET: `/scan/boxesUnspent/{scanId}` - 3.3.0

Objects and endpoints description can be found in [openapi.yaml file in Ergo protocol reference client repository](https://github.com/ergoplatform/ergo/blob/master/src/main/resources/api/openapi.yaml).

Specification: Predefined Scans
----------------------------------------

There are some predefined scans in the node, such as SimplePayments and MiningRewards. External scans has exclusive
priority over predefined ones, this does mean that if a box could be, for example, associated with both the
SimplePayments and an external scan, then the box will be associated with the external scan **only**.

The SimplePayments scan always has id == 10, MiningRewards has id == 9.
The SimplePayments default wallet scan is using the `OR(CONTAINS(pk_1), ..., CONTAINS(pk_n))` predicate, where
`pk_1, ..., pk_n` are script bytes of the P2PK addresses of the wallet. MiningRewards predicate is similarly about
mining script bytes corresponding to the P2PK addresses of the wallet.

UTXO-Set Scanning dApp Examples
--------------------

Below example scenarios for dApp use cases are presented.

* *Crowdfunding*

The simplest crowdfunding script is provided in Section 2.3 of [ErgoScript Whitepaper](https://ergoplatform.org/docs/ErgoScript.pdf).

There are two roles in the script, a user and a project. For a user, scanning pledge boxes of self would be
just `EQUALS(script)`, where `script` are the bytes of a script from the Whitepaper that embeds both the backer and
project public keys. The user can withdraw the pledge box if it is still unspent after the crowdfunding deadline.
However, a user may be interested to know the state of the campaign at a given moment. The project also needs to collect all of the pledge boxes.
For this, the simplest option is to use `CONTAINS(projectPubKey)` predicate
, however if the project is using its key for other purposes than the crowdfunding, then the filter will
give false-positives. To reduce false positives count, instead of the public key, a larger part of the script which
contains *projectPubKey* but does not contain *backerPubKey* could be used within `CONTAINS()`.

* *Mixing*

For mixing scripts, see Section 3.3.1 of
[Advanced ErgoScript Tutorial](https://ergoplatform.org/docs/AdvancedErgoScriptTutorial.pdf). To find her half-mix coin
in the mixing application, Alice can simply watch for her public key. Then she is watching for this box, and once the
box is spent, she figures out the outputs of the spending transaction and adds her output manually to the wallet. Bob can
on his side can track a large enough part of the half-mix script not including Alice's pubkey u.

* *LETS*

We consider a trusted LETS as described [here](trustless-lets.md)

Management contract uses a singleton token, as does the exchange contract as well. Thus for both the managers
and the user, boxes can be tracked via `CONTAINS_ASSET()` filter.
