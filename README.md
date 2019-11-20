# quick-drupal

## Install

Simply create the following Bash aliases to invoke the script from anywhere.

```
alias quick-start='path/to/quick-drupal.sh quick-start'
alias quick-restart='path/to/quick-drupal.sh quick-restart'
alias quick-clean='path/to/quick-drupal.sh quick-clean'
```

Do not forget to enable those changes immediately, so you can avoid to logout or reboot.

```
source ~/.bash_aliases
```

## Usage

```
quick-start [standard|minimal|umami] <patch>
quick-clean
```

Note: we require the use of `sudo` for the `quick-clean` command.

## Demo

[![quick-drupal demo](https://asciinema.org/a/275245.png)](https://asciinema.org/a/275245)
