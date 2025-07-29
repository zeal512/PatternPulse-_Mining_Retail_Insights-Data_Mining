import time

import pandas as pd
import AprioriAlgorithmImpl
import FpgrowthAlgorithmImpl


def getDatabaseChoice():
    print("1. Amazon")
    print("2. Best Buy")
    print("3. Walmart")
    print("4. K-Mart")
    print("5. Nike\n")

    datasetnumber = input()
    minimumConfidence: str
    minimumSupport: str

    if datasetnumber == "1":
        print("\nYou have selected the Amazon database.\n")
        minSupport = getMinimumSupport()
        minConfidence = getMinimumConfidence()
        amazonDatabase = 'Amazon_Database.csv'
        dataFrame = pd.read_csv(amazonDatabase)

        bruteForceStartTime = time.time()

        transaction = []
        for i in range(0, dataFrame.shape[0]):
            transaction.append([str(dataFrame['Transaction'][i])])

        flattened_list = [sublist[0].split(',') for sublist in transaction]

        frequent_itemsets = generate_frequent_itemsets(flattened_list, float(minSupport/100))

        rules = generate_association_rules(frequent_itemsets, float(minConfidence/100))
        print("\nAssociation Rules:")
        ruleCounter = 1
        for antecedent, consequent, confidence, support in rules:
            print(f"Rule {ruleCounter}: {set(antecedent)} -> {set(consequent)}")
            print("Support: ", support)
            print("Confidence: ", confidence)
            print("-" * 75)
            ruleCounter += 1
        bruteForceEndTime = time.time()

        apriori_time = AprioriAlgorithmImpl.association_rules_using_apriori(amazonDatabase, (minSupport / 100),
                                                                            (minConfidence / 100))
        fpgrowth_time = FpgrowthAlgorithmImpl.association_rules_using_fpgrowth(amazonDatabase, (minSupport / 100),
                                                                               (minConfidence / 100))

        print("\n Total execution time of Brute Force algorithm is " + str(
            round(bruteForceEndTime - bruteForceStartTime, 4)) + " seconds.")
        print("\n Total execution time of Apriori algorithm is " + str(
            round(apriori_time, 4)) + " seconds.")

        print("\n Total execution time of FP-growth algorithm is " + str(
            round(fpgrowth_time, 4)) + " seconds.\n")

    elif datasetnumber == "2":
        print("\nYou have selected the Best Buy database.\n")
        minSupport = getMinimumSupport()
        minConfidence = getMinimumConfidence()
        bestBuyDatabase = 'Best_Buy_Database.csv'

        dataFrame = pd.read_csv(bestBuyDatabase)

        bruteForceStartTime = time.time()

        transaction = []
        for i in range(0, dataFrame.shape[0]):
            transaction.append([str(dataFrame['Transaction'][i])])

        flattened_list = [sublist[0].split(',') for sublist in transaction]
        print(flattened_list)

        frequent_itemsets = generate_frequent_itemsets(flattened_list, float(minSupport / 100))

        rules = generate_association_rules(frequent_itemsets, float(minConfidence / 100))
        print("\nAssociation Rules:")
        ruleCounter = 1
        for antecedent, consequent, confidence, support in rules:
            print(f"Rule {ruleCounter}: {set(antecedent)} -> {set(consequent)}")
            print("Confidence:", confidence)
            print("-" * 75)
            ruleCounter += 1
        bruteForceEndTime = time.time()
        apriori_time = AprioriAlgorithmImpl.association_rules_using_apriori(bestBuyDatabase, minSupport, minConfidence)
        fpgrowth_time = FpgrowthAlgorithmImpl.association_rules_using_fpgrowth(bestBuyDatabase, (minSupport / 100),
                                                                               (minConfidence / 100))

        print("\n Total execution time of Brute Force algorithm is " + str(
            round(bruteForceEndTime - bruteForceStartTime, 4)) + " seconds.")
        print("\n Total execution time of Apriori algorithm is " + str(
            round(apriori_time, 4)) + " seconds.")

        print("\n Total execution time of FP-growth algorithm is " + str(
            round(fpgrowth_time, 4)) + " seconds.\n")

    elif datasetnumber == "3":
        print("\nYou have selected the Walmart database.\n")
        minSupport = getMinimumSupport()
        minConfidence = getMinimumConfidence()
        walmartDatabase = 'Walmart_Database.csv'
        dataFrame = pd.read_csv(walmartDatabase)

        bruteForceStartTime = time.time()

        transaction = []
        for i in range(0, dataFrame.shape[0]):
            transaction.append([str(dataFrame['Transaction'][i])])

        flattened_list = [sublist[0].split(',') for sublist in transaction]
        frequent_itemsets = generate_frequent_itemsets(flattened_list, float(minSupport / 100))

        rules = generate_association_rules(frequent_itemsets, float(minConfidence / 100))
        print("\nAssociation Rules:")
        ruleCounter = 1
        for antecedent, consequent, confidence, support in rules:
            print(f"Rule {ruleCounter}: {set(antecedent)} -> {set(consequent)}")
            print("Confidence:", confidence)
            print("-" * 75)
            ruleCounter += 1
        bruteForceEndTime = time.time()
        apriori_time = AprioriAlgorithmImpl.association_rules_using_apriori(walmartDatabase, (minSupport / 100),
                                                                            (minConfidence / 100))
        fpgrowth_time = FpgrowthAlgorithmImpl.association_rules_using_fpgrowth(walmartDatabase, (minSupport / 100),
                                                                               (minConfidence / 100))
        print("\n Total execution time of Brute Force algorithm is " + str(
            round(bruteForceEndTime - bruteForceStartTime, 4)) + " seconds.")
        print("\n Total execution time of Apriori algorithm is " + str(
            round(apriori_time, 4)) + " seconds.")
        print("\n Total execution time of FP-growth algorithm is " + str(
            round(fpgrowth_time, 4)) + " seconds.\n")

    elif datasetnumber == "4":
        print("\nYou have selected the K-Mart database.\n")
        minSupport = getMinimumSupport()
        minConfidence = getMinimumConfidence()
        kmartDatabase = 'K_Mart_Database.csv'
        dataFrame = pd.read_csv(kmartDatabase)

        bruteForceStartTime = time.time()

        transaction = []
        for i in range(0, dataFrame.shape[0]):
            transaction.append([str(dataFrame['Transaction'][i])])

        flattened_list = [sublist[0].split(',') for sublist in transaction]

        frequent_itemsets = generate_frequent_itemsets(flattened_list, float(minSupport / 100))

        rules = generate_association_rules(frequent_itemsets, float(minConfidence / 100))
        print("\nAssociation Rules:")
        ruleCounter = 1
        for antecedent, consequent, confidence, support in rules:
            print(f"Rule {ruleCounter}: {set(antecedent)} -> {set(consequent)}")
            print("Confidence:", confidence)
            print("-" * 75)
            ruleCounter += 1
        bruteForceEndTime = time.time()
        apriori_time = AprioriAlgorithmImpl.association_rules_using_apriori(kmartDatabase, (minSupport / 100),
                                                                            (minConfidence / 100))
        fpgrowth_time = FpgrowthAlgorithmImpl.association_rules_using_fpgrowth(kmartDatabase, (minSupport / 100),
                                                                               (minConfidence / 100))

        print("\n Total execution time of Brute Force algorithm is " + str(
            round(bruteForceEndTime - bruteForceStartTime, 4)) + " seconds.")
        print("\n Total execution time of Apriori algorithm is " + str(
            round(apriori_time, 4)) + " seconds.")

        print("\n\n Total execution time of FP-growth algorithm is " + str(
            round(fpgrowth_time, 4)) + " seconds.\n")

    elif datasetnumber == "5":
        print("\nYou have selected the Nike database.\n")
        minSupport = getMinimumSupport()
        minConfidence = getMinimumConfidence()
        nikeDatabase = 'Nike_Database.csv'

        dataFrame = pd.read_csv(nikeDatabase)

        bruteForceStartTime = time.time()

        transaction = []
        for i in range(0, dataFrame.shape[0]):
            transaction.append([str(dataFrame['Transaction'][i])])

        flattened_list = [sublist[0].split(',') for sublist in transaction]

        frequent_itemsets = generate_frequent_itemsets(flattened_list, float(minSupport / 100))

        rules = generate_association_rules(frequent_itemsets, float(minConfidence / 100))
        print("\nAssociation Rules:")
        ruleCounter = 1
        for antecedent, consequent, confidence, support in rules:
            print(f"Rule {ruleCounter}: {set(antecedent)} -> {set(consequent)}")
            print("Confidence:", confidence)
            print("-" * 75)
            ruleCounter += 1
        bruteForceEndTime = time.time()

        apriori_time = AprioriAlgorithmImpl.association_rules_using_apriori(nikeDatabase, (minSupport / 100),
                                                                            (minConfidence / 100))
        fpgrowth_time = FpgrowthAlgorithmImpl.association_rules_using_fpgrowth(nikeDatabase, (minSupport / 100),
                                                                               (minConfidence / 100))

        print("\n Total execution time of Brute Force algorithm is " + str(
            round(bruteForceEndTime - bruteForceStartTime, 4)) + " seconds.")
        print("\n Total execution time of Apriori algorithm is " + str(
            round(apriori_time, 4)) + " seconds.")

        print("\n Total execution time of FP-growth algorithm is " + str(
            round(fpgrowth_time, 4)) + " seconds.\n")

    else:
        print("\nPlease select a valid database, from 1 to 5 mentioned below.\n")
        getDatabaseChoice()


