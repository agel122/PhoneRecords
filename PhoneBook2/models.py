from django.db import models
from django.urls import reverse


class WorkGroup(models.Model):
    groupname = models.CharField(max_length=100, primary_key=True, help_text='please, specify the name'
                                                                        'of group')
    groupinfo = models.TextField(help_text='please, specify additional info if required')

    def __str__(self):
        return self.groupname


# alternative group-selection from set:
class WorkGroupSet(models.Model):
    GROUP_NAME_SET = [
        ('home', 'home group'),
        ('work', 'work group'),
        ('others', 'all other contact'),
    ]
    groupname = models.CharField(max_length=20, choices=GROUP_NAME_SET)

    def __str__(self):
        return self.groupname


class PhoneRecord(models.Model):
    name = models.CharField(max_length=100, help_text='any Name is OK here')
    phone = models.CharField(max_length=11, help_text='any phone-number is OK here')
    mailbox = models.EmailField(max_length=100, help_text='email address with @ required')
    group = models.ForeignKey(WorkGroup, on_delete=models.CASCADE, help_text='need to define group')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('records_detail', args=[str(self.id)])


# alternative group-selection from set:
class PhoneRecordWithGroups(models.Model):
    GROUP_NAME_SET = [
        ('home', 'home group'),
        ('work', 'work group'),
        ('others', 'all other contact'),
    ]
    name = models.CharField(max_length=100, help_text='any Name is OK here')
    phone = models.CharField(max_length=11, help_text='any phone-number is OK here')
    mailbox = models.EmailField(max_length=100, help_text='email address with @ required')
    group = models.CharField(max_length=20, choices=GROUP_NAME_SET)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('records_detail', args=[str(self.id)])
