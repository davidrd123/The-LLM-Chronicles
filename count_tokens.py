#!/usr/bin/env python3
import sys
import tiktoken
import argparse

def count_tokens(text, model="gpt-4"):
    """Count tokens in text using the specified model's tokenizer."""
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
    return len(tokens)

def main():
    parser = argparse.ArgumentParser(description='Count tokens using tiktoken')
    parser.add_argument('--model', '-m', default='gpt-4', 
                        help='Model to use for tokenization (default: gpt-4)')
    parser.add_argument('files', nargs='*', help='Files to process (default: stdin)')
    args = parser.parse_args()
    
    # Process stdin if no files provided
    if not args.files:
        text = sys.stdin.read()
        token_count = count_tokens(text, args.model)
        print(f"Token count: {token_count}")
        return
    
    # Process each file
    total_tokens = 0
    for file in args.files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
                tokens = count_tokens(text, args.model)
                total_tokens += tokens
                print(f"{file}: {tokens} tokens")
        except Exception as e:
            print(f"Error processing {file}: {e}", file=sys.stderr)
    
    if len(args.files) > 1:
        print(f"Total tokens: {total_tokens}")

if __name__ == "__main__":
    main()