def fractional_knapsack(items, capacity):
    # Calculate value per weight for each item
    for item in items:
        item['value_per_weight'] = item['value'] / item['weight']
    
    # Sort items by value per weight in descending order
    items.sort(key=lambda x: x['value_per_weight'], reverse=True)
    
    total_value = 0
    knapsack = []

    for item in items:
        if capacity >= item['weight']:
            # Take whole item
            knapsack.append({
                'item': item['item'],
                'fraction': 1.0
            })
            total_value += item['value']
            capacity -= item['weight']
        else:
            # Take fraction of item
            fraction = capacity / item['weight']
            knapsack.append({
                'item': item['item'],
                'fraction': fraction
            })
            total_value += item['value'] * fraction
            break

    return total_value, knapsack

def main():
    # Example items: [item, weight, value]
    items = [
        {'item': 'A', 'weight': 10, 'value': 60},
        {'item': 'B', 'weight': 20, 'value': 100},
        {'item': 'C', 'weight': 30, 'value': 120}
    ]
    
    capacity = 50
    
    max_value, selected_items = fractional_knapsack(items, capacity)
    
    print("Maximum value:", max_value)
    print("\nSelected items:")
    for item in selected_items:
        print(f"Item: {item['item']}, Fraction: {item['fraction']:.2f}")

if __name__ == "__main__":
    main()