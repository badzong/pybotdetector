botdetector
===========

Small python2 module to reliably detect web spiders using reverse DNS lookups
for data harvesting protection.


Spiders supported:

  * Googlebot (googlebot.com)
  * bingbot (search.msn.com)


Adding a new bot is very easy, just append the domain to the bots list of the
BotDetector instance.


Install
-------

    python setup.py install


Example
-------

```python
>>> from botdetector import BotDetector
>>> bd = BotDetector()
>>> bd.bot('66.249.66.43')
'googlebot.com'
>>> bd.bot('207.46.204.229')
'search.msn.com'
>>> bd.bot('1.2.3.4')
>>>
```
