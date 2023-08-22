# WINC CI - CD Assignment

For this assignment I wrote a short website in which I tried to explain as completely as possible what steps I took to arrive at my solution.
This will cover GitHub Actions, Bash to Digital Ocean and SSH.

I made a calculation page and the calculation functions are tested before the workflow will give the server the command to pull the repo.
A third, very unnessary step, will always be executed, just to show how it can be done.

- I've had quite a bit of trouble connecting with github. Because I wanted to know how it works, I did not use third party software such as Appleboy.
- Instead of making a .sh file server site, I chained commands in the workflow to change workdirectory and pull the repository.
- Also I had problems importing the functions in static/python/calculations.py
  This is the location where the calculation-functions are. From Test/test.calcs.py I could not import those calculation functions.
  As a solution I imported `sys` in the test file then a `sys.path.append("..")`
  Then I could run the tests by calling python -m pytest

I have linked the server to a domain so that you can easily access the website.

### www.eastrend.nl

Fore this one I didn't bother to see if I could find a lets-encrypt certificate for the server. The website therefore seems unsafe, but no private data is requested.
