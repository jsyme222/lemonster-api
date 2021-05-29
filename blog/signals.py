from tags.models import BlogTag

def set_blog_tag_usage(sender, action, **kwargs) -> None:
    inst = kwargs["instance"]
    tags = kwargs["pk_set"]
    for tag in tags:    
        tag = BlogTag.objects.get(pk=tag)
        if action == "post_add":
            print("ADDING TAG")
            print(tag.title)
            tag.set_usage(True)
        elif action == "post_remove":
            print("REMOVING TAG")
            print(tag.title)
            tag.set_usage()
    # tags = sender.tags.all()
    # for t in tags:

