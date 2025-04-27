import json

# Input and output file paths
INPUT_FILE = "demo_log.json"  # Replace with your JSON file
OUTPUT_FILE = "demo_log_formatted.json"  # The formatted output file

def format_json(input_file, output_file):
    try:
        # Load the JSON file
        with open(input_file, "r") as f:
            data = json.load(f)

        # Save the formatted JSON to a new file
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Formatted JSON saved to {output_file}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    format_json(INPUT_FILE, OUTPUT_FILE)