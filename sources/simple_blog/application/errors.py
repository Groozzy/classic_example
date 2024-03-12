from classic.error_handling import Error


class BlogError(Error):
    namespace = 'blog'


class NoPost(BlogError):
    message_template = 'No post with id "{id}"'
