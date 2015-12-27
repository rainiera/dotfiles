import sys
import time
import os
os.getcwd()
os.chdir("/Users/rainierababao/cs/rainier/content/")
words = [arg for arg in sys.argv[1:]]
with open("{}.md".format(('-').join(words)), "w") as beak:
    beak.write("Title: {}\n".format((' ').join(words)))
    beak.write("Date: {}\n".format(time.strftime("%Y-%m-%d")))
    beak.write("Category: General\n\n")
    beak.write("#### Also a terrible attempt at writing a quine\n\n")
    beak.write("Automates writing test content with correct metadata for Pelican. This is the partial code for it, which can also be found [here](https://github.com/rainiera/dotfiles/blob/master/scripts/write_more.py):\n\n")
    beak.write("""
```
import sys
import time
import os
os.getcwd()
os.chdir("/Users/rainierababao/cs/rainier/content/")
words = [arg for arg in sys.argv[1:]]
with open("{}.md".format(('-').join(words)), "w") as beak:
    beak.write("Title: {}\\n".format((' ').join(words)))
    beak.write("Date: {}\\n".format(time.strftime("%Y-%m-%d")))
    beak.write("Category: General\\n\\n")
    beak.write("#### Also a terrible attempt at writing a quine\\n\\n")
    # ...turtles all the way down :)
```
""")