def getMinimumSupport():
    print("\nPlease enter minimum support in % (value from 1 to 100): \n")
    minimumSupport = input()
    minSupport = int(minimumSupport)
    if 0 < minSupport < 100:
        return minSupport
    else:
        return getMinimumSupport()


def getMinimumConfidence():
    print("\nPlease enter minimum Confidence in % (value from 1 to 100): \n")
    minimumConfidence = input()
    minConfidence = int(minimumConfidence)
    if 0 < minConfidence < 100:
        return minConfidence
    else:
        return getMinimumConfidence()


def generate_candidates(prev_itemsets, k):
    candidates = []
    n = len(prev_itemsets)
    for i in range(n):
        for j in range(i + 1, n):
            itemset1 = prev_itemsets[i]
            itemset2 = prev_itemsets[j]
            if itemset1[:-1] == itemset2[:-1]:
                candidate = tuple(sorted(set(itemset1) | set(itemset2)))
                if len(candidate) == k:
                    candidates.append(candidate)
    return candidates


def generate_frequent_itemsets(transactions, min_support):
    items = {}
    for transaction in transactions:
        for item in transaction:
            if item in items:
                items[item] += 1
            else:
                items[item] = 1

    frequent_itemsets = []
    n = len(transactions)
    for item, count in items.items():
        support = count / n
        if support >= min_support:
            frequent_itemsets.append(([item], support))

    k = 2
    while True:
        candidates = generate_candidates([itemset[0] for itemset in frequent_itemsets], k)
        if not candidates:
            break

        frequent_candidates = []
        for candidate in candidates:
            count = 0
            for transaction in transactions:
                if set(candidate).issubset(set(transaction)):
                    count += 1
            support = count / n
            if support >= min_support:
                frequent_candidates.append((list(candidate), support))

        frequent_itemsets.extend(frequent_candidates)
        k += 1

    return frequent_itemsets


def generate_association_rules(frequent_itemsets, min_confidence):
    rules = []
    for itemset, support in frequent_itemsets:
        if len(itemset) >= 1:
            for i in range(1, len(itemset)):
                antecedent = itemset[:i]
                consequent = itemset[i:]
                antecedent_support = calculate_support(antecedent, frequent_itemsets)
                if antecedent_support > 0:
                    confidence = support / antecedent_support
                    if confidence >= min_confidence:
                        rules.append((antecedent, consequent, confidence,antecedent_support))
    return rules


# def calculate_support(itemset, frequent_itemsets):
#     for items, support in frequent_itemsets:
#         if all(item in items for item in itemset):
#             return support
#     return 0


def calculate_support(itemset, frequent_itemsets):
    for items, support in frequent_itemsets:
        if all(item in items for item in itemset):
            return support
    return 0


print("Which dataset would you like to use Zeal?\n")
getDatabaseChoice()
