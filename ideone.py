from ideone import Ideone
import sys
if len(sys.argv) < 2:
    print '''[+] USAGE: python2 ideone.py  <language>

    [+]Languages:
         C++14
         Pascal
         Perl
         Python
         Fortran
         Whitespace
         Ada
         Ocaml
         Intercal
         Java
         C
         Brainf**k
         Assembler
         CLIPS
         Prolog
         Icon
         Ruby
         Pike
         Haskell
         Pascal
         Smalltalk
         Nice
         Lua
         C#
         Bash
         PHP
         Nemerle
         Common Lisp
         Scheme
         C99 strict
         JavaScript
         Erlang
         Tcl
         Scala
         SQL
         Objective-C
         Assembler
         Perl 6
         Java7
         Text
         VB.NET
         D
         AWK gawk-3.1.6
         AWK mawk-1.3.3
         COBOL 85
         Forth
         Prolog
         bc
         Clojure
         JavaScript
         Go
         Unlambda
         Python 3
         R
         COBOL
         Oz
         Groovy
         Nimrod
         Factor
         F#
         Falcon
    '''
    sys.exit(1)

lang  = sys.argv[1]
print "Paste: and CTRL+D to End the paste..."
paste = sys.stdin.read()
i = Ideone('awesomepaste', '9878783904')
res = i.create_submission(paste, lang)
link = res['link']
print "http://www.ideone.com/" + link
