# isitvalid365

Just another o365 email validator tool with throttling functionality built in. I've noticed that Microsoft will return false positives and negatives when rapid consecutive queries are executed. This tool gives you the option to take the low and slow approach to email validation. I recommend combining this with something like `fireprox` (https://github.com/ustayready/fireprox) for additional traffic obfuscation. 

## Usage
`usage: isitvalid365.py [-h] email_file output_file throttle jiggle`


![2025-01-28_14-23-11](https://github.com/user-attachments/assets/4fab567b-b105-4fdb-902d-38a72ace62dc)
