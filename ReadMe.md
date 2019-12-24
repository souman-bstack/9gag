# 9Gag Crawler
This is a project to crawl 9gag websites hot category according to the specification mentioned here https://github.com/browserstack/tech-onboarding/blob/master/scraper/README.md

## Requirement/Installation
- OS X 10.13.5 or higher
- Python3 (version 3.6.8)
- pip3 (version 18.1)
- mongodb (version 3.6.16)

To prepare the code to execute run the following commands in your terminal
```
$ git clone git@github.com:souman-bstack/9gags.git
$ cd 9gags
$ pip install -r requirements.txt
```
### Setting up the cron for periodic crawling
- Get the path of python3 executable
```
$ which python3
```
- You will get an output like `/Library/Frameworks/Python.framework/Versions/3.6/bin/python3`
Let's say the output is *python3_path* and home directory path of the 9gags website is *9gags_home*

- Now add the cron in crontab
`$ crontab -e`

- Add the following line
`* * * * * cd 9gags_home && python3_path nine_gag.py scrap`

### Getting the results
- While in 9gags home directory. Run the command to get the output
#### Example
```
$ python3 nine_gag.py TEXT 4
```