# palindrome_checker.py
"""Check if input is palindrome (ignores spaces, punctuation, case)."""
import argparse
import re

def normalize(s: str) -> str:
    return re.sub(r'[^A-Za-z0-9]', '', s).casefold()

def is_palindrome(s: str) -> bool:
    n = normalize(s)
    return n == n[::-1]

def main():
    parser = argparse.ArgumentParser(description="Palindrome checker")
    parser.add_argument("text", help="Text to check")
    args = parser.parse_args()
    if is_palindrome(args.text):
        print("Yes — it's a palindrome.")
    else:
        print("No — not a palindrome.")

if __name__ == "__main__":
    main()
