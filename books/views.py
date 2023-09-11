
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.http import HttpRequest
from django.views.generic import ListView , DetailView , FormView 
from django.db.models import Q
from .models import Books , Review
from .forms import BookForm , ReviewForm




class bookViewList(LoginRequiredMixin, ListView):
    model = Books
    context_object_name = 'books'
    template_name = 'book_list.html'
    login_url = 'account_login'

    

class SearchList(ListView):
    model = Books
    context_object_name = 'result'
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Books.objects.filter(
            Q(title__icontains = query) | Q(auth__icontains = query) 
        )
    

class CreateBook(FormView , LoginRequiredMixin):
    form_class = BookForm
    template_name = 'book_create.html'
    success_url = 'books/'
    initial = {'key' : 'value'}

    def post(self, request):
        if request.method == 'POST':
            form = BookForm(request.POST , request.FILES)
            if form.is_valid():
                form.save()
        return render(request, self.template_name , {'form' : form})
    

        
def getBookDetalis(request , pk):
    book = Books.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
                form.save(commit=False)
                form.auth = request.user
                form.book = book
                form.save()
    else:
        form = ReviewForm()
    
    context={'form':form , 'book':book}

    return render(request, 'book_detalis.html' , context)
