# 0x17. Web stack debugging #3
> This repo contains a puppet manifest that fixes a bug in an apache2 config file this is the fourth of a web debugging series, where I was tasked to fix a bug in a LAMP stack project.

## Tasks :page_with_curl:
* **0. Strace is your friend**
  * [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp): Puppet manifest
  that fixes a typo error causing a WordPress application being served by an Apache
  web server to fail.
  * Usage: `puppet apply 0-strace_is_your_friend.pp`
