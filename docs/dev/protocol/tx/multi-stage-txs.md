# Multi-Stage Transactions

A simple transaction (tx) is the foundation of all transactions, representing a direct exchange between two parties. The advent of Smart Contracts enables the creation of autonomous systems that can handle complex real-world scenarios on the blockchain.

## What Are Multi-Stage Transactions?

Multi-stage transactions involve multiple steps, where each step is a separate transaction that must be successfully executed to complete a larger objective. Unlike simple one-to-one transfers, these transactions require coordination across various stages, often governed by intricate smart contract logic.

For example, multi-stage transactions may be required in scenarios involving complex conditions or timed events, such as escrow services, staged payments, or multi-party agreements. Each stage relies on the execution of a preceding step, making the entire process more secure and robust.

A classic illustration of a multi-stage transaction is the **pin-lock contract**, where multiple layers of validation or condition checks must be met before the final transaction can occur. The complexity of multi-stage transactions can vary, but their key feature is the chaining of multiple transactions to complete a scenario.

## Real-World Lending as a Multi-Stage Transaction

Let’s use a traditional lending process as an example. While in the real world, lending may seem like a single transaction, when mapped onto a blockchain, it can be broken down into a **multi-stage transaction** process:

### Stages of a Lending Process in Blockchain

1. **Loan Request Stage**:
   - **Real World**: A borrower requests a loan from a lender with agreed terms, such as the loan amount and interest rate.
   - **Blockchain**: The borrower creates a smart contract (or box) requesting funds. This smart contract includes conditions, such as the repayment terms and the interest rate.

2. **Loan Approval and Funding Stage**:
   - **Real World**: The lender approves the request and disburses the loan.
   - **Blockchain**: The lender funds the borrower’s smart contract, which triggers the transfer of funds to the borrower upon satisfying the conditions set in the contract.

3. **Loan Utilization Stage**:
   - **Real World**: The borrower uses the loan for business purposes.
   - **Blockchain**: The borrower accesses the funded box, transferring the loaned amount into their own account for use.

4. **Repayment Stage** (This is where the multi-stage aspect becomes evident):
   - **Real World**: The borrower repays the loan with interest in agreed-upon installments.
   - **Blockchain**: The borrower initiates a series of transactions, where each monthly repayment is a separate transaction executed on the blockchain. These repayments continue until the full amount (plus interest) has been transferred back to the lender.

5. **Completion Stage**:
   - **Real World**: The loan agreement concludes when the borrower pays off the debt.
   - **Blockchain**: The smart contract governing the loan automatically closes once the final repayment transaction is executed, concluding the multi-stage process.

### Why is This a Multi-Stage Transaction?

Each step in the lending process on the blockchain is **linked** to the success of the previous one. The loan cannot be funded until the borrower’s smart contract is created, and repayments cannot occur until the funds are utilized. The entire process involves **multiple transactions** (loan request, funding, repayments, and final closure), making it a perfect example of a multi-stage transaction.

## Translating Real-World Scenarios to Blockchain: A Summary

| Real-World Lending Scenario                                                                                         | Equivalent Blockchain Transaction                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Borrower requests a loan with specified terms.                                                                   | Borrower creates a smart contract requesting the loan amount, specifying the conditions for release.                                                     |
| 2. Lender approves and sends the loan.                                                                              | Lender funds the borrower’s smart contract.                                                                                                             |
| 3. Borrower utilizes the loan.                                                                                      | Borrower accesses the funds.                                                                                                                            |
| 4. Borrower repays the loan in installments.                                                                        | Borrower makes multiple transactions over time to repay the loan with interest.                                                                          |
| 5. Loan transaction concludes.                                                                                      | Smart contract closes once all repayments are made, completing the multi-stage transaction.                                                              |
