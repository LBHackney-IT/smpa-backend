# Screen 1

Enter postcode

* postcode - str
    * E8 3HW or N16 8ED

# Screen 2

*Address info*
Address 128 Richmond Rd London
UPRN    10008300494
Easting & Northing: 534091, 184445
Ward:   Hoxton East and Shoreditch
BPLU use:   Residential
Property type:  Semi-detached house

*Constraints*
* Conservation area   Graham Road and Mapledene
* Listed building
    * Statuary    No
    * Local   No
* Flood zone  No  Find out more
* Trees Preservation Orders   No  Find out more
* Article 4 directions
    * A4D Light Industrial to Residential Use
    * A4D Storage and Distribution to Residential Use

## Questions:
What kind of data could show up under...
* flood zone
* tree preservation orders
* Do we have a definitive list of Article 4 Directions?

# Screen 3

* Have the works already started?
    * No
    * Yes
        * When did the work start?
            * Day
            * Month
            * Year

        * Has the work already been completed?
            * No
            * Yes
        * Describe what you have already done

# Screen 4

Proposals

* You are doing an extension or alteration - str - 
    * `proposal_extension`
* You are installing or replacing an equipment
    * `proposal_equipment`

# Screen 5

What are you making changes to?

## proposal_extension sub options
You are making changes to the original house
You are building, replacing or removing an outbuilding
You are making changes to gates, fences, garden walls, etc.
You are making changes to means of access to the site
You are affecting car and/or bike parking spaces

    {
    proposalName: “To the original house”,
    proposalId: “extension_original_house”,
    goTo: [“AboutChangesToOriginalHouse”]
    },
    {
    proposalName: “To any incidental buildings”,
    proposalId: “extension_incidental_buildings”,
    goTo: [“WorksXLocation”, “Outbuilding”]
    },
    {
    proposalName: “To gates, fences, garden walls, etc”,
    proposalId: “extension_gates_fences_etc”,
    goTo: [“GatesFencesWalls”, “WorksXLocation”]
    },
    {
    proposalName: “To means of access to the site”,
    proposalId: “extension_means_of_access_to_site”,
    goTo: [“Access”, “MoreAboutAccess”]
    },
    {
    proposalName: “Car and/or bike parking spaces”,
    proposalId: “extension_car_bike_spaces”,
    goTo: [“Parking”]
    }

# Screen 6

About the extension, improvement or alteration to the original house

These are probably classes, maybe called Work

* ! Single storey extension (including conservatory)
* Two storey extension
* Part single / Part two storey extension
* ! Basement works (including light wells)
* ! Roof works (including roof extensions)
* Outbuilding
* Porch
* Balcony or terrace
* Installation of a staircase

```
    extension_original_house: [
    {
    proposalName: “Single storey extension”,
    proposalId: “extension_original_house_single_storey_extension”,
    goTo: [“WorksXLocation”]
    },
    {
    proposalName: “Two storey extension”,
    proposalId: “extension_original_house_two_storey_extension”,
    goTo: [“WorksXLocation”]
    },
    {
    proposalName: “Part single / Part two storey extension”,
    proposalId: “extension_original_house_part_single_part_two_storey_extension”,
    goTo: [“WorksXLocation”]
    },
    {
    proposalName: “Basement”,
    proposalId: “extension_original_house_basement”,
    goTo: [“Basement”, “WorksXLocation”]
    },
    {
    proposalName: “Roof works”,
    proposalId: “extension_original_house_roof_works”,
    goTo: [“Roofs”, “WorksXLocation”]
    },
    {
    proposalName: “Outbuilding”,
    proposalId: “extension_original_house_outbuilding”,
    goTo: [“WorksXLocation”]
    },
    {
    proposalName: “Porch”,
    proposalId: “extension_original_house_porch”,
    goTo: [“WorksXLocation”]
    },
    {
    proposalName: “Balcony or terrace”,
    proposalId: “extension_original_house_balcony_terrace”,
    goTo: [“WorksXLocation”]
    },
    {
    proposalName: “Staircase”,
    proposalId: “extension_original_house_staircase”,
    goTo: [“WorksXLocation”]
    },
    {
    proposalName: “Addition and/or replacement of windows and doors”,
    proposalId: “extension_original_house_add_replacement_windows_doors”,
    goTo: [“WorksXLocation”]
    },
    {
    proposalName: “Changing and/or adding cladding”,
    proposalId: “extension_original_house_cladding”,
    goTo: [“WorksXLocation”]
    }
    ]
```


# Screen 7 etc.

About the Single storey extension
Where are the proposed works located in relation to the original house?

* ! Rear
* Side
* Front
* Rear / side wrap-around

Note: Maybe pull these options from API - could be logic about which are shown

Note: WorksClass needs to know which locations user can choose from, and which they have chosen. Or something.

