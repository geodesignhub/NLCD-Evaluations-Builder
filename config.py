settings = {

    "aoifile": "minn-sa.geojson",
    "systems": ["URB","AG","IND","FOR","HYDRO","EI","LDH","MIX"],
    "outputdirectory": "output",
    "workingdirectory": "working",
    "nlcddata": "working.zip",
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
    "GI": {
        "red": [11,12,41,42,43],
        "yellow": [11,12,23,24],
        "green": [21,22,31,51,52,71,72,73,74,81,90,95] 
    },
        
    "EI": {
        "red": [],
        "yellow": [11,12,23,42,43,41,31,81,82,90,95,24,51,52,71,72,73,74],
        "green": [21,22]
    },
    "LDH": {
        "red": [22],
        "yellow": [41,42,43,31,11,12,23,24,73,74,90,95,82],
        "green": [51,71,72,82,52,81,90,95]
    },
    "MIX": {
        "red": [23],
        "yellow": [11,12,42,73,74,81,82,90,95],
        "green": [21,22,24,31,41,43,51,52,71,72,]
    }
}
