from rcmt.unittest import TaskTestCase, Repository, File

from rcmt_tasks.example import Example


class ExampleTest(TaskTestCase):
    def test_filter(self):
        """Test that filter() matches."""
        task = Example()

        self.assertTaskFilterMatches(
            task=task,
            repo=Repository(name="example.dev/local/test")
        )
        self.assertTaskFilterDoesNotMatch(
            task=task,
            repo=Repository(name="github.com/wndhydrnt/rcmt")
        )

    def test_apply(self):
        """Test that apply() modifies the content of example.txt"""
        repo_before = Repository(
            "example.dev/local/test",
            File(content="some content", path="example.txt")
        )
        repo_after = Repository(
            "example.dev/local/test",
            File(content="example\n", path="example.txt")
        )

        task = Example()

        self.assertTaskModifiesRepository(
            task=task, before=repo_before, after=repo_after
        )
