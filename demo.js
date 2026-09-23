db.cars.aggregate([
    {$match:{maker:"Hyundai"}},
    {$project:{
        _id:0,
        carname:{"$toUpper":{$concat:[
            "$maker", " ", "$model"
        ]}}
    }},
    {$out:"hyundaiCar"}
])