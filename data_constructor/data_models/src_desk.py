# coding=utf-8

from data_constructor.data_models.utils import Utils

class Column(object):

    CASES = ["type", "subject", "priority", "status", "labels", "_links", "message"]

class Collection(object):

    @classmethod
    def cases(cls, faker):

        """
        :DESK:API:CASE:phone:sample:
            {
          "type": "phone",
          "subject": "Creating a case via the API",
          "priority": 4,
          "status": "open",
          "labels": [
            "Spam",
            "Ignore"
          ],
          "_links": {
            "customer": {
              "href": "/api/v2/customers/1",
              "class": "customer"
            },
            "assigned_user": {
              "href": "/api/v2/users/1",
              "class": "user"
            },
            "assigned_group": {
              "href": "/api/v2/groups/1",
              "class": "group"
            },
            "locked_by": {
              "href": "/api/v2/users/1",
              "class": "user"
            },
            "entered_by": {
              "href": "/api/v2/users/1",
              "class": "user"
            }
          },
          "message": {
            "direction": "out",
            "body": "Please assist me with this case"
          }
        }
        """

        _TYPE = ["phone"]
        _PRIORITY = [1, 2, 3, 4, 5]
        _STATUS = ["open", "new", "pending", "resolved", "closed"]
        _LABELS = ["Spam", "Ignore"]
        _LINKS = {"customer": {"href": "/api/v2/customers/370257800", "class": "customer"}}
        _MESSAGE = {"direction": "out", "body": "Please assist me with this case"}

        value = [_TYPE[0], faker.text(max_nb_chars=20), faker.random_element(_PRIORITY),
                 faker.random_element(_STATUS), _LABELS, _LINKS, _MESSAGE]

        return Utils.to_dict(Column.CASES, value)


