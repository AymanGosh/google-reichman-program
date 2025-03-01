def ul(l):
    res=""
    for i in l:
        res = res+ "\t<li>"+i +"</li>\n"
    return "<ul>\n"+res+"</ul>\n"

assert ul(['item 1', 'item 2']) ==  '<ul>\n\t<li>item 1</li>\n\t<li>item 2</li>\n</ul>\n'
assert ul(['a', 'b', 'c']) ==  '<ul>\n\t<li>a</li>\n\t<li>b</li>\n\t<li>c</li>\n</ul>\n'