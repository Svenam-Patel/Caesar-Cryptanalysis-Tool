# Caesar-Cryptanalysis-Tool
#### What this project does
This project automatically decrypts a Caesar cipher without needing the key by using *Chi-Square statistical frequency analysis*. It compares the ciphertext’s letter patterns with real English frequencies to identify the most likely plaintext.
#### Why this project is different
Instead of brute-forcing and making the user choose, it uses a *statistical scoring method* to evaluate all shifts and automatically pick the best one. This makes it behave like real cryptanalysis rather than a basic Caesar cipher script.
#### What problem it solves
In real situations, encrypted text arrives with no key. This tool shows how classical ciphers can still be broken using *frequency analysis*, a foundational method in cybersecurity.
#### How it works
- Tests all 26 shifts  
- Calculates *Chi-Square scores* for each shift  
- Selects the *closest statistical match* to English  
- Warns when text is *too short for reliable analysis* and prints the full table for *manual verification* 
