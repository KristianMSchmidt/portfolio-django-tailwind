from django.test import TestCase
from django.urls import reverse
from .models import Mail
from .forms import ContactForm

class HomeViewTest(TestCase):
    
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/home.html')
        self.assertTemplateUsed(response, 'portfolio/base.html')
        self.assertTemplateUsed(response, 'tailwind/tags/css.html')
        # Template should neither contain message success or error messags
        self.assertNotContains(response, "Your message was not send.")
        self.assertNotContains(response, "Enter a valid email address.")

    def test_send_valid_message(self):
        """
        Sending valid message will generate new object in mail database and redirect user back home.
        """
        post = {'name': 'Bob', 'sender': 'bob@mail.dk',
                'subject': 'some subject', 'message': 'some message'}
 
        response = self.client.post(reverse('home'), post)
        num_mails_in_database = Mail.objects.all().count()
 
        self.assertEqual(num_mails_in_database,1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('home'))

    def test_message_with_invalid_mail(self):
        """
        Sending message with invalid mail address will not generate new object in mail database and not redirect
        Correct feedback message is shown.
        """
        post = {'name': 'Bob', 'sender': 'bob@mail',
                'subject': 'some subject', 'message': 'some message'}
        response = self.client.post(reverse('home'), post)
        num_mails_in_database = Mail.objects.all().count()

        self.assertEqual(num_mails_in_database, 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/home.html')
        self.assertNotContains(response, "Your message was send.")
        self.assertContains(response, "Enter a valid email address.")

    def test_message_with_no_subject(self):
        """
        Sending message with no name will not generate new object in mail database and not redirect.
        Correct feedback message is shown.
        """
        post = {'name': '', 'sender': 'bob@mail.dk',
                'subject': 'some subject', 'message': 'some message'}
        response = self.client.post(reverse('home'), post)
        num_mails_in_database = Mail.objects.all().count()

        self.assertEqual(num_mails_in_database, 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/home.html')
        self.assertNotContains(response, "Your message was send.")


class ContactFormTest(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Hanne',
            'sender': 'hanne@mail.dk',
            'subject': 'some subject',
            'message': 'some message',
        }

    def test_bad_email_is_invalid(self):
        """ email must contain @ """
        self.data['sender'] = 'hannemail.dk'
        form = ContactForm(data=self.data)

        is_valid = form.is_valid()

        self.assertFalse(is_valid)

        self.assertTrue('sender' in form.errors)
        self.assertTrue(
            'Enter a valid email address.' in str(form.errors))
        self.assertFalse('name' in form.errors)
        self.assertFalse('subject' in form.errors)
        self.assertFalse('message' in form.errors)
     
    def test_no_message_is_invalid(self):
        """ email must message """
        self.data['message'] = ''
        form = ContactForm(data=self.data)

        is_valid = form.is_valid()

        self.assertFalse(is_valid)

        self.assertTrue('message' in form.errors)
        self.assertTrue(
            'This field is required.' in str(form.errors))
        self.assertFalse('name' in form.errors)
        self.assertFalse('email' in form.errors)
        self.assertFalse('subject' in form.errors)
