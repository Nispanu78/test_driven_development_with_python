import contacts


class TestAddingEntries:
    def test_basic(self):
        app = contacts.Application()

        app.run("contacts add NAME 3345554433")

        assert app._contacts == [
            ("NAME", "3345554433")
        ]