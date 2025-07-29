import pandas as pd
import warnings
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import time


# from apyori import apriori


def association_rules_using_apriori(databaseName, minSupport, minConfidence):
    start_time = time.time()

    # Suppress DeprecationWarnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    # Load the dataset
    df = pd.read_csv(databaseName)
    pd.set_option('display.max_rows', None)

    # Check the structure and content of the DataFrame
    print("\n")

    # Preprocess the data

    df['Transaction'] = df['Transaction'].str.split(',')
    one_hot_encoded = df['Transaction'].str.join('|').str.get_dummies()

    # Use Apriori algorithm to find frequent itemsets

    frequent_itemsets = apriori(one_hot_encoded, min_support=minSupport, use_colnames=True)

    if frequent_itemsets.size == 0:
        print("No frequent itemset found with minimum support of " + str(minSupport))
        exit()

    print("\n\nAssociation Rules using Apriori algorithm are: \n")
    # Generate association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=minConfidence)

    ruleCounter = 1
    for _, rule in rules.iterrows():
        # print("Antecedents:", set(rule['antecedents']))
        # print("Consequents:", set(rule['consequents']))
        print(f"Rule {ruleCounter}: {set(rule['antecedents'])} -> {set(rule['consequents'])}")
        print("Support:", rule['support'])
        print("Confidence:", rule['confidence'])
        print("-" * 75)
        ruleCounter += 1

    end_time = time.time()
    return end_time - start_time
    # print("\n\n Total execution time of Apriori algorithm is " + str(round(end_time - start_time, 2)) + " seconds.\n\n\n")
