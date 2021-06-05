from django import forms

GROUP_NAME_SET = [
        ('home', 'home group'),
        ('work', 'work group'),
        ('others', 'all other contact'),
    ]


class SelectGroup(forms.Form):
    selected_group = forms.CharField(label='Selected Group', max_length=50)


class SelectGroupFromSet(forms.Form):
    selected_group = forms.ChoiceField(label='Selected Group', choices=GROUP_NAME_SET)

