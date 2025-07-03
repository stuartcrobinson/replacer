#!/usr/bin/env python3
"""
Setup script to create demo files for testing replacer.
Run this first, then paste the example (`replacer/demo_replacer_input.md`) into replacer/replacer_input.md
"""

import os

def create_demo_files():
   # Create directory structure
   dirs = [
       'replacer_demo_src',
       'replacer_demo_src/routes',
       'replacer'
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
   
   with open('replacer_demo_src/routes/api.js', 'w') as f:
       f.write(api_content)
   
   # Create replacer_input.md if needed
   path = 'replacer/replacer_input.md'
   if not os.path.exists(path):
      open(path, 'w').close()
   
   print("✓ Demo files created:")
   print("  - replacer_demo_src/routes/api.js (with hardcoded timeout)")
   print("  - replacer/replacer_input.md (empty)")
   print("\nNow run replacer/replacer.py and then paste the example from demo_replacer_input.md into replacer_input.md")

if __name__ == "__main__":
   create_demo_files()