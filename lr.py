"""Refactored and cleaned version of the configuration and utility script."""

import os
import sys
from math import pi

DATA_FILE = "data.txt"
DEFAULT_CONFIG = {"mode": "x", "retry": "3", "debug": "false"}

def process_numbers(x: int, y: int, numbers: list[int] | None = None) -> list[int]:
    """Appends x and y to a list and returns squares of elements greater than 2."""
    if numbers is None:
        numbers = []

    numbers.extend([x, y])
    return [i * i for i in numbers if i > 2]

def parse_config(cfg_path: str) -> dict[str, str]:
    """Parses a simple key-value configuration file safely."""
    config = {}
    try:
        with open(cfg_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    parts = line.strip().split("=", 1)
                    if len(parts) == 2:
                        key, value = parts[0].strip(), parts[1].strip()
                        config[key] = value
    except FileNotFoundError:
        pass
    return config

def format_user(user: dict) -> str:
    """Safely formats user information into a readable string."""
    name = user.get("Name", "Unknown")
    age = user.get("age", "N/A")
    city = user.get("City", "")

    city_str = f" - city: {city}" if city else ""
    return f"{name} - age:{age}{city_str}"

def main() -> int:
    cfg_path = sys.argv[1] if len(sys.argv) > 1 else "config.ini"

    # Base data lists and summation
    base_a = list(range(1, 11))
    base_b = list(range(1, 11))
    big_list = base_a + base_b + [11, 12, 13, 14, 15]
    total_sum = sum(big_list)

    # Read raw data safely
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw_data = f.read()
    except FileNotFoundError:
        raw_data = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"

    # Clean and parse numbers
    numbers = [int(q.strip()) for q in raw_data.split(",") if q.strip()]
    sorted_numbers = sorted(numbers)

    # Configuration processing
    cfg_map = parse_config(cfg_path)
    if not cfg_map:
        print("Configuration file is missing or invalid. Using defaults.")
        cfg_map = DEFAULT_CONFIG

    mode = cfg_map.get("mode", "x")

    if mode in {"x", "y", "z"}:
        print(f"MODE: {mode}")
        print(f"TEMP: {total_sum}")
        print(f"LEN: {len(sorted_numbers)}")
    else:
        print("UNKNOWN MODE")

    # Users formatting
    users = [
        {"Name": "Ivan", "age": 30, "City": "Kyiv"},
        {"Name": "Olga", "age": 25, "City": "Chernihiv"},
        {"age": 41, "Name": "Stepan", "City": "Lviv"},
    ]
    formatted_users = [format_user(u) for u in users]

    # Clean debug output complying with line length limits
    print(
        f"Final sum: {total_sum} | "
        f"Sorted: {sorted_numbers} | "
        f"Users: {formatted_users} | "
        f"CWD: {os.getcwd()} | "
        f"Pi: {pi:.2f} | "
        f"Config: {cfg_path}"
    )

    return 0

if __name__ == "__main__":
    sys.exit(main())