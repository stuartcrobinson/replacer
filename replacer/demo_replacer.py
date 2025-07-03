#!/usr/bin/env python3
"""
Setup script to create demo files for testing replacer.
Run this first, then paste the example into replacer/replacer_input.md
"""

import os

def create_demo_files():
   # Create directory structure
   dirs = [
       'src',
       'src/routes',
       'scripts'
   ]
   
   for dir_path in dirs:
       os.makedirs(dir_path, exist_ok=True)
   
   # Create the initial api.js file with hardcoded timeout
   api_content = """const express = require('express');
const router = express.Router();

const timeout = 3000;

router.get('/status', (req, res) => {
   setTimeout(() => {
       res.json({ status: 'ok', timeout });
   }, 100);
});

module.exports = router;
"""
   
   with open('src/routes/api.js', 'w') as f:
       f.write(api_content)
   
   # Create empty replacer_input.md
   open('scripts/replacer_input.md', 'w').close()
   
   print("✓ Demo files created:")
   print("  - src/routes/api.js (with hardcoded timeout)")
   print("  - scripts/replacer_input.md (empty)")
   print("\nNow paste the example into scripts/replacer_input.md and run replacer!")

if __name__ == "__main__":
   create_demo_files()