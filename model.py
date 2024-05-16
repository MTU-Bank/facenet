from PIL import Image
from facenet_pytorch import MTCNN, InceptionResnetV1

__version__ = '0.0.1'

mtcnn = MTCNN()
resnet = InceptionResnetV1(pretrained='vggface2').eval()

def get_predict(data: list):
    path_img1, path_img2 = data
    img1 = Image.open(path_img1)
    img2 = Image.open(path_img2)
    face1, _ = mtcnn.detect(img1)
    face2, _ = mtcnn.detect(img2)

    if face1 is None or face2 is None:
        result = {'result': 'No face detected'}
        return result
    else:
        aligned1 = mtcnn(img1).unsqueeze(0)
        aligned2 = mtcnn(img2).unsqueeze(0)
        embeddings1 = resnet(aligned1).detach()
        embeddings2 = resnet(aligned2).detach()

        distance = (embeddings1 - embeddings2).norm().item()

        match = distance < 0.8
        result = {'result': match, 'distance': distance}

        return result

# print(get_predict(['static/slf1.jpg', 'static/slf2.jpg']))