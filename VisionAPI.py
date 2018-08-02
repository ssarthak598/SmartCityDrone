import requests, json, os
import urllib2
import urllib

subscription_key = "*******"
vision_url = "https://*.api.cognitive.microsoft.com/vision/v1.0/an$

camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.rotation = 90

image_name = "image.jpg"
headers    = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "a$
params     = {'visualFeatures': 'Categories,Description,Color'}

while True :

        raw_input("Press any key to take a picture")

        camera.capture(image_name)
        print "image taken"
        image_data = open(image_name, "rb").read()
        response   = requests.post(vision_url, headers=headers, params=params, $
        analysis   = response.json()

        image_caption = analysis["description"]["captions"][0]["text"].capitali$
        tags = "<title>" + image_caption + "</title>"
        query_args = { 'q':tags}
        encoded_args = urllib.urlencode(query_args)
        urlx = URi + enco$
        resp = urllib2.urlopen(urlx).read()
        print image_caption
