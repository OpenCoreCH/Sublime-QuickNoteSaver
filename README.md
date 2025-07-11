# Quick Note Saver for Sublime Text

A simple but powerful Sublime Text plugin to instantly save an unsaved buffer (a new, untitled file) as a timestamped note. It optionally prompts for a title to create more descriptive filenames.

## Features

- **Instant Capture:** Save your fleeting thoughts and code snippets without the friction of the "Save As..." dialog.
- **Timestamped Filenames:** Automatically names files with a `YYYY-MM-DD_HH-MM-SS` format for easy sorting and reference.
- **Optional Titles:** Prompts for an optional title, which gets appended to the filename (e.g., `2025-07-11_10-53-01_My-API-Idea.txt`).
- **Configurable:** Easily set your desired notes directory in a settings file.
- **Seamless Workflow:** After saving, the temporary tab is closed and the new note file is opened automatically.

## Installation

### Manual Installation (Recommended)

This is the easiest way to install while the plugin is not on Package Control.

1.  Open Sublime Text and go to `Preferences` > `Browse Packages...`. This will open your `Packages` directory.
2.  Clone this repository into the `Packages` directory:
    ```sh
    git clone [https://github.com/YOUR_USERNAME/QuickNoteSaver.git](https://github.com/YOUR_USERNAME/QuickNoteSaver.git)
    ```
3.  Restart Sublime Text.

## Configuration

Before using the plugin, you must specify where your notes should be saved.

1.  In Sublime Text, go to `Preferences` > `Package Settings` > `QuickNoteSaver` > `Settings`.
2.  This will open the `QuickNoteSaver.sublime-settings` file.
3.  Change the `notes_location` to your desired path. You can use `~` to refer to your home directory.

    ```json
    {
      // Example for macOS/Linux:
      "notes_location": "~/Documents/SublimeNotes",

      // Example for Windows:
      // "notes_location": "C:/Users/YourUser/Documents/MyNotes"
    }
    ```

## Usage

1.  Open a new tab in Sublime Text (`CMD+N` or `CTRL+N`).
2.  Type or paste your note content.
3.  Press the shortcut `CMD+SHIFT+S` (macOS) or `CTRL+SHIFT+S` (Windows/Linux).
4.  An input panel will appear at the bottom asking for an optional title.
    - Type a title and press `Enter`.
    - Or, leave it blank and press `Enter` to use only the timestamp.
5.  Your note will be saved to your configured directory, and the new file will open.

## Default Keybinding

The default keybinding is `super+shift+s`.

-   macOS: `CMD + SHIFT + S`
-   Windows/Linux: `CTRL + SHIFT + S`

You can change this by going to `Preferences` > `Key Bindings` and adding an override.
