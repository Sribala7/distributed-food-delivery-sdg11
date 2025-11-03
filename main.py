import os

def parse_orders(lines):
    orders = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(',')]
        if len(parts) != 4:
            # skip malformed lines
            continue
        order_id, customer, amount_str, item = parts
        try:
            amount = float(amount_str)
        except ValueError:
            continue
        orders.append({
            'order_id': order_id,
            'customer': customer,
            'amount': amount,
            'item': item,
        })
    return orders


def summarize(orders):
    total_orders = len(orders)
    total_amount = sum(o['amount'] for o in orders)
    by_item = {}
    for o in orders:
        by_item[o['item']] = by_item.get(o['item'], 0) + 1
    top_item = max(by_item.items(), key=lambda x: x[1])[0] if by_item else 'N/A'
    return total_orders, total_amount, top_item, by_item


def main():
    input_path = 'input.txt'
    output_path = 'output.txt'

    if not os.path.exists(input_path):
        raise FileNotFoundError(f'{input_path} not found')

    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    orders = parse_orders(lines)
    total_orders, total_amount, top_item, by_item = summarize(orders)

    with open(output_path, 'w', encoding='utf-8') as out:
        out.write('Distributed Food Delivery Report\n')
        out.write('--------------------------------\n')
        out.write(f'Total orders: {total_orders}\n')
        out.write(f'Total amount: {total_amount:.2f}\n')
        out.write(f'Most ordered item: {top_item}\n')
        out.write('\nOrders by item:\n')
        for item, count in sorted(by_item.items(), key=lambda x: (-x[1], x[0])):
            out.write(f'- {item}: {count}\n')

if __name__ == '__main__':
    main()
