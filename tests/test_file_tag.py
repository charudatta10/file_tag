import unittest
from src.file_tag import FileTag  # Replace 'your_module' with the actual module name

class TestFileTag(unittest.TestCase):

    def setUp(self):
        self.file_tag = FileTag()
        self.file_tag.file_tags = {
            "example1.txt": ["important", "work"],
            "example2.txt": ["urgent", "personal"]
        }

    def test_add_tags(self):
        self.file_tag.add_tags("example3.txt", ["new", "test"])
        self.assertIn("example3.txt", self.file_tag.file_tags)
        self.assertListEqual(self.file_tag.file_tags["example3.txt"], ["new", "test"])

    def test_add_tags_existing_file(self):
        self.file_tag.add_tags("example1.txt", "extra")
        self.assertIn("extra", self.file_tag.file_tags["example1.txt"])

    def test_remove_tag(self):
        self.file_tag.remove_tag("example2.txt", "urgent")
        self.assertNotIn("urgent", self.file_tag.file_tags["example2.txt"])

    def test_remove_tag_last(self):
        self.file_tag.remove_tag("example2.txt", "urgent")
        self.file_tag.remove_tag("example2.txt", "personal")
        self.assertNotIn("example2.txt", self.file_tag.file_tags)

    def test_sort_tags(self):
        sorted_files = sorted(self.file_tag.file_tags.items(), key=lambda item: item[1][0] if item[1] else '')
        self.assertEqual(sorted_files[0][0], "example1.txt")

if __name__ == "__main__":
    unittest.main()
