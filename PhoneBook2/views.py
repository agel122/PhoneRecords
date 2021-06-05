from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import PhoneRecord, PhoneRecordWithGroups

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SelectGroup, SelectGroupFromSet


class PhoneBookListView(ListView):
    # model = PhoneRecord
    model = PhoneRecordWithGroups
    template_name = 'records_list.html'


class PhoneBookDetailView(DetailView):
    # model = PhoneRecord
    model = PhoneRecordWithGroups
    template_name = 'records_detail.html'


class PhoneBookCreateView(CreateView):
    # model = PhoneRecord
    model = PhoneRecordWithGroups
    template_name = 'records_new.html'
    fields = ['name', 'phone', 'mailbox', 'group']


class PhoneBookUpdateView(UpdateView):
    # model = PhoneRecord
    model = PhoneRecordWithGroups
    template_name = 'records_edit.html'
    fields = ['name', 'phone', 'mailbox', 'group']


class PhoneBookDeleteView(DeleteView):
    # model = PhoneRecord
    model = PhoneRecordWithGroups
    template_name = 'records_delete.html'
    success_url = reverse_lazy('records_list')


class PhoneBookListViewSel(ListView):
    # model = PhoneRecord
    model = PhoneRecordWithGroups
    template_name = 'records_list.html'

    def get_queryset(self):
        if self.request.method == 'GET':
            selection = self.request.GET.get('selected_group')
            # return PhoneRecord.objects.filter(group__groupname=selection)
            return PhoneRecordWithGroups.objects.filter(group__iexact=selection)


def select_group(request):
    if request.method == 'POST':
        # form = SelectGroup(request.POST)
        form = SelectGroupFromSet(request.POST)
        if form.is_valid():
            selected_group = form.cleaned_data['selected_group']
            return HttpResponseRedirect(f"{reverse('selected_group')}?selected_group={selected_group}")
    else:
        form = SelectGroup()
    return render(request, 'records_select.html', {'form': form})



