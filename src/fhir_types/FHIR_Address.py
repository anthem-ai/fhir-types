from typing import Any, List, Literal, TypedDict

from .FHIR_Element import FHIR_Element
from .FHIR_Period import FHIR_Period
from .FHIR_string import FHIR_string

# An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
FHIR_Address = TypedDict(
    "FHIR_Address",
    {
        # Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces.
        "id": FHIR_string,
        # May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance  applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension.
        "extension": List[Any],
        # The purpose of this address.
        "use": Literal["home", "work", "temp", "old", "billing"],
        # Extensions for use
        "_use": FHIR_Element,
        # Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.
        "type": Literal["postal", "physical", "both"],
        # Extensions for type
        "_type": FHIR_Element,
        # Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific parts.
        "text": FHIR_string,
        # Extensions for text
        "_text": FHIR_Element,
        # This component contains the house number, apartment number, street name, street direction,  P.O. Box number, delivery hints, and similar address information.
        "line": List[FHIR_string],
        # Extensions for line
        "_line": List[FHIR_Element],
        # The name of the city, town, suburb, village or other community or delivery center.
        "city": FHIR_string,
        # Extensions for city
        "_city": FHIR_Element,
        # The name of the administrative area (county).
        "district": FHIR_string,
        # Extensions for district
        "_district": FHIR_Element,
        # Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes).
        "state": FHIR_string,
        # Extensions for state
        "_state": FHIR_Element,
        # A postal code designating a region defined by the postal service.
        "postalCode": FHIR_string,
        # Extensions for postalCode
        "_postalCode": FHIR_Element,
        # Country - a nation as commonly understood or generally accepted.
        "country": FHIR_string,
        # Extensions for country
        "_country": FHIR_Element,
        # Time period when address was/is in use.
        "period": FHIR_Period,
    },
    total=False,
)
