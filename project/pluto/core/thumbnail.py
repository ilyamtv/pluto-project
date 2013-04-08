import os
from sorl.thumbnail.conf import settings
from sorl.thumbnail.helpers import serialize, tokey
from sorl.thumbnail.base import ThumbnailBackend, EXTENSIONS


class BeautyThumbnailBackend(ThumbnailBackend):

    def _get_thumbnail_filename(self, source, geometry_string, options):
        """
        Computes the destination filename.
        """
        key = tokey(serialize(options))
        image_path = os.path.relpath(source.url, source.storage.location)
        path = '%s-%s-%s' % (os.path.splitext(image_path)[0], geometry_string, key)
        return '%s%s.%s' % (settings.THUMBNAIL_PREFIX, path, EXTENSIONS[options['format']])