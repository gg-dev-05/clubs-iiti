import yaml

''' 
img object initialize 
img stores links to all hosted images on https://imgur.com/
'''
img = yaml.load(open('images.yaml'), Loader=yaml.FullLoader)