def exercise1(tp, fp, fn):
    """calculate F1-score given tp, fp, fn"""
    dict_params = {"tp": tp, "fp": fp, "fn": fn}

    # Check if the input is an integer and greater than zero
    for param, value in dict_params.items(): # convert dict to list of tuples
        if not isinstance(value, int):
            print(f"{param} is not an integer")
            return
        if value < 0:
            print("tp, fp, fn must be greater than zero")
            return
    
    # Calculate F1-score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-score: {f1_score}")

exercise1(tp=2, fp=4, fn=5)