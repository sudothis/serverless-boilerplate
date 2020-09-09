from troposphere.s3 import Bucket as S3Bucket

class Bucket:
    def __init__(self, identifier):
        self._identifier = identifier

    def build(self):
        print('Building')
    

