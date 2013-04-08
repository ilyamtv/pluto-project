import os, random, glob
from django.conf import settings

def beauty_upload_to(path, filename):
    directory = os.path.join(settings.MEDIA_ROOT, path)
    ext = filename.split('.')[-1]
    filename = str(random.randrange(1000, 9999))
    while glob.glob(os.path.join(directory, filename) + '.*'):
        filename = filename + "_" + str(random.randrange(1000, 9999))

    return os.path.join(path, filename + '.' + ext)