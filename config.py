settings = {

    "aoifile": "https://gdh-data.ams3.digitaloceanspaces.com/boundaries/Jekyll-Island.geojson",
    "systems": ["URB", "IND", "FOR", "HYDRO","AG"],
    "outputdirectory": "output",
    "workingdirectory": "working",
    "nlcddata": "NLCD.zip",
}


processchains = {
    "URB": {
        "red": [22, 23, 24],
        "yellow": [41,42,43, 90,95,11, 12],
        "green": [21, 31, 51, 52,71,72,73,74,81,82 ]
    },
    "AG": {
        "red": [81,82],
        "yellow": [11,12,21,22,23,24,31,90,95],
        "green": [41,42,43,51,52,71,72,73,74]  
    },
    
    "IND": {
        "red": [24,23],
        "yellow": [11,12,81,82,90,95],
        "green": [21,22,31,41,42,43,51,52,71,72,73,74] 
    },
    
    "FOR": {
        "red": [41,42,43],
        "yellow": [11,12,21,22,23,24],
        "green": [51,52,71,72,73,74,81,82,90,95] 
    },
    
    "HYDRO": {
        "red": [11,12],
        "yellow": [21,22,23,24,31,41,42,43,51,52],
        "green": [71,72,73,81,82,90,95] 
    },
    

}
