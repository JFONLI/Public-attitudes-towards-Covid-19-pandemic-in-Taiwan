import json


dictObj = {
	'andy':{
		'age': 23,
		'city': 'shanghai',
		'skill': 'python'
	},
	'william': {
		'age': 33,
		'city': 'hangzhou',
		'skill': 'js'
	}
}


jsObj = json.dumps(dictObj)
 
fileObject = open('jsonFile.json', 'w')
fileObject.write(jsObj)
fileObject.close()


dictObj = {
	'andy':{
		'age': 23,
		'city': 'shanghai',
		'skill': 'python'
	},
	'william': {
		'age': 33,
		'city': 'hangzhou',
		'skill': 'js'
	},
    'jerry': {
        'age': 22,
        'city': 'Taipei',
        'skill': 'None'
    }
    
}

jsObj = json.dumps(dictObj)
 
fileObject = open('jsonFile.json', 'w')
fileObject.write(jsObj)
fileObject.close()
