# isitvalid365

Just another o365 email validator tool with throttling functionality built in. I've noticed that Microsoft will return false positives and negatives when rapid consecutive queries are executed. This tool gives you the option to take the low and slow approach to email validation. I recommend combining this with something like `fireprox` (https://github.com/ustayready/fireprox) for additional traffic obfuscation. 

## Usage
```
usage: isitvalid365.py [-h] email_file output_file throttle jiggle

Validate email addresses against Microsoft's API.

positional arguments:
  email_file   Path to the file containing email addresses.
  output_file  Path to save valid email addresses.
  throttle     Base throttling time in seconds (e.g., 0.5 for half a second).
  jiggle       Maximum jiggle time to vary the throttle (e.g., 0.2).

options:
  -h, --help   show this help message and exit
```



