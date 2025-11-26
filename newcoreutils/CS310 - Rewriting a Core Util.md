# Jax Jacobson
# 11/26/2025
# CS 310 - Rewriting a Core Util

# What command did you impliment?
I implimented the "whoami" core util. Usually this command just returns the user's name, but I wanted it to return the user's name, EUID, GID, and current path in a nice, readable format.

# What was a hurdle?
The biggest hurdle for me was trying to figure out how to get my version to be called instead of the default version when calling whoami in the terminal. I got around this by getting the path for the original whoami and putting my version before it, so Linux would read my version before the original and stop.

# What was easy? 
The easiest part was making a new version of the core util. That was only a few lines of code, and half of them were print lines.