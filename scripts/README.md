# dotfiles

### write_more.py

Script to start off a blog post in Markdown with correct metadata for Pelican. See my [blog post](http://rainier.io/seeing-if-this-script-worked.html)

#### Usage:

1. `python write_more.py My Blog Post`

2. Add content to `blog/content/My-Blog-Post.md`. When you're done, `./fly-pelican`?

### fly-pelican

Script to update my personal website/blog.

#### Usage:

1. Create/update/delete pages in `blog/content/` with the appropriate metadata. Use `write_more.py`?

2. `./fly-pelican`

### ssh-utcs-machine

A simple script to log in to one of the UTCS public machines without having to type anything in.

#### Example Usage:

1. Change ```myUsername```, ```myPassword``` to the appropriate parameters.

2. Put the script in the default working directory of your favorite iTerm2 profile.

3. ```cd``` into where the script is in and type ```sudo chmod 777 ssh-utcs-machine```

4. In the "Command" section of the "General" pane of your profile preferences, enter ```expect ssh-utcs-machine```.

5. Whenever you open up an iTerm2 window with the profile you edited, it should automatically run this script and you should be ssh'd into a UTCS public machine without being prompted for your username or password!

#### Notes:

- Edited 6/23/15: Changed ```a-public-machine``` to ```linux``` because ```linux.cs.utexas.edu``` is apparently always aliased to a public Linux machine. (This can be changed if you have a favorite machine). Inserted the ```sudo chmod``` step to make the script executable because I forgot to mention that. Oops!

