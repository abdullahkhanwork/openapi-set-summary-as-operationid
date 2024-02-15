import yaml

def modify_operation_ids(openapi_file, output_file):
    try:
        with open(openapi_file, 'r') as f:
            openapi_data = yaml.safe_load(f)

        paths = openapi_data.get('paths', {})
        for path, operations in paths.items():
            for method, operation in operations.items():
                summary = operation.get('summary', '')
                new_id = "".join(summary.split())
                operation['operationId'] = new_id

        with open(output_file, 'w') as f:
            yaml.dump(openapi_data, f)

    except FileNotFoundError as e:
        raise ValueError(f"Input file not found: {e}")
    except PermissionError as e:
        raise ValueError(f"Permission error writing output file: {e}")

if __name__ == '__main__':
    filename = input("Enter file name: ")
    input_file = f"input/{filename}.yaml"
    output_file = f"output/{filename}.yaml"
    modify_operation_ids(input_file, output_file)
    print("Operation IDs modified and saved to", output_file)
