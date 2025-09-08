from dotenv import load_dotenv
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient   #pip install azure-ai-vision-imageanalysis
from azure.core.credentials import AzureKeyCredential           #pip install azure-core
from azure.ai.vision.imageanalysis.models import VisualFeatures
from PIL import Image, ImageDraw, ImageFont

load_dotenv()

AI_SERVICE_ENDPOINT=os.getenv("AI_SERVICE_ENDPOINT")
AI_SERVICE_API_KEY=os.getenv("AI_SERVICE_API_KEY")

print(AI_SERVICE_ENDPOINT, AI_SERVICE_API_KEY)

credential = AzureKeyCredential(AI_SERVICE_API_KEY)

client = ImageAnalysisClient(endpoint=AI_SERVICE_ENDPOINT,
                             credential=credential)

def get_image_info():
    file_path = input("Enter the path to the image file: ")

    with open(file_path,"rb") as image_file:
        image_data = image_file.read()

    result = client.analyze(
                image_data=image_data,
                visual_features=[
                    VisualFeatures.TAGS,
                    VisualFeatures.CAPTION,
                    VisualFeatures.OBJECTS
                ],
                model_version="latest"
            )

    # caption를 출력하는 부분
    if result.caption is not None:
        print(" Caption: ")
        print(f"    '{result.caption.text}, confidence: {result.caption.confidence:.4f}")


    # tag를 출력하는 부분
    if result.tags is not None:
        print(" Tags: ")
        for tag in result.tags.list:
            print(f"    '{tag.name}, confidence: {tag.confidence:.4f}")

    # Object Detection
    if result.objects is not None:
        print(" Objects:")
        bounding_boxes =[]

        for obj in result.objects.list:
            print(f"    '{obj.tags[0].name},{obj.bounding_box}, confidence: {tag.confidence:.4f}")
            bounding_boxes.append(obj.bounding_box)

    draw_bounding_boxes(file_path, bounding_boxes)

def draw_bounding_boxes(image_path, bounding_boxes):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    for box in bounding_boxes:
        x = box['x']
        y = box['y']
        w = box['w']
        h = box['h']

        draw.rectangle(((x,y),(x+w,y+h)),outline="red", width=2)
        draw.text((x,y),"Object",fill="red")
    image.show()


if __name__=="__main__":
    get_image_info()