from django.test import SimpleTestCase
from django.urls import reverse ,resolve
from .views import HomePageView
# (SimpleTestCase) that is designed for webpages that do not have a model included
# resolve() لتحديد وظيفة العرض التي يتم تعيينها لمسار ويب معين
class HomePagesTest(SimpleTestCase):

    def setUp(self):
        url=reverse('home')
        self.response=self.client.get(url)


    #  we can remove the test_homepage_url_name test since we’re using the reverse on home each time in setUp
    # def test_homepage_url_name(self):
    #     response=self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code,200)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response,'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response,'HomePage')

    def test_homepage_dose_not_contains_incorrect_html(self):
        self.assertNotContains(self.response,'this is not the home page')

    def test_homepage_url_resolves_HomePageView(self):
        view=resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )



