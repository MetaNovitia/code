# Online Judge CLI

Check your solutions to online judges (e.g. HackerRank) from your CLI! Uses a headless Firefox browser to submit code. Downloads problem file and sample inputs/outputs when you make a new directory. You can also check against sample inputs locally.

## Requirements
Currently being developed on MacOS 10.15.3

- [Python 3](https://www.python.org/downloads/) (with pip3)

For Submitting from CLI:

- [Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Firefox Gecko Driver](https://github.com/mozilla/geckodriver/releases) (needs to be in $PATH)
- Selenium (install in setup)

Optional (for compiling cpp solutions):

- gcc (needed [XCode CLI](https://developer.apple.com/download/more/) on MacOS) 
- Windows: [Cygwin](https://preshing.com/20141108/how-to-install-the-latest-gcc-on-windows/) (includes gcc)


## Procedure

Jump to [setup](#setup) if requirements are fulfilled.

### Fulfilling Requirements:
This program assumes that __python3__ and __pip3__ are the commands to run Python 3 and Pip 3. To fix paths, use alias on MacOS, or edit PATH variable. To check if they're from the same package and has the correct versions:

```
$ pip3 -V
$ python3
>> import sys
>> sys.executable
>> quit()
```

The Firefox __geckodriver__ will have to be in the PATH variable for the program to find it. This can be achieved by either adding the path to the directory where the geckodriver is, or moving geckodriver to one of the paths (e.g. /usr/local/bin).

Installing Cygwin on [Windows](https://preshing.com/20141108/how-to-install-the-latest-gcc-on-windows/) may allow UNIX type commands on the Command Prompt, and also install gcc.

The clang compiler on MacOS does not have bits/stdc++.h header. __XCode CLI__ is needed to install __gcc__ on MacOS. After installing XCode CLI, install gcc using Homebrew:

```
$ brew install gcc
```
Or if there are still errors with header files, do:
```
$ brew upgrade gcc
```

### <a id="setup">Setup</a>:
```shell
$ pip3 install selenium
```

### Run:
Inside the root folder of this directory:
```shell
$ python3 run.py
```
or give permissions to script and run without including python3 in the future:
```shell
$ chmod 755 run.py
$ ./run.py
```

## Commands:
```
- new [link]            : create new directory with problem pdf and sample i/o (ignored by git)
- open [link]           : open directory associated with link
- vim [ext?]            : open code.[ext] in vim
- view [ftype?]	        : view a file (from pdf reader or readonly vim)
- login                 : logs in to current domain
- save [ext?] [fname?]  : saves to solutions folder (default fname=time())
- clear                 : clear work-folder code and copy templates
- rm                    : remove file from directory (choose in next prompt)
- post [ext?]           : post solution online (headless) and return feedback
- check	[ext?]          : check solution against sample input and output (diff)
- run [ext?]            : run solution using sample input (no diff)
- help                  : print possible commands
```

## Command Arguments 
```
- link                  : link of problem
- ext                   : solution file extension [py, cpp] (default: py)
- fname                 : file name to save to (default: current time)
- ftype                 : choice of file type to choose (pdf, i, o, sol)
```
