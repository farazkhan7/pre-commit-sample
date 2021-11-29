"""
Contains category related API
"""


def get_categories():
    """
    .. http:get:: /categories

       Returns all the categories

       :query sort: (**optional**) one of ``hit``, ``created-at``
       :query offset: (**optional**) offset number. default is 0
       :query limit: (**optional**) limit number. default is 30
       :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
       :reqheader Authorization: optional OAuth token to authenticate
       :resheader Content-Type: this depends on :mailheader:`Accept`
                                header of request
       :statuscode 200: no error
       :statuscode 404: there's no user


    """
    return [{"user": "Ram"}]


def update_category(category_id):
    """
    .. http:put:: /category/(int:category_id)

       Updates an existing category

       :reqheader Accept: application/json
       :reqheader Authorization: Bearer ``token``
       :reqheader Content-Type: application/x-www-form-urlencoded

       :param category_id: post's unique id
       :type category_id: int

       :form category_new_name: new updated name for category

       :resheader Content-Type: application/json
       :statuscode 204: Category was updated
       :statuscode 400: bad request
       :statuscode 401: You do not have authorization

    """
    print(f"updating category {category_id}...")
    return "category updated"
