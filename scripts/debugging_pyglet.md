# Debugging pyglet mac os x high sierra

With a lot of help from this: https://bitbucket.org/pyglet/pyglet/issues/131/library-c-not-found

**Original error**

```python
In [1]: import gym
   ...: env = gym.make('CartPole-v0')
   ...: env.reset()
   ...: for _ in range(1000):
   ...:     env.render()
   ...:     env.step(env.action_space.sample()) # take a random action
   ...:
[2017-11-29 21:32:45,490] Making new env: CartPole-v0
---------------------------------------------------------------------------
ReraisedException                         Traceback (most recent call last)

.
.
.


ReraisedException: Error occured while running `from pyglet.gl import *`
The original exception was:

ImportError: Library "c" not found.

HINT: make sure you have OpenGL install. On Ubuntu, you can run 'apt-get install python-opengl'. If you're running on a server, you may need a virtual frame buffer; something like this should work: 'xvfb-run -s "-screen 0 1400x900x24" python <your_script.py>'
```

**Troubleshooting**

Can pyglet library loader find it?

```
from pyglet.lib import MachOLibraryLoader
loader = MachOLibraryLoader()
print(loader.find_library('c'))

None
```

No, so try loading it manually

```
import ctypes
libc = ctypes.CDLL('/usr/lib/libc.dylib')
print(libc)

Something happens!
```

So it's not an issue with the Python installation, must be a loader having issue
with an env variable

```
echo $DYLD_LIBRARY_PATH
echo $DYLD_FALLBACK_LIBRARY_PATH

Something something Anaconda that doesn't include `/usr/local/lib`
```

Add it to `.zshrc` now

```
export DYLD_FALLBACK_LIBRARY_PATH=/usr/lib:/Users/rainierababao/anaconda/lib/:
```

cartpole renders now.

