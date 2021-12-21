from typing import Generator, Optional, List, Tuple
from os import path


class ProjectImgs:
    def __init__(self, id: str, img_root: str, images: List[Tuple[str, str]]) -> None:
        self.id = id
        self.img_root = img_root
        self.images = images

    def get_images(self) -> Generator[int, str, str]:
        for i, (img_filename, image_description) in enumerate(self.images):
            yield i, path.join('static', 'images', self.img_root, img_filename), image_description


class Project:
    def __init__(self, name: str, description: str, context: str, 
                 git_link: Optional[str] = None, site_link: Optional[str] = None, images: Optional[ProjectImgs] = None) -> None:
        self.name = name
        self.description = description
        self.context = context
        
        self.git_link = git_link
        self.site_link = site_link

        self.images = images
