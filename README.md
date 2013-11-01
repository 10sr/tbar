tbar
====

Terminal bar.

Visualize values with `*`.


Synopsis
--------

    tbar [-h] [-m MAX] [-l LENGTH] [-v] [filename]

If a filename is given, data are read from that file, otherwise from stdin.



Input Format
------------

One line has a pair of name and value separated by whitespaces.
Any line starts with `#` are comments and ignored.



Usage Example
-------------

    $ ./bin/tbar sample/a.txt
        a|********************************************      |
    bcdef|**********************                            |
      ghi|***********                                       |
       jk|**************************************************|

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
