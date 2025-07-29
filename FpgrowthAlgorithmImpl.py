import pandas as pd
import warnings
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder
import time


def association_rules_using_fpgrowth(databaseName, minSupport, minConfidence):
    start_time = time.time()
    # Suppress DeprecationWarnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    dataFrame = pd.read_csv(databaseName)
    dataFrame.shape
    transaction = []
    for i in range(0, dataFrame.shape[0]):
        transaction.append([str(dataFrame['Transaction'][i])])

    transactions = [transaction.split(',') for transaction in dataFrame['Transaction']]
    te = TransactionEncoder()
    te_array = te.fit_transform(transactions)
    dataset = pd.DataFrame(te_array, columns=te.columns_)

    res = fpgrowth(dataset, min_support=minSupport, use_colnames=True)
    if res.size > 0:
        result = association_rules(res, metric="confidence", min_threshold=minConfidence)
    else:
        print("No frequent itemset found with minimum support of " + str(minSupport))
        return 0

    print("\nAssociation Rules using FP-growth algorithm are: \n")
    ruleCounter = 1
    for _, rule in result.iterrows():
        # print("Consequents:", set(rule['consequents']))
        # print("Antecedents:", set(rule['antecedents']))
        print(f"Rule {ruleCounter}: {set(rule['antecedents'])} -> {set(rule['consequents'])}")
        print("Support:", round(rule['support'],4))
        print("Confidence:", round(rule['confidence'],4))
        print("-" * 75)
        ruleCounter += 1

    end_time = time.time()
    return end_time - start_time
    # print("\n\n Total execution time of FP-growth algorithm is " + str(round(end_time - start_time, 4)) + " seconds.\n\n")