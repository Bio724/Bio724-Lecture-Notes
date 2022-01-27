
# Visual Studio Code Tips

## Extensions

* Install language specific extensions as needed to get better autocompletion, syntax highlighting, etc. For this class the following extensions are either required or nice to have:

  * [Remote Development Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) -- Must have for working remotely on your linux VM.  We reviewed how to install and configure this extension in the first lecture.

  * [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) -- colors columns of CSV and TSV files to make it easy to see how fields line up w/out having to open a spreadsheet program

  * [Markdown All In One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) -- you'll be writing a lot of Markdown over the course of the semester  when working on HW assignments. This extension provides nice shortcuts, syntax highlighting, and previews.

  * [Awk](https://marketplace.visualstudio.com/items?itemName=luggage66.AWK) -- provide syntax highlighting for Awk programming. I've noticed a few error in the syntax coloring but I still find it useful.


## Configuration of the integrade terminal in VS Code

* Set the terminal to use "xterm" when connecting to a Linux external -- In "Settings" ("⌘-," on Mac; "ctrl-," on Windows)  search for `terminal linux exec` in the search bar. In the field for `Terminal > External: Linux Exec` enter `xterm`.  When you connect to your VM via the VS Code integrated terminal this should give you coloring of terminal commands like grep(assuming you're using the default `.bashrc` settings that your VM came configured with)

* Turn on bright colors for bold text in the terminal -- In "Settings" ("⌘-," on Mac; "ctrl-," on Windows)  search for `terminal bold text` in the search bar. Click the check box next to the `Terminal > Integrated: Draw Bold Text in Bright Colors` setting.  This will give you brighter colors for bold text in the integrated terminal.

