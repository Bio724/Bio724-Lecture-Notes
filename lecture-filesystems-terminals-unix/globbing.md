
## Wildcards and globbing

Most shells allow you to find or manipulate files whose names match a specified pattern.  These patterns are usually referred to as "wildcards" and the process of matching with wildcards is colloquially known as "globbing".

### Wildcard patterns

* `?` -- a question mark matches any single character
  * e.g. `ls pic?.jpg` -- lists files like `pic1.jpg`, `picA.jpg`, `pick.jpg`, etc.
* `*` -- an asterisk matches any number of characters
  * e.g. `ls *.jpg` -- lists all files whose names end in `.jpg`
  * e.g. `rm *junk*` -- removes all files whose names  contain `junk` as a substring; be very careful with globbing when removing files!
* `[...]` -- square brackets matches any one of the enclosed characters
  * e.g. `ls b[lr]*.jpg` -- lists all files whose name starts with `b` and whose second letter is either `l` or `r` and which end in `.jpg`. For example `blood.jpg`, `break.jpg`, but *not* `beak.jpg`

