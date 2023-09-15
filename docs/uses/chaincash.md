# ChainCash

ChainCash is a decentralized, peer-to-peer monetary system aimed at creating money collectively through trust and blockchain assets. The system addresses the issue of inelasticity in blockchain asset supply, which hinders the real-world usage of blockchain assets in many cases. ChainCash allows for the elastic creation of money in a decentralized manner while maintaining the quality of the currency.

## New Developments: L1 and L2 Payments

One of the latest advancements in ChainCash involves the development of contracts that allow payments to be executed either on Layer 1 (L1) or Layer 2 (L2), with a unified redemption contract serving both layers. This opens up the possibility for various applications, such as privacy enhancements like mixing. For instance, you could transfer an asset worth the equivalent of a kilogram of gold on L1 for maximum security, or opt for a quicker L2 transaction equivalent to a couple of grams of gold. The unified redemption contract simplifies the process, working seamlessly irrespective of the initial layer of the transaction. Although still in development, this feature is showing promising capabilities for enhancing both security and efficiency.

## Unit of Account: Gold

Inspired by historical peer-to-peer monetary systems such as the WAT system, ChainCash uses gold as its unit of account. One ChainCash token represents approximately one milligram of gold. This system enables users to issue notes of arbitrary values, which may or may not be backed by reserves in various digital tokens or real-world assets.

## Currency Quality and Trust

To maintain the quality of the currency, acceptance of a note depends on the collateral or trust in the issuer. Participants can issue notes without any reserves, allowing for different collateralization levels within various economic circles. As notes circulate, their quality generally improves due to the collective collateral and trust backing them.

## Implementation Details

ChainCash is implemented using two contracts on the Ergo blockchain: one for notes and one for reserves. The off-chain logic can track different note and reserve contracts, support various acceptance predicates and redemption mechanisms, and accommodate complementary currency systems such as Local Exchange Trading Systems (LETS) and local currencies.

Although Layer Two implementation is still under consideration, ChainCash offers a flexible and decentralized monetary system that can potentially cater to different economic agents globally, addressing the limitations of traditional blockchain assets.

## References

- [ergoforum: ChainCash - A Spender Signed Currency on Ergo](https://www.ergoforum.org/t/chaincash-a-spender-signed-currency-on-ergo/4015)