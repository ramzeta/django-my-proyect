from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    def init(self, args, **kwargs):
        super(UserCreateForm, self).init(args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})