Irregular
==============

A domain-specific language mimicing Lua's regular expression functionality but implemented with Pythonic coroutines and generators.

**Please refer to the wiki for more Irregular documentation.**

Irregular features an abstract syntax tree parser and an interperter that implements the regular expression backtracking algorithim.

This project allows us to explore the various differences between Lua and Python coroutines, yielding, stack frames, and tail call optimizations. As such, this project is also a great self-teaching experience for these same concepts. Most practically, it's a demonstration of the benefits and use-cases of Python's famous generator idioms. This project also allows us to translate the rather clean backtracking algorithim featured in the Lua documentation into Python-based subsystems. The Lua documentation can be found here: http://www.inf.puc-rio.br/~roberto/docs/MCC15-04.pdf.

.


