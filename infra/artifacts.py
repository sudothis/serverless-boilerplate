from resources.stack import Stack
from troposphere import Template

def main():
    artifact_stack = Stack('ArtifactStack')
    artifact_stack.build()

main()