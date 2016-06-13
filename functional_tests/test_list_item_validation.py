from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item.  She hist Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tires again with some text for the item, which now works

        # Perversely, she now decides to submit a swcond blank list tiem

        # She recieves a smiilar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')

# vim: set ai et sw=4 ts=4 sts=4
