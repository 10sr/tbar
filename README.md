tbar
====

Visualize values with ascii characters in terminal.


Synopsis and Options
--------

    tbar [-h] [-m MAX] [-l LENGTH] [-v] [<options_for_reader>] [filename]
    
    options_for_reader should be:
        -re, --regexp REGEXP
            Python regular expression for each line.
            Must contain symbolic group of "key" and "value".

If a filename is given, data are read from that file, otherwise from stdin.



Usage Example
-------------

When the content of `sample/a.txt` is like:

    # sample data
    a 80
    bcdef 40
    ghi 20
    jk 90

then the command

    ./bin/tbar sample/a.txt

will print bars as:

        a|********************************************      |
    bcdef|**********************                            |
      ghi|***********                                       |
       jk|**************************************************|

Regular expressions can be used for more compilcated format:

    $ bin/tbar --regexp '^(?P<key>[^ ]*) (?P<value>[^ ]*)' sample/a.txt
        a|********************************************      |
    bcdef|**********************                            |
      ghi|***********                                       |
       jk|**************************************************|

When specifying the option `--vertical`, tbar prints bars vertically:

    $ ./bin/tbar --vertical --length 10 sample/a.txt
    ----
       *
       *
    *  *
    *  *
    *  *
    *  *
    ** *
    ** *
    ****
    ****
    ----
    abgj
     chk
     di
     e
     f
