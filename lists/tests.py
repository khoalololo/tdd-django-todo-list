from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from lists.models import Item, List

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_renders_input_form(self):
        response = self.client.get("/")
        # The book will guide you on when to uncomment and change this action
        # self.assertContains(response, '<form method="POST">')
        self.assertContains(response, '<form method="POST" action="/lists/new">')
        self.assertContains(response, '<input name="item_text"')


class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        mylist=List()
        mylist.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = mylist # Assign the List object to the item's 'list' ForeignKey
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = mylist # Assign the same List object to the second item
        second_item.save()

        saved_list=List.objects.get() # Assumes only one list exists for simplicity here
        self.assertEqual(saved_list, mylist) # Check if the retrieved list is the same object

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        # CORRECTED LINES:
        # Assertions for the first item's text and its linked list object
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(first_saved_item.list, mylist) # Correct: Compare Item.list (List object) to mylist (List object)

        # Assertions for the second item's text and its linked list object
        self.assertEqual(second_saved_item.text, "Item the second")
        self.assertEqual(second_saved_item.list, mylist) # Correct: Compare Item.list (List object) to mylist (List object)

class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post("/lists/new", data={"item_text": "A new list item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.get()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_POST(self):
        response = self.client.post("/lists/new", data={"item_text": "A new list item"})
        self.assertRedirects(response, "/lists/the-only-list-in-the-world/")

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')
    def test_renders_input_form(self):
        response = self.client.get("/lists/the-only-list-in-the-world/")
        # The book will guide you on when to uncomment and change this action
        # self.assertContains(response, '<form method="POST">')
        self.assertContains(response, '<form method="POST" action="/lists/new">')
        self.assertContains(response, '<input name="item_text"')

    def test_displays_all_list_items(self):
        mylist = List.objects.create()
        Item.objects.create(text="itemey 1", list=mylist)
        Item.objects.create(text="itemey 2", list=mylist)

        response = self.client.get("/lists/the-only-list-in-the-world/")

        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")