## About basement
Where are the proposed works located in reference to the original house?
* Excavation of a new basement
* Enlargement of an existing basement
* Addition of lightwell(s)
* Other alterations to the appearance of the house
ETC! Will circle round to screen like the previous

    * Rear
    * Side
    * Front

## Roof circles round too...

* Addition of a dormer extension
* Removal of a dormer extension
* Creation of a mansard styled roof extension
* Installation of rooflight(s) and/or roof lantern(s)
* Addition of a new storey(s)
* Alteration of a roof slope
* Replacement of a roof structure and/or covering
* Removal of chimney
* Addition of chimney

## Works to outbuilding...

* Does the work include the removal or demolition of any existing outbuilding?
    * No
    * Yes
* Can you provide more detail?


## Gates, Fences, Walls

* What are the proposed works about - Select all that apply.
    * Addition of a new entrance
    * Removal of an entrance
    * Replacement and/or repair of wall
    * Replacement and/or repair of pillar caps

## Means of access

Would the proposed works affect access to the site for vehicles, cycles and/or pedestrians?

!
Warning Any public footpath that crosses or adjoins the site, or is affected, must be shown clearly on the plans. This includes any proposals that may require a closure or diversion.

Select one
* Only for pedestrian access
* Only for vehicle access
* For vehicle and pedestrian access

! Selected both

Would the proposed works affect access to the site for vehicles, cycles, and/or pedestrians?

Select all that apply.
* Addition of a new entrance
* Removal of an entrance
* Improve disabled access
* Dropped kerb and formation of vehicular access

## Parking

Would the proposed works affect car or cycle parking spaces, or both?

Select one
* Only car parking spaces
* Only cycle parking spaces
* Both, car and bike parking spaces

Sub screen

What is the net number of parking spaces available after the works have been completed?

The minimum dimensions for a car parking space are 2.4 x 4.8 metres. These dimensions are for standing space only and do not consider access or turning space.

* Current number of car parking spaces - int
* Total number of car parking spaces after completion - int

What is the net number of parking spaces available after the works have been completed?

* Current number of bike parking spaces - int
* Total number of bike parking spaces after completion - int

Does the proposal involve electrical vehicle (EV) charging points?
* No
* Yes
    * How many new EC charhing points are being added? - int

## Questions 

Do EV charging points only relate to the parking question?

# About the equipment


You need to specify what equipment you are installing.

Select all that apply.
* Satellite dish or antenna
* Air conditioning unit
* Tank

Because your site is in a conservation area, the following equipment installation, replacement or alteration also requires planning permission.

* CCTV
* Security alarm
* Solar panel or other sustainable energy equipment

# End of level boss

How much floor area (GIA) is being added?

Definition

Gross internal area (GIA) is the area of a building. Broadly speaking it includes the whole enclosed area of a building within the external walls taking each floor into account and excluding the thickness of the external walls. Measurement should be in accordance with the RICS Code of Practice.

Specifics on what not to be included and what to be included

* Gross Internal Area - int
* Units - id


# end

OPTIONAL Does the proposal involve the creation of new bedrooms?

Definition

According to the Policy D4 Housing quality and standards of the London Plan for the Greater London area:

A one bedspace single bedroom must have a floor area of at least 7.5 sqm and be at least 2.15m wide.
A two bedspace double (or twin) bedroom must have a floor area of at least 11.5 sqm.

* No
* Yes
    * How many full new single bedrooms are gained? - int
    * How many full new double bedrooms are gained? - int


# Trees!

Notice is required for works to trees that have a trunk diameter of more than 75mm when measured at 1.5m from ground level (or more than 100mm if reducing the number of trees to benefit growth of other trees).
See example
!
Warning It is a criminal offence to prune, fell, damage or harm a protected tree. You must get our permission before carrying out any works to a protected tree, or risk receiving an unlimited fine or criminal conviction.
There is one protected tree in the selected location.

Considering the requirements mentioned above, are there any trees or hedges inside the boundary of the site?

Yes No

Will any trees or hedges need to be removed or pruned in order to carry out your proposal?

There might be trees on land adjacent to your site that could be impacted by the works. A planner will need to visit and assess if you need to submit a tree assessment.
Yes No

Are there any other trees or hedges within 5 metres (5m) from the site boundary to the proposed works?

There might be trees on land adjacent to your site that could be impacted by the works. A planner will need to visit and assess if you need to submit a tree assessment.
Yes No

# Materials

How would you like to describe proposed materials to be used for the works?

Select one.
You define proposed materials on supporting documentation You define existing and proposed materials here. You don’t know yet which materials are going to be used. You will submit an Approval of conditions later on.

Materials 2

What is the proposed roof covering made of?

Select all that apply.
Tiles
Concrete
Slate
Metal
Thatch
Asphalt shingles
Unknown
Other


## Questions

Where does the `Are new windows added?` question live?
