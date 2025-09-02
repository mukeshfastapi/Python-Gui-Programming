# Process a list of data with using match case

def process_data(data):

    match data:
        case [x, y]:
            print(f"list of two item {x} {y}")
        case [x, y, z]:
            print(f"List of Three Items {x},{y},{z}")

        case _:
            print('Unknown format!!')


process_data([20, 10])

process_data([20, 10, 40])
process_data(10)