import requests



# url = "https://api.endlessmedical.com/v1/dx/"


# terms = requests.get(url + "InitSession")


# print(terms.json())
##############################################################

url = "https://api.endlessmedical.com/v1/dx/"

querystring = {"SessionID":"sprU96mC4wCdjEAN","passphrase": "I have read, understood and I accept and agree to comply with the Terms of Use of EndlessMedicalAPI and Endless Medical services. The Terms of Use are available on endlessmedical.com"}



terms = requests.post(url + "AcceptTermsOfUse", params = querystring)


# response = requests.post(url, params=querystring)
print(terms)

########################################################################


list_of_features = ["Age", "Temp", "PMHXAsthma", "LossOfSmell", "Contacts", "NewFoods"]
list_of_values = [19, 104, 3, 3, 3, 3]

for x in range(len(list_of_features)) :
    querystring = {"name":list_of_features[x],"value":list_of_values[x],"SessionID":"sprU96mC4wCdjEAN"}
    features = requests.post(url + "UpdateFeature", params=querystring)
    print(features.json())

###########################################################################
url = "https://api.endlessmedical.com/v1/dx/"

querystring = {"SessionID":"sprU96mC4wCdjEAN"}



result = requests.get(url + "Analyze", params = querystring)
print(result.json())


###############################################################
###############################################################
###############################################################
###############################################################

import requests

# url = "https://api.endlessmedical.com/v1/dx/"


# terms = requests.get(url + "InitSession")


# print(terms.json())
##############################################################

url = "https://api.endlessmedical.com/v1/dx/"

querystring = {"SessionID":"sxQUdwAkOLTbgPVC","passphrase": "I have read, understood and I accept and agree to comply with the Terms of Use of EndlessMedicalAPI and Endless Medical services. The Terms of Use are available on endlessmedical.com"}



terms = requests.post(url + "AcceptTermsOfUse", params = querystring)


# response = requests.post(url, params=querystring)
print(terms)

########################################################################


list_of_features = ["Age", "Arrest", "ArrhythmiaSymptomsChestPains", "BoneLocPain"]
list_of_values = [82, 2, 4, 3]

for x in range(len(list_of_features)) :
    querystring = {"name":list_of_features[x],"value":list_of_values[x],"SessionID":"sxQUdwAkOLTbgPVC"}
    features = requests.post(url + "UpdateFeature", params=querystring)
    print(features.json())

###########################################################################
url = "https://api.endlessmedical.com/v1/dx/"

querystring = {"SessionID":"sxQUdwAkOLTbgPVC"}



result = requests.get(url + "Analyze", params = querystring)
print(result.json())