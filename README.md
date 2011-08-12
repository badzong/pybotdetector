botdetector
===========

Small script to reliably detect web spiders. Currently supports

  * Googlebot
  * bingbot


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
