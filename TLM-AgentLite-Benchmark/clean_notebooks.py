#!/usr/bin/env python3
"""
Script to clean Jupyter notebooks by setting metadata to {} and execution_count to null
for all cells in all notebooks in the current directory.
"""

import json
import glob
import os
from pathlib import Path

def clean_notebook(notebook_path):
    """Clean a single notebook by setting metadata to {} and execution_count to null."""
    print(f"Processing: {notebook_path}")
    
    try:
        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Clean each cell
        for cell in notebook.get('cells', []):
            # Set metadata to {}
            cell['metadata'] = {}
            
            # Always set execution_count to null
            cell['execution_count'] = None
        
        # Clean notebook-level metadata
        notebook['metadata'] = {}
        
        # Write back the cleaned notebook
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        print(f"✓ Cleaned: {notebook_path}")
        
    except Exception as e:
        print(f"✗ Error processing {notebook_path}: {e}")

def main():
    """Main function to process all notebooks in the current directory."""
    # Find all .ipynb files in the current directory
    notebook_files = glob.glob("*.ipynb")
    
    if not notebook_files:
        print("No Jupyter notebooks found in the current directory.")
        return
    
    print(f"Found {len(notebook_files)} notebook(s):")
    for notebook in notebook_files:
        print(f"  - {notebook}")
    
    print("\nCleaning notebooks...")
    
    # Process each notebook
    for notebook_path in notebook_files:
        clean_notebook(notebook_path)
    
    print("\nAll notebooks have been cleaned!")

if __name__ == "__main__":
    main() 