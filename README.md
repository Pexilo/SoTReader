<br />
<p align="center">
  <a href="https://github.com/Pexilo">
    <img src="https://i.imgur.com/n85oe6Q.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SoT Reader</h3>

  <p align="center">
	A tool for people looking to save time when writing down the lore of Sea of Thieves!<br />
    <strong>English 🥖 Français<br />Compatible</strong></a>
    <br />
    <br />
    <a href="https://github.com/Pexilo/SoTReader/issues">Report Bug</a>
    ·
    <a href="https://github.com/Pexilo/SoTReader/issues">Request Feature</a>
  </p>
</p>

## About SoT Reader

I noticed that many people documenting the lore of Sea of Thieves were writing the text in-game by hand, I created this script to allow you to automate this by taking only simple screenshots.

Important notes:
* The script uses the CPU to detect the text, speed may vary depending on your.
* Don't run the same images multiple times if you find mistakes! The results will be the same, just correct them by hand.
* What I've tested: this specific font doesn't work with the script (font used mainly on Larinna scrolls), <a href="https://i.imgur.com/hxr7BRB.jpeg">see this image</a>.
* All lore books and dialogues should work properly. Make sure your screenshots are clean, avoid island popups or player names.

There is an end of execution beep once the script has finished running, this allows you to do something else.

## Installation (user-friendly)

1. Download and install [https://aka.ms/vs/16/release/vc_redist.x64.exe](https://aka.ms/vs/16/release/vc_redist.x64.exe)
2. Download Python [https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe](https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe)
3. Make sure to select <strong>Add Python 3.9 to PATH</strong> then click Install Now.

![alt text](https://i.imgur.com/x3hQIqC.png)


4. When Python has finished installing, make sure to select <strong>Disable path length limit</strong>

![alt text](https://i.imgur.com/b1IyOK6.png)


5. Download and unzip the project in the folder of your choice

![alt text](https://i.imgur.com/Dybbhzu.png)

## Usage

<strong>Note:</strong> The simplest way is to double click on `main.py` file. 
However, if you have issues, use the `fix` option on the command line as shown below.

This script can be used easily in a shell.

1. Put the desired images in `/images` folder.
2. Press "shift + right click" where `main.py` folder is and open <strong>PowerShell</strong>,
* Here you can type:
```sh
python main.py
```
The script will install all necessary modules and run the script.

You can see the results in the console and in the `/results` folder.

* *If you have trouble with text detection you can try:*
```sh
python main.py fix
```

***
### First launch errors

1. Open Powershell in administrator mode
 
![alt text](https://i.imgur.com/sKmQ4is.png)

2. Copy the directory where SoTReader is located. Simply copy the path on your explorer

![alt text](https://i.imgur.com/iI00XDe.png)

3. Type in Powershell (*replace it with your path copied above*)
```sh
cd C:\Users\Pexi\Downloads\SoTReader-1.3
```

4. Then type to launch SoTReader
```sh
python main.py
```

Installation should be done without errors just wait a bit!
<br />Enjoy ! :)
