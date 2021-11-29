"""
Contains user related API
"""


def get_users():
    """
    .. http:get:: /users

       Returns all the users who are registered on this application

       :query sort: (**optional**) one of ``hit``, ``created-at``
       :query offset: (**optional**) offset number. default is 0
       :query limit: (**optional**) limit number. default is 30
       :reqheader Accept: application/json
       :reqheader Authorization: Bearer ``token``
       :resheader Content-Type: application/json
       :statuscode 200: success
       :statuscode 404: there's no user

       **Example request**:

       .. sourcecode:: http

          GET /users HTTP/1.1
          Host: example.com
          Accept: application/json, text/javascript
          Authorization: Bearer dX5g57pbafuav54b1a5f


       **Example response**:

       .. sourcecode:: http

          HTTP/1.1 200 OK
          Vary: Accept
          Content-Type: text/javascript

          [
            {
              "user_id": 12345,
              "user_name": "John Doe"
            },
            {
              "user_id": 12346,
              "user_name": "Jane Doe"
            }
          ]


    """
    return [{"user": "Ram"}]


def add_user(user):
    """
    .. http:post:: /users

       Adds a new user

       :reqheader Accept: application/json
       :reqheader Authorization: Bearer ``token``

       :jsonparam string user_name: The name of new user
       :jsonparam boolean super_user: whether it's a superuser or not

       :resheader Content-Type: application/json
       :statuscode 201: user was created
       :statuscode 400: bad request
       :statuscode 401: You do not have authorization

       **Example request**:

       .. sourcecode:: http

          POST /users HTTP/1.1
          Host: example.com
          Accept: application/json, text/javascript
          Authorization: Bearer dX5g57pbafuav54b1a5f

          {
            "user_name": "New User",
            "super_user" : true
          }


       **Example response**:

       .. sourcecode:: http

          HTTP/1.1 201 CREATED
          Vary: Accept
          Content-Type: text/javascript

          {
            'message': 'created'
          }


    """
    print(f"saving user{user}...")
    return "user saved"
