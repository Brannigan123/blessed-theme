# blessed-theme

Allows for defining a theming baseline across apps on console.

This works by reading theme configurations from `~/.config/theme/config.yml`
The configurations allows for defining color schemes, fonts, wallpaper and measures such as padding and margin sizes.

By using it as a library, other scripts can use it do get theming information defined in the aforementioned config.
Currently using it with a theme templating engine to generate consistent look and feel across apps, terminal emulators, launchers and window manager.
