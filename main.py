import json
import os.path
from uuid import uuid4
from datetime import datetime


class Person:
    serialized_obj = {}

    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"id: {self.id} created_at: {self.created_at} updated_at: {self.updated_at}"

    def in_dict(self):
        to_json = self.__dict__
        to_json['__class__'] = str(self.__class__.__name__)

        return to_json

    def new_class(self):
        key = f"{self.__class__.__name__}.{self.id}"
        return key

    def save(self):
        print('serialized_obj', self.serialized_obj)
        self.serialized_obj[self.new_class()] = self.in_dict()
        with open('file.json', "w") as file:
            json.dump(self.serialized_obj, file, indent=2)

    def reload(self):
        with open('file.json', "r") as file:
            if os.path.getsize('file.json') > 0:
                try:

                    content = json.load(file)

                    for k, v in content.items():
                        print("key", k)
                        #  print("v", v)

                        self.serialized_obj[k] = v

                except json.decoder.JSONDecodeError:
                    print("Decoding error")


person1 = Person()
#  print(person1)
person1.reload()
person1.save()

#  person2 =Person("Edmund", 31, "Male")
#  print(person2)
#  person2.save()
