from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from models import *

# Returns a webpage showing a BlogPost matching a specific post_id
def blog_post(request, post_id):
    # Get post matching post_id or raise a HTTP 404 error
    post = get_object_or_404(BlogPost, id=post_id)

    # post = get_object_or_404(BlogPost, id=post_id) is basically the same as
    # post = None
    # try:
    #     post = BlogPost.objects.filter(id=post_id)[0]
    # except IndexError:
    #     raise Http404

    data = {'post': post}
    return render(request, 'blog_post.html', data)

# Returns a webpage showing a list of all BlogPosts in the database
def all_posts(request):
    # Find all blog posts
    data = {'posts': BlogPost.objects.all()}
    print BlogPost.objects.all()
    return render(request, 'all_blog_posts.html', data)

# Returns a form to create a BlogPost
def create(request):
    # Find all authors
    authors = Author.objects.all()
    data = {'authors': authors}
    return render(request, 'create_form.html', data)

# Handles the data sent by the form generated by create
def save_post(request):
    # success indicates whether or not post was sucessfully saved
    success = False 
    message = ''
    # Make sure form uses correct method
    if request.method == 'POST':
        success = True
        try:
            # Find author from the form
            a = Author.objects.filter(id=request.POST['author'])[0]
            t = request.POST['title'].strip()
            p = request.POST['post'].strip()
            # Create a new BlogPost object with form's data
            new_post = BlogPost(title=t, post=p, author=a)
            # Validate and save the BlogPost
            new_post.full_clean()
            new_post.save()
        # Is the author_id valid?
        except IndexError:
            success = False
            message = "Error: Invalid author"
        # Did the form have all the necessary fields?
        except KeyError:
            success = False
            message = "Error: Form missing necessary fields"
        # Were all fields properly filled out?
        except ValidationError:
            success = False
            message = "Error: Form set invalid information"

    data = {
        'success': success,
        'message': message
    }
    return render(request, 'submission_response.html', data)

# Returns a webpage listing a specific author's BlogPosts
def author(request, author_id):
    # Find author matching author_id or raise an HTTP 404 error
    author = get_object_or_404(Author, id=author_id) 
    posts = BlogPost.objects.filter(author=author)
    
    data = {
        'author': author,
        'posts' : posts
    }
    
    return render(request, 'author.html', data)

# Returns a webpage listing all authors in the database
def all_authors(request):
    # Find all authors
    data = {'authors': Author.objects.all()}
    return render(request, 'all_authors.html', data)

def create_author(request):
    data = {}
    return render(request, 'create_author.html', data)

def save_author(request):
    success = False
    message = ''
    if request.method == 'POST':
        success = True
        try: 
            f = request.POST['first'].strip()
            l = request.POST['last'].strip()
            g = request.POST['gender'].strip()

            a = Author(first = f, last = l, gender = g)

            a.full_clean()
            a.save()
        except KeyError:
            success = False
            message = 'Error: Form missing necessary fields.'
        except ValidationError:
            success = False
            message = 'Error: Form set invalid information.'
    data = {
        'success' : success,
        'message' : message
    }

    return render(request, 'author_response.html', data)
