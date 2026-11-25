import os


def process_file(input_filename):
    """Processes a single file and returns the formatted report string."""
    report = []

    # Check if file exists
    if not os.path.exists(input_filename):
        return f"Error: File '{input_filename}' not found."

    items = []
    with open(input_filename, "r") as file:
        for line in file:
            cleaned = line.strip().lower()
            if cleaned != "":
                items.append(cleaned)

    # Test Case 3: Empty file check
    if len(items) == 0:
        return "No data found: The file is empty. Please enter valid data."

    # Count frequencies
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1

    total_items = len(items)
    unique_items = len(counts)

    # Filter duplicates
    duplicates = {item: c for item, c in counts.items() if c > 1}

    # Format report
    report.append(f"Total items: {total_items}")
    report.append(f"Unique items: {unique_items}")

    if duplicates:
        for item, count in duplicates.items():
            report.append(f"Duplicate item: {item} ({count} occurrences)")
    else:
        report.append("No duplicate items found.")

    return "\n".join(report)


def main():
    test_cases = [
        ("Test Case 1 (Standard Duplicates)", "input1.txt"),
        ("Test Case 2 (No Duplicates)", "input2.txt"),
        ("Test Case 3 (Empty File)", "input3.txt"),
        ("Test Case 4 (Mixed Case & Whitespace)", "input4.txt"),
    ]

    all_outputs = []

    for case_name, filename in test_cases:
        separator = "=" * 45
        header = f"\n{separator}\n>>> {case_name} ({filename})\n{separator}"
        result = process_file(filename)

        all_outputs.append(header)
        all_outputs.append(result)

    full_report = "\n".join(all_outputs)

    # 1. Print all test results in terminal at once
    print(full_report)

    # 2. Save entire multi-case run into output.txt
    with open("output.txt", "w") as out:
        out.write(full_report + "\n")

    print("\n" + "=" * 45)
    print("[✓] All test cases executed and saved to output.txt")
    print("=" * 45)


if __name__ == "__main__":
    main()