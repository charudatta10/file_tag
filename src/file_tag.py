import os
import json

class FileTag:

    def __init__(self) -> None:
        self.file_tags = {}

    def load_file(self, tags_file='file_tags.json'):
        if os.path.exists(tags_file):
            with open(tags_file, 'r') as f:
                self.file_tags = json.load(f)

    def save_file(self, tags_file='file_tags.json'):
        with open(tags_file, 'w') as f:
            json.dump(self.file_tags, f, indent=4)

    def add_tags(self, file_path: str, tags) -> None:
        if isinstance(tags, str):
            tags = [tags]
        
        if file_path in self.file_tags:
            self.file_tags[file_path] = list(set(self.file_tags[file_path] + tags))
        else:
            self.file_tags[file_path] = tags

    def show_tags(self) -> None:
        for file_path, tags in self.file_tags.items():
            print(f"{file_path}: {', '.join(tags)}")

    def remove_tag(self, file_path: str, tag: str) -> None:
        if file_path in self.file_tags and tag in self.file_tags[file_path]:
            self.file_tags[file_path].remove(tag)
            if not self.file_tags[file_path]:
                del self.file_tags[file_path]

    def sort_tags(self):
        sorted_files = sorted(self.file_tags.items(), key=lambda item: item[1][0] if item[1] else '')
        for file_path, tags in sorted_files:
            print(f"{file_path}: {', '.join(tags)}")

if __name__ == "__main__":
    t = FileTag()
    t.load_file()
    t.add_tags("main.py", ["src", "python"])
    t.add_tags("archives.7z", "archive")
    t.sort_tags()
    t.show_tags()
    t.remove_tag("archives.7z", "archive")
    t.save_file()

