# Working implementation of this 3rd patch for undetect_chromedriver (single python file)

Here is the latest version of flaresolverr with this fix implemented: 
https://github.com/Dexcelerate/FlareSolverr-udetect-patch/ 

Note: I haven't tested running it through a new docker image / container, but it should work just fine. I'll include a systemd service implementation for those that want to run it standalone.

Original issue that started several weeks ago:
https://github.com/FlareSolverr/FlareSolverr/issues/811

Still waiting on this (seemingly) more robust method to be implemented & released:
https://github.com/ultrafunkamsterdam/undetected-chromedriver/discussions/1420

I also put together a small browser extension that can run in Chrome or Firefox that worked well enough to get me through the periods where CF was winning. Will probably be useful for if/when there are no known solutions like right now:
https://github.com/digitalnomad91/cloudflare-bypass-extension=

Note: Don't forget to pip3 install the packages imported below & then you can run python3 fuck_cloudflare.py and check if it is working.
