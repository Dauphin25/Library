from django.shortcuts import render
from django.views.generic import DetailView

from market.models.author import Author


def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'author/author.html', {'authors': authors})


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail.html'
    context_object_name = 'author'
    pk_url_kwarg = 'author_id'
    query_pk_and_slug = True
    slug_field = 'name'
    slug_url_kwarg = 'author_name'
    extra_context = {}
    extra_context['title'] = 'Author Detail'
    extra_context['header'] = 'Author Detail'
    extra_context['description'] = 'This is the detail of the author'
    extra_context['keywords'] = 'author, detail, author detail'
