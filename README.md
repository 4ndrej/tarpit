# tarpit
various tarpits for fighting script kiddies back

## http

### ./http/tarpit.py
* python3 code stolen from https://nullprogram.com/blog/2019/03/22/
* more info at https://news.ycombinator.com/item?id=19465967
* run as

    ./tarpit.py

* how it works
  * listen on http://127.0.0.1:1984/
  * sends random X-header lines every 5 seconds until client hangs
