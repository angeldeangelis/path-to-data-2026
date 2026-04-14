import re

structural_elements = [
    {
        "element_id": "E1001",
        "age_years": 15,
        "material": "Concrete",
        "element_type": "Bridge Pier",
        "load_capacity_tons": 120,
        "last_inspection_id": "I2301",
    },
    {
        "element_id": "e1002",
        "age_years": 27,
        "material": "concrete",
        "element_type": "Retaining Wall",
        "load_capacity_tons": 40,
        "last_inspection_id": "i2302",
    },
    {
        "element_id": "E1003",
        "age_years": 4,
        "material": "Steel",
        "element_type": "Steel Beam",
        "load_capacity_tons": 15,
        "last_inspection_id": "i2303",
    },
    {
        "element_id": "e1004",
        "age_years": 32,
        "material": "Wood",
        "element_type": "Temporary Support",
        "load_capacity_tons": 10,
        "last_inspection_id": "I2304",
    },
]


def find_invalid_elements(
    element_id,
    age_years,
    material,
    element_type,
    load_capacity_tons,
    last_inspection_id,
):
    constraints = {
        "element_id": isinstance(element_id, str)
        and re.fullmatch(r"e\d+", element_id, re.IGNORECASE),
        "age_years": isinstance(age_years, int) and age_years >= 0,
        "material": isinstance(material, str)
        and material.lower() in ("concrete", "steel"),
        "element_type": isinstance(element_type, str),
        "load_capacity_tons": isinstance(load_capacity_tons, int)
        and load_capacity_tons >= 20,
        "last_inspection_id": isinstance(last_inspection_id, str)
        and re.fullmatch(r"i\d+", last_inspection_id, re.IGNORECASE),
    }

    return [key for key, value in constraints.items() if not value]


def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False

    is_invalid = False
    key_set = {
        "element_id",
        "age_years",
        "material",
        "element_type",
        "load_capacity_tons",
        "last_inspection_id",
    }

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                f"Invalid format: {dictionary} at position {index} "
                f"has missing and/or invalid keys."
            )
            is_invalid = True
            continue

        invalid_elements = find_invalid_elements(**dictionary)

        for key in invalid_elements:
            print(
                f"Unexpected format '{key}: {dictionary[key]}' "
                f"at position {index}."
            )
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True


validate(structural_elements)