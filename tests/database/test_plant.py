from house_plant.database.plant import create_plant_rows, PetFriendly, SoilTypes, PlantORM

PASSING_PLANTS = [
    {
    "id": 1, # TODO: once this is automatic, update
    "name": "Kermit",

    # TODO: add in once location table has been added
    # location_name:
    "sublocation_name": "Doro's office",

    "scientific_type": "Kermitops gratus", # this is an actual frog! :)
    "common_type": "frog",

    # Not typed as optional because it will default to unknown
    # But not a required user input
    "pet_friendly": PetFriendly.PET_SAFE,
    "soil": SoilTypes.UNKNOWN,

    # int is number of days
    "fertilizing_cadence":  None,
    "repotting_cadence": 1,

    "light_info": None,
    "dryness_info": None,
    "fertilizing_info": None,
    },
    {
    "id": 2, # TODO: once this is automatic, update
    "name": "Miss Piggy",

    # TODO: add in once location table has been added
    # location_name:
    "sublocation_name": "Doro's office",

    "scientific_type": "Pigathius Lee",
    "common_type": "pig",

    # Not typed as optional because it will default to unknown
    # But not a required user input
    "pet_friendly": PetFriendly.PET_SAFE,
    "soil": SoilTypes.UNKNOWN,

    # int is number of days
    "fertilizing_cadence":  None,
    "repotting_cadence": 1,

    "light_info": None,
    "dryness_info": None,
    "fertilizing_info": None,
    }
]
# FAILING_PLANTS ={} # TODO: add once validation is added 


def test_create_plant_rows():
    rows = create_plant_rows(PASSING_PLANTS)
    for thing in rows:
        assert isinstance(thing, PlantORM)
