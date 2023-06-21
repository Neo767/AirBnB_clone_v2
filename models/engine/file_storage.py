#!/usr/bin/python3
<<<<<<< HEAD
    '''
    Define class FileStorage
    '''
import json
import models
=======
"""
    Define class FileStorage
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
>>>>>>> b90f50a7fab0cf2c02368505aa62818f60ace865


class FileStorage:
    '''
<<<<<<< HEAD
    Serializes instances to JSON file and deserializes to JSON file.
=======
        Serializes instances to JSON file and deserializes to JSON file.
>>>>>>> b90f50a7fab0cf2c02368505aa62818f60ace865
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
<<<<<<< HEAD
        Return the dictionary
        '''
        if cls is None:
            return self.__objects
        else:
            my_dict = {}
            for k, v in self.__objects.items():
                name = k.split('.')
                if name[0] in str(cls):
                    my_dict[k] = v
            return my_dict
            
=======
            Return the dictionary
        '''
        fs_objects = {}
        if cls:
            if type(cls) is str and cls in classes:
                for key, val in self.__objects.items():
                    if cls == key.split('.')[0]:
                        fs_objects[key] = val
            elif cls.__name__ in classes:
                for key, val in self.__objects.items():
                    if cls.__name__ == key.split('.')[0]:
                        fs_objects[key] = val
        else:
            return self.__objects
        return fs_objects

>>>>>>> b90f50a7fab0cf2c02368505aa62818f60ace865
    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
<<<<<<< HEAD

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
            '''
            try:
                with open(FileStorage.__file_path, encoding="UTF8") as fd:
                    FileStorage.__objects = json.load(fd)
                for key, val in FileStorage.__objects.items():
                    class_name = val["__class__"]
                    class_name = models.classes[class_name]
                    FileStorage.__objects[key] = class_name(**val)
            except FileNotFoundError:
                pass
        
    def delete(self, obj=None):
        '''
            Deletes an object from __objects if it is inside of __objects
        '''
        copy_storage = dict(FileStorage.__objects)
        desired_key = obj
        for key, val in copy_storage.items():
            if val == desired_key:
                del(obj)
                del FileStorage.__objects[key]
                self.save()
    
    def close(self):
        ''' deserializes json file to objects '''
=======
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete object from __objects if it's inside
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]
        self.save()

    def close(self):
        """
        call reload
        """
>>>>>>> b90f50a7fab0cf2c02368505aa62818f60ace865
        self.reload()
