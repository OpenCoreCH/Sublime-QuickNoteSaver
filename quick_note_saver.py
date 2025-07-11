import sublime
import sublime_plugin
import os
import re
from datetime import datetime

class SaveUnsavedNoteCommand(sublime_plugin.TextCommand):
    """
    This command saves the content of an unsaved view to a timestamped
    text file. It first prompts the user for an optional title, which
    is appended to the filename if provided.
    """
    def run(self, edit):
        if self.view.file_name() is not None:
            return

        settings = sublime.load_settings("QuickNoteSaver.sublime-settings")
        notes_dir = settings.get("notes_location")

        if not notes_dir:
            sublime.error_message(
                "QuickNoteSaver Plugin:\n\n"
                "'notes_location' is not configured. "
                "Please set it in QuickNoteSaver.sublime-settings."
            )
            return

        window = self.view.window()
        if window:
            window.show_input_panel(
                "Note Title (Optional, press Enter to skip):",
                "",
                lambda title: self.on_title_entered(title, notes_dir),
                None,
                None
            )

    def on_title_entered(self, title, notes_dir):
        sanitized_title = ""
        if title and title.strip():
            clean_title = title.strip().replace(' ', '_')
            sanitized_title = re.sub(r'(?u)[^-\w.]', '', clean_title)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        if sanitized_title:
            filename = f"{timestamp}_{sanitized_title}.txt"
        else:
            filename = f"{timestamp}.txt"
            
        full_path = os.path.join(os.path.expanduser(notes_dir), filename)

        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        content_region = sublime.Region(0, self.view.size())
        content = self.view.substr(content_region)

        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)

            window = self.view.window()
            self.view.set_scratch(True)
            self.view.close()
            if window:
                window.open_file(full_path)
            
            sublime.status_message(f"Note saved to: {os.path.basename(full_path)}")

        except Exception as e:
            sublime.error_message(f"QuickNoteSaver: Failed to save note.\n\nError: {e}")

    def is_enabled(self):
        return self.view.file_name() is None and not self.view.is_read_only()

    def is_visible(self):
        return self.is_enabled()
