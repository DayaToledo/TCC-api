from pydantic import BaseModel, Field

class Questions(BaseModel):
    EXT1: int = Field(example=4)
    EXT2: int = Field(example=1)
    EXT3: int = Field(example=5)
    EXT4: int = Field(example=2)
    EXT5: int = Field(example=5)
    EXT6: int = Field(example=1)
    EXT7: int = Field(example=5)
    EXT8: int = Field(example=2)
    EXT9: int = Field(example=4)
    EXT10: int = Field(example=1)
    EST1: int = Field(example=1)
    EST2: int = Field(example=4)
    EST3: int = Field(example=4)
    EST4: int = Field(example=2)
    EST5: int = Field(example=2)
    EST6: int = Field(example=2)
    EST7: int = Field(example=2)
    EST8: int = Field(example=2)
    EST9: int = Field(example=3)
    EST10: int = Field(example=2)
    AGR1: int = Field(example=2)
    AGR2: int = Field(example=5)
    AGR3: int = Field(example=2)
    AGR4: int = Field(example=4)
    AGR5: int = Field(example=2)
    AGR6: int = Field(example=3)
    AGR7: int = Field(example=2)
    AGR8: int = Field(example=4)
    AGR9: int = Field(example=3)
    AGR10: int = Field(example=4)
    CSN1: int = Field(example=3)
    CSN2: int = Field(example=4)
    CSN3: int = Field(example=3)
    CSN4: int = Field(example=2)
    CSN5: int = Field(example=2)
    CSN6: int = Field(example=4)
    CSN7: int = Field(example=4)
    CSN8: int = Field(example=2)
    CSN9: int = Field(example=4)
    CSN10: int = Field(example=4)
    OPN1: int = Field(example=5)
    OPN2: int = Field(example=1)
    OPN3: int = Field(example=4)
    OPN4: int = Field(example=1)
    OPN5: int = Field(example=4)
    OPN6: int = Field(example=1)
    OPN7: int = Field(example=5)
    OPN8: int = Field(example=3)
    OPN9: int = Field(example=4)
    OPN10: int = Field(example=5)

class Result(BaseModel):
    Prediction: str
