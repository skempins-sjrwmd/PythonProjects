from flask.views import MethodView
from flask import jsonify, request, abort

class PetAPI(MethodView):
    pets = [
        {"id": 1, "name": u"Mac", "links": [{"rel": "self", "href": "/pets/1"}]},
        {"id": 2, "name": u"Leo", "links": [{"rel": "self", "href": "/pets/2"}]},
        {"id": 3, "name": u"Brownie", "links": [{"rel": "self", "href": "/pets/3"}]}
    ]

    def get(self, pet_id):
        #print("pet_id="+str(pet_id))
        if pet_id:
            return jsonify({"pets": self.pets[pet_id-1]})
        else:
            return jsonify({"pets": self.pets})
