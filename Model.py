import arcpy

"Your RoadNetwork Name" = "Your Road Network path"
Closest_Facility = "Closest Facility"
Closest_Facility__5_ = Closest_Facility
"Your Exported Facilities ShapeFile Name" = "Your Facilities ShapeFile Path"
Closest_Facility__2_ = Closest_Facility__5_
"Your Exported Incidents ShapeFile Name" = "Your Incident ShapeFile Path"
Closest_Facility__3_ = Closest_Facility__2_
Solve_Succeeded = "true"

arcpy.MakeClosestFacilityLayer_na(""Your Road Network file name)_nd, "Closest Facility", "Minutes", "TRAVEL_TO", "", "1", "Length_mi;Minutes", "ALLOW_UTURNS", "Oneway", "NO_HIERARCHY", "", "TRUE_LINES_WITH_MEASURES", "", "NOT_USED")

arcpy.AddLocations_na(Closest_Facility, "Facilities", "Your Exported Facilities ShapeFile name" , "", "5000 Meters", "", "Roads SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP", "5 Meters", "INCLUDE", "Roads #;Roads_ND_Junctions #")

arcpy.AddLocations_na(Closest_Facility__5_, "Incidents", "Your Exported Incidents ShapeFile name" , "Name Name #", "5000 Meters", "", "Roads SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP", "5 Meters", "INCLUDE", "Roads #;Roads_ND_Junctions #")

arcpy.Solve_na(Closest_Facility__2_, "SKIP", "TERMINATE", "", "")

#To Run the Model
execfile("Model File Path")
