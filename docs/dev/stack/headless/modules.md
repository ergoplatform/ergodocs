## Modules Of The Ergo Headless dApp Framework

### Box Spec
This module exposes the `BoxSpec` struct, which allows you to create a specification of a UTXO. This is used for defining the boxes which are required for the actions of your protocol.

```rust
/// A specification which specifies parameters of an `ErgoBox`.
/// This spec is used as a "source of truth" to both verify and find
/// `ErgoBox`es which match the spec. This is often used for defining
/// Stages in multi-stage smart contract protocols, but can also be used
/// to define input boxes for Actions.
/// All fields are wrapped in `Option`s to allow ignoring specifying
/// the field.
#[wasm_bindgen]
#[derive(Clone)]
pub struct BoxSpec {
    /// The address of the box
    address: Option<ErgoAddressString>,
    /// The allowed range of nanoErgs
    value_range: Option<Range<NanoErg>>,
    /// A sorted list of `Constant`s which define registers
    /// of an `ErgoBox`.
    /// First element is treated as R4, second as R5, and so on.
    registers: Vec<Option<Constant>>,
    /// A sorted list of `TokenSpec`s which define tokens
    /// of an `ErgoBox`.
    tokens: Vec<Option<TokenSpec>>,
    /// An optional predicate which allows for defining custom
    /// specification logic which gets processed when verifying
    /// the box.
    predicate: Option<fn(&ErgoBox) -> bool>,
}
```

Once you've constructed a `BoxSpec`, you have a number of essential methods that simplify the experience of writing off-chain code for dApps.

For example, `verify_box` allows you to test whether an `ErgoBox` you provide as input matches the specification you created with your `BoxSpec`.

```rust
pub fn verify_box(&self, ergo_box: &ErgoBox) -> Result<()> {
```

### Box Traits

This module exposes two traits:

1. `WrappedBox`
2. `SpecifiedBox`
3. `ExplorerFindable`

All `ExplorerFindable` structs are also `SpecifiedBox`es which are all `WrappedBox`es. In your off-chain code you will be defining all of your inputs UTXOs to actions as structs that implement `SpecifiedBox`, while automatically deriving `WrappedBox` and `ExplorerFindable` without any extra work.

`WrappedBox`es provide a simplified interface for interacting with `ErgoBox`es. `SpecifiedBox`es on the other hand specify that a given `WrappedBox` also implements a `BoxSpec` via the `box_spec()` method. And lastly `ExplorerFindable` provides an interface on top of the `SpecifiedBox` trait for finding boxes that match the `BoxSpec` from an Ergo Explorer API instance.


### Specified Boxes
This module exposes generic "Specified Box" structs that implement the `SpecifiedBox`/`WrappedBox`/`ExplorerFindable` traits. These boxes can be used as inputs for Actions in your off-chain protocol code, while also enabling front-end devs to easily gain access to on-chain data, such as Oracle Pool data.

Currently Implemented Specified Boxes:
1. ErgsBox
2. ErgUsdOraclePoolBox
3. AdaUsdOraclePoolBox

`ErgsBox` are used for acquiring inputs that hold Ergs inside of them which can be used within your smart contract protocol actions.

`ErgUsdOraclePoolBox` & `AdaUsdOraclePoolBox` provide an extremely simplified interface for both headless dApp developers as well as front-end implementors to utilize data from the two currently running Oracle Pools. These two specified boxes can even be used by wallets/any off-chain application that needs to read the current rates from the Oracle Pool boxes.

The code block below shows how in 4 lines you can read the current Erg-USD oracle pool rate from your preferred Ergo Explorer API instance:

```rust
let url = ErgUsdOraclePoolBox::explorer_endpoint("https://api.ergoplatform.com/api").unwrap();
let response = get(&url).unwrap().text().unwrap();
let oracle_pool_box =
    ErgUsdOraclePoolBox::process_explorer_response(&response).unwrap()[0].clone();
println!(
    "Erg-USD Oracle Pool: {} nanoErgs per USD",
    oracle_pool_box.datapoint()
);
```


### Output Builders
This module exposes structs which provide you with a basic interface
for creating common output UTXOs within your Actions. These are often
used for creating outputs that hold a user's change or pay a tx fee.

Example Output Builders:
1. ChangeBox
2. TokensChangeBox
3. TxFeeBox


### Tx Creation
This module exposes a few basic functions for making your life easier when building `UnsignedTransaction`s inside of your Actions.


### Encoding
This module exposes a number of helpful functions related to encoding/decoding/wrapping/unwrapping values from one form into another.

Examples:

```rust
pub fn erg_to_nano_erg(erg_amount: f64) -> u64;
pub fn nano_erg_to_erg(nanoerg_amount: u64) -> f64;
pub fn unwrap_long(c: &Constant) -> Result<i64>;
pub fn serialize_p2s_from_ergo_tree(ergo_tree: ErgoTree) -> P2SAddressString;
```

### Procedural Macros
This crate exposes three procedural macros to make the life of devs much simpler:

1. WrapBox
2. SpecBox
3. WASMBox

`WrapBox` simply implements the `WrappedBox` trait for you, `SpecBox` implements a customized `new()` method that uses your `BoxSpec` + implements the `ExplorerFindable` trait for you, and `WASMBox` implements the two basic required methods to enable WASM support for your struct (`w_new()` and `w_box_struct()`).

