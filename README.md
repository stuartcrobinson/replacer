# replacer
script and workflow and instructions for LLM to be able to generate multi-line WRITE and search/replace edits for files on file system.  janky temp solution


# how it works 

your project needs a `replacer/replacer_input.txt` file. this is where you'll dump responses from the LLM.  `replacer` will parse out and implement the embedded edit instructions.

it also generates `replacer/replacer_history.log` that you'll prob want to add to `.gitignore`

# how i use it

in a node project i'm working on, i add this to my project to download the entire `replacer/` dir into my project when i `npm install`, and then run 

```
<repo> $ python replacer/replacer.py
```

and this will watch `replacer/replacer_input.txt` for `replacer` commands.

# example 

here's actual toy demo from an LLM:

```markdown
I'll add a config file and update your route to use it. This will make your settings easier to manage.

<<<EXPLANATION>>>
Creating a centralized config file for API settings
<<<FILE>>>
src/config.json
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
src/routes/api.js
<<<SEARCH>>>
const timeout = 3000;
<<<REPLACE>>>
const { timeout } = require('../config.json');
<<<END>>>

That's it! Paste into `scripts/replacer_input.txt` and run `python replacer/replacer.py`.
```