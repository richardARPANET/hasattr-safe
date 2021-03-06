**NOTICE**: If you're reading this on GitHub.com please be aware this is a mirror of the primary remote located at https://code.richard.do/explore/projects.
Please direct issues and pull requests there.

# hasattr_safe
[![Build Status](https://travis-ci.org/richardasaurus/hasattr-safe.png?branch=master)](https://travis-ci.org/richardasaurus/hasattr-safe)

`hasattr()` in Python 2 hides all exceptions, `hasattr_safe()` does not, as is the behaviour in Python 3.

### Installation

```bash
pip install hasattr-safe
```

### Usage


```python
import hasattr_safe

cake_is_a_lie = hasattr_safe(TheCake, 'lies')
```

[https://docs.python.org/3/library/functions.html#hasattr](https://docs.python.org/3/library/functions.html#hasattr)

