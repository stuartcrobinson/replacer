*** paste content here containing any `replacer` command blocks ***


assuming replacer is running:

```
python replacer/replacer.py
```

# example input text containing some `replacer` command blocks:

```
I'll add a config file and update your route to use it. This will make your settings easier to manage.

<<<EXPLANATION>>>
Creating a centralized config file for API settings
<<<FILE>>>
replacer_demo_src/irrelevant/default/example/config.json
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
invalid/demo/path/to/file/routes/api.js
<<<SEARCH>>>
const timeout = 3000;
<<<REPLACE>>>
const { timeout } = require('../config.json');
<<<END>>>
```
