import tweepy

consumer_key = "p0dAIU5hN6QMZrVQNzMhtyQvp"
consumer_secret = "wcsdHwzKaovI77rIJJJKqj6x8jMpMDQKg7Pjv0DGd9mC51qNKj"
access_key = "1012273463162122241-Y7yS3qTXrGyLhM6ovzbvdegrb0ZPKW"
access_secret = "jwUiH3SLm2fTHorpwTOq7DJYTY49HgkW8wXFon1YdejGw"

oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_key, access_secret)

api = tweepy.API(oauth)

public_tweets = api.search('#cricket')
print(public_tweets)


#  What are Access Tokens ?
"""
Access tokens are the thing that applications use to make API requests on behalf of a user.
The access token represents the authorization of a specific application to access specific parts of a user’s data.

Access tokens must be kept confidential in transit and in storage.
The only parties that should ever see the access token are the application itself,
the authorization server, and resource server.
The application should ensure the storage of the access token 
is not accessible to other applications on the same device.
 The access token can only be used over an https connection,
 since passing it over a non-encrypted channel would make it trivial for third parties to intercept.

The token endpoint is where apps make a request to get an access token for a user.

My Twitter Access Token : access_key = "1012273463162122241-Y7yS3qTXrGyLhM6ovzbvdegrb0ZPKW"
"""

# Some Trusted Website IP Addresses
# Google -> 172.217.163.132


# Facebook -> 157.240.16.39

# Youtube ::
"""
    216.58.196.174
    172.217.163.110
    172.217.163.174
    172.217.163.206
    172.217.166.110
"""

# Difference Between Library and API

"""
An architect (read application developer) wanted to build a house(read application),
so he prepared for all its aspects including structure, plumbing, wiring, decors etc(read different libraries).

He cant do all of the stuff himself so he took help from various experts in those fields,
who are really good at doing what they do.
But he needed communicate his needs and requirements face to face or via mail (read invoking API )
so that they can cater to his need and provide the asked service.
After some time a fellow Architect came and wanted to accomplish
a similar task but with a few add on features like swimming pool (a new library).
He can conveniently use the framework provided by our architect and add new features invoking any new service.


A library -> is a collection of functions / objects that serves one particular purpose. you could use a library 
in a variety of projects.

An API -> is an interface for other programs to interact with your program or library  without having direct access.
examples: JQuery,XML,Wordpress,PHP,Javascript etc

A framework -> is a collection of patterns and libraries to help with building an application.

                    A framework thus can be easily extended to plan a town having various houses,
                    which may be same or similar (having some new feature like swimming pool).
eg- Angular js- a JS framework may use many libraries like inline editing of text using an exposed API of that library.

"""
