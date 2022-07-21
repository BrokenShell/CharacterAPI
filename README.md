# Character API Workshop
API for CRUD operations on a Mongo Database.


## Character Object

### Required Fields
- name: str [3, 64] char len
- level: int [1, 20]
- profession: str ["Fighter", "Mage", "Cleric", "Rogue"]
- offence: float [0, 1)
- defense: float [0, 1)

### Automatically Generated Fields
- created_at: datetime
- updated_at: datetime
