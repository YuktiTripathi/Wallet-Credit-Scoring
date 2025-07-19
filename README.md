# Wallet-Credit-Scoring

This repository contains a Python-based machine learning model that assigns a credit score between 0 and 1000 to wallet addresses on the Aave V2 protocol. The score is derived solely from on-chain transaction history, with higher scores indicating reliable financial behavior and lower scores reflecting risky or unstable activity.

## Project Overview

In traditional finance, credit scores are a cornerstone of risk assessment. The decentralized nature of DeFi lacks a direct equivalent, making it difficult to quantify the reliability of a given wallet. This project addresses that gap by creating a behavioral credit score based on how users interact with the Aave V2 lending protocol.

The model ingests raw, transaction-level data and uses an unsupervised learning approach to group wallets into distinct behavioral clusters, which are then ranked and scored.

## Architecture and Processing Flow

The credit scoring process is executed in a single script (`score_wallets.py`) and follows a clear, multi-step architecture:



1.  **Data Loading & Preprocessing**: The script begins by loading the raw JSON transaction data. It unnests the nested `actionData` object into a flat DataFrame structure. Key numerical fields like `amount` and `assetPriceUSD` are converted to numeric types, and a final `amountUSD` is calculated. To prevent outliers from skewing the model, transaction values are capped at the 99th percentile.

2.  **Feature Engineering**: This is the core of the model where raw data is transformed into meaningful behavioral indicators for each `userWallet`. Key engineered features include:
    * **Transactional Volume & Frequency**: `transaction_count`, `total_volume_usd`, `avg_transaction_usd`, `transactions_per_day`.
    * **Account Maturity**: `account_age_days` (time since first transaction).
    * **Behavioral Ratios (Critical for Scoring)**:
        * `repay_borrow_ratio`: A measure of loan repayment diligence.
        * `liquidation_ratio`: A strong indicator of high-risk behavior.
        * `net_supply_ratio`: Indicates whether a user is a net supplier of capital (positive) or a net withdrawer (negative).
    * **Action Counts**: The total count for each transaction type (`deposit`, `borrow`, `repay`, `liquidationcall`, etc.).

3.  **Feature Scaling**: All engineered features are standardized using `StandardScaler`. This ensures that features with larger scales (like `total_volume_usd`) do not disproportionately influence the clustering algorithm compared to smaller-scale ratio features.

4.  **Unsupervised Clustering**: A **K-Means clustering algorithm** is used to group the wallets. K-Means partitions wallets into a predefined number of clusters (in this case, 10) based on their scaled feature similarities. Each resulting cluster represents a distinct behavioral archetype (e.g., "High-Risk Borrower," "Consistent Supplier").

5.  **Scoring and Ranking**:
    * The centroids (average feature values) of each cluster are analyzed to determine their risk profile.
    * A `risk_score` is calculated for each cluster, heavily penalizing liquidations while rewarding high repayment ratios and net supply behavior.
    * Clusters are ranked based on this risk score.
    * Finally, this rank is mapped to a credit score between 0 and 1000, where the lowest-risk cluster receives the highest score. A small random value is added to differentiate wallets within the same cluster.

## How to Run the Model

1.  **Prerequisites**: Ensure you have Python 3 and the following libraries installed:
    ```bash
    pip install pandas scikit-learn numpy
    ```
2.  **Data**: Place the `user-wallet-transactions.json` file in the same directory as the script.
3.  **Execute**: Run the main script from your terminal.
    ```bash
    python score_wallets.py
    ```
4.  **Output**: The script will generate a `wallet_scores.csv` file containing two columns: `userWallet` and `credit_score`.


