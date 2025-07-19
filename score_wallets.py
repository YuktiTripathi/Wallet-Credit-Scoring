{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9922035e-8da2-4138-8677-76f908b0bbd3",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'src'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 4\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcluster\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m KMeans\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpreprocessing\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m StandardScaler\n\u001b[0;32m----> 4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msrc\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mfeature_engineering\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m engineer_features\n\u001b[1;32m      6\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mscore_wallets\u001b[39m(json_file_path):\n\u001b[1;32m      7\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m      8\u001b[0m \u001b[38;5;124;03m    Loads transaction data, engineers features, clusters wallets,\u001b[39;00m\n\u001b[1;32m      9\u001b[0m \u001b[38;5;124;03m    and assigns credit scores.\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[38;5;124;03m        pandas.DataFrame: A DataFrame with wallet addresses and their credit scores.\u001b[39;00m\n\u001b[1;32m     16\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'src'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from src.feature_engineering import engineer_features\n",
    "\n",
    "def score_wallets(json_file_path):\n",
    "    \"\"\"\n",
    "    Loads transaction data, engineers features, clusters wallets,\n",
    "    and assigns credit scores.\n",
    "\n",
    "    Args:\n",
    "        json_file_path (str): The path to the JSON transaction data.\n",
    "\n",
    "    Returns:\n",
    "        pandas.DataFrame: A DataFrame with wallet addresses and their credit scores.\n",
    "    \"\"\"\n",
    "\n",
    "    # Load and preprocess data\n",
    "    df = pd.read_json(json_file_path)\n",
    "    # ... additional preprocessing ...\n",
    "\n",
    "    # Engineer features\n",
    "    wallet_features = engineer_features(df)\n",
    "\n",
    "    # Scale features\n",
    "    scaler = StandardScaler()\n",
    "    scaled_features = scaler.fit_transform(wallet_features.drop('wallet_address', axis=1))\n",
    "\n",
    "    # Cluster wallets\n",
    "    kmeans = KMeans(n_clusters=5, random_state=42)  # Adjust n_clusters as needed\n",
    "    wallet_features['cluster'] = kmeans.fit_predict(scaled_features)\n",
    "\n",
    "    # Assign scores based on cluster characteristics\n",
    "    # (This will require analyzing the cluster centers)\n",
    "    # For now, a placeholder scoring logic is used.\n",
    "    # A lower cluster number might indicate higher risk in this simplified example.\n",
    "    wallet_features['credit_score'] = (wallet_features['cluster'] + 1) * 200\n",
    "\n",
    "    return wallet_features[['wallet_address', 'credit_score']]\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    scores = score_wallets('data/user-transactions.json')\n",
    "    print(scores)\n",
    "    scores.to_csv('wallet_scores.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47241f0a-0c6d-4f8f-8dfe-ca54ceaeb656",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
