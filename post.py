import facebook as fb

from cred import access_token

user_intance_bot=fb.GraphAPI(access_token)

message='''
    Hello, guys this is system generated post.
    I hope you all are doing good.

    Don't reply to this post.
'''

user_intance_bot.put_object('me','feed',message=message)

print('Posted successfully')