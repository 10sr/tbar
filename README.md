tbar
====

Visualize values with ascii characters in terminal.


Synopsis and Options
--------

    usage: tbar [-h] [-r REGEXP] [-c COMMENT] [-s SEP] [-f FIELD] [-m MAX]
                [-l LENGTH] [-v]
                [filename]
    
    Visualize values with ascii characters in terminal
    
    positional arguments:
      filename              filename for input. If omitted read from stdin
    
    optional arguments:
      -h, --help            show this help message and exit
      -r REGEXP, --regexp REGEXP
                            regular expression to extract key and value. When this
                            option is given, -s and -f options are ignored
      -c COMMENT_START, --comment COMMENT_START
                            string that leading commnent strings, defaults to "#"
      -s SEP, --sep SEP     separator of field
      -f NUM,NUM, --field NUM,NUM
                            numbers of field to use as key and value, default to
                            1,2
      -m MAX, --max MAX     value for max
      -l LENGTH, --length LENGTH
                            length of bars, defaults to 50
      -v, --vertical        print bars vertically



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

                                                            90.0
        a|********************************************      |
    bcdef|**********************                            |
      ghi|***********                                       |
       jk|**************************************************|

When specifying the option `--vertical`, tbar prints bars vertically:

    $ ./bin/tbar --vertical --length 10 sample/a.txt
    90.0----
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

Specifying Field to Show
------------------------

When extracting data from input line, there are two ways: cut-like options and
regular expression.
Using cut-like options is an easy way. For example, when input lines are

    # sample data
    a 80
    bcdef 40
    ghi 20
    jk 90

then you can use the first field as key (name) and the second as value by
specifying the options like

    --sep " " --field 1,2

(Actually this options are set by default so you do not need these options for
this simple case)
If you want to deal with rather complicated input, you can use regular
expression with symbolic groups instead. For example, specifying

    --regexp '^(?P<key>[^ ]*) *(?P<value>[^ ]*)'

means the same thing as previous example by cut-like options.
