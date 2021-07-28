from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    sender = forms.EmailField(label="Email")
    subject = forms.CharField(max_length=100, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")

    # This will add custom classes to input fields
    name.widget.attrs.update({"class": "flex-grow mr-6 border-none w-full"})
    sender.widget.attrs.update({"class": "flex-grow border-none w-full"})
    subject.widget.attrs.update({"class": "flex-grow border-none w-full"})
    message.widget.attrs.update(
        {"class": "h-32 lg:h-20 border-none flex-grow w-full px-2 w-full"}
    )


class XXX():
    name = 4

    sex = "femals"


class yyy():

    pass
