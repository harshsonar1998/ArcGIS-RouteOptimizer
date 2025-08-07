import arcpy


Roads_ND_nd = "Your Road Network path"
Closest_Facility = "Closest Facility"
Closest_Facility__5_ = Closest_Facility
Merged_shp = "Your Facilities Shape FilePath"
Closest_Facility__2_ = Closest_Facility__5_
Export_Output_shp = "Your Incident ShapeFile Path"
Closest_Facility__3_ = Closest_Facility__2_
Solve_Succeeded = "true"

arcpy.MakeClosestFacilityLayer_na(Roads_ND_nd, "Closest Facility", "Minutes", "TRAVEL_TO", "", "1", "Length_mi;Minutes", "ALLOW_UTURNS", "Oneway", "NO_HIERARCHY", "", "TRUE_LINES_WITH_MEASURES", "", "NOT_USED")

arcpy.AddLocations_na(Closest_Facility, "Facilities", Merged_shp, "", "5000 Meters", "", "Roads SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP", "5 Meters", "INCLUDE", "Roads #;Roads_ND_Junctions #")

arcpy.AddLocations_na(Closest_Facility__5_, "Incidents", Export_Output_shp, "Name Name #", "5000 Meters", "", "Roads SHAPE;Roads_ND_Junctions NONE", "MATCH_TO_CLOSEST", "APPEND", "NO_SNAP", "5 Meters", "INCLUDE", "Roads #;Roads_ND_Junctions #")

arcpy.Solve_na(Closest_Facility__2_, "SKIP", "TERMINATE", "", "")

