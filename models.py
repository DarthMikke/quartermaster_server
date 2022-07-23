import json
from django.db import models


class ModelValidationError(Exception):
    pass


class Thing:
    __keys__ = [
        'make', 'amount', 'categoryId', 'multiplier'
    ]

    @classmethod
    def validate(cls, instance):
        for key in cls.__keys__:
            if key not in instance.keys():
                raise ModelValidationError


# Create your models here.
def get_entities(plural):
    try:
        with open(f"quartermaster_data/{plural}.json") as fh:
            return json.load(fh)
    except Exception as e:
        raise e


def save_entities(plural, entities):
    if type(entities) != list:
        raise TypeError("Tried to save an object instead of an array.")
    try:
        with open(f"quartermaster_data/{plural}.json", "w") as fh:
            return json.dump(entities, fh)
    except Exception as e:
        raise e


def put_entity(plural, instance):
    """This function performs no instance validation whatsoever!"""
    entities = get_entities(plural)

    for i in range(len(entities)):
        if entities[i]['id'] == instance['id']:
            entities[i] = instance
            save_entities(plural, entities)
            return instance

    max_id = 0 if len(entities) == 0 else max([x['id'] for x in entities])
    instance['id'] = max_id + 1
    entities.append(instance)
    save_entities(plural, entities)
    return instance


def patch_entity(plural, instance):
    """This function performs no instance validation whatsoever!"""
    entities = get_entities(plural)

    for i in range(len(entities)):
        if entities[i]['id'] == instance['id']:
            for key in instance.keys():
                entities[i][key] = instance[key]
            save_entities(plural, entities)
            return instance

    raise EntityNotFound()


def delete_entity(plural, instance):
    """This function performs no instance validation whatsoever!"""
    entities = get_entities(plural)

    for i in range(len(entities)):
        if entities[i]['id'] == instance['id']:
            deleted = entities.pop(i)
            save_entities(plural, entities)
            return deleted

    raise EntityNotFound()


class EntityNotFound(Exception):
    pass
