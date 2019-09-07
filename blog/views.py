from django.shortcuts import render

# Create your views here.
def post_list(requet):
    return render(requet, 'blog/post_list.html', {})
