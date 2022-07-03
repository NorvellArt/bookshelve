from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .forms import BookForm
from django.http import HttpResponseRedirect


class UserBooksList(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'my_books/book_list.html'
    context_object_name = 'book_list'
    ordering = ['-is_complete']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = context['book_list'].filter(user=self.request.user)
        context['title'] = 'Мои книги'
        return context


class BookDetail(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'my_books/book_detail.html'
    context_object_name = 'book'


class AddNewBook(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'my_books/book_forms.html'
    success_url = reverse_lazy('my_books')
    form_class = BookForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddNewBook, self).form_valid(form)


class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'my_books/book_forms.html'
    success_url = reverse_lazy('my_books')
    form_class = BookForm


class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('my_books')


    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = reverse_lazy('my_books')
            return HttpResponseRedirect(url)
        else:
            return super(DeleteBook, self).post(request, *args, **kwargs)

