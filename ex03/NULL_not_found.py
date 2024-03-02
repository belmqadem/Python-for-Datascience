def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if object is None:
        print("Nothing:", object, obj_type)
    elif object != object:
        print("Cheese:", object, obj_type)
    elif object == 0 and obj_type == int:
        print("Zero:", object, obj_type)
    elif object is Empty:
        print("Empty:", obj_type)
    elif object is False and obj_type == bool:
        print("Fake:", object, obj_type)
    else:
        print("Type not Found")
        return 1
    return 0

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))