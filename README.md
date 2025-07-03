tool to implement file edit instructions on computer from LLM 

# quickstart 

1. clone this repo or add this postinstall step to `packagejson` and run `npm install` again

`package.json`
```json

  ...  
  "scripts": {
    ...
    "postinstall": "npx degit stuartcrobinson/replacer/replacer replacer",
    ...
  }
  ...
```

2. run the startup demo

```
python3 replacer/demo_replacer.py
```

3.  run replacer 

```
python3 replacer/replacer.py
```

4.  copy/paste the demo `replacer` commands from `demo_replacer_input.md` into `replacer_input.md` and hopefully your files get updated and some results get added the the top of your `replacer_input.md` like:





# replacer
script and workflow and instructions for LLM to be able to generate multi-line OVERWRITE and SEARCH/REPLACE edits for files on file system. 


# how it works 

your project needs a `replacer/replacer_input.md` file. this is where you'll dump responses from the LLM.  `replacer` will parse out and implement the embedded edit instructions.

it also generates `replacer/replacer_history.log` that you'll prob want to add to `.gitignore`

# how i use it

in a node project i'm working on, i add this to my project to download the entire `replacer/` dir into my project when i `npm install`:

{
  "name": "your-project",
  "version": "1.0.0",
  "scripts": {
    "postinstall": "npm run download-replacer-folder",
    "download-folder": "npx degit stuartcrobinson/replacer/replacer replacer",
  }
}


and then run 

```
<repo> $ python replacer/replacer.py
```

and this will watch `replacer/replacer_input.md` for `replacer` commands.

# example 

here's actual toy demo from an LLM:

```markdown
I'll add a config file and update your route to use it. This will make your settings easier to manage.

<<<EXPLANATION>>>
Creating a centralized config file for API settings
<<<FILE>>>
replacer_demo_src/config.json
<<<OVERWRITE>>>
{
  "apiVersion": "v1",
  "timeout": 5000
}
<<<END>>>

Now let's update the hardcoded value to pull from config instead:

<<<EXPLANATION>>>
Using config file instead of hardcoded timeout value
<<<FILE>>>
replacer_demo_src/routes/api.js
<<<SEARCH>>>
const timeout = 3000;
<<<REPLACE>>>
const { timeout } = require('../config.json');
<<<END>>>

That's it! Paste into `scripts/replacer_input.md` and run `python replacer/replacer.py`.
```

# todo

need to clean up `replacer/replacer_llm_instructions.md`

# ⚠️ warning ⚠️ NOT FOR PRODUCTION

this is all kinda janky.  i've been using a lot but no promises.  sometimes it leaves `replacer` syntax in important files.  dumb name.  hobby use only. 

i just made this repo to formalize stuff for myself instead of lugging conflicting files & scripts back and forth

🚨 NO SECURITY
🚨 NO SANDBOXING
🚨 NO SAFEGUARDS