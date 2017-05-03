from blog.forms import PostModelForm
data = {'title': 'This is title',
'subtitle': 'This is subtitle','tags.tag_name':'test','content': 'This is content'}
f = PostModelForm(data)
