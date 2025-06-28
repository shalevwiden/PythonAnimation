import os

'''
Running this file deletes all images in "imagesfolder"
'''
imagesfolder='/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images'


def deleteallimagesinimagefolder(imagefolderpath):
    images=os.listdir(imagefolderpath)
    
    delcount=0
    for image in images:
        fullpath=f'{imagefolderpath}/{image}'
        
        try:
            os.remove(fullpath)
            delcount += 1
        except PermissionError:
            print(f"Permission denied: {fullpath}")
        except Exception as e:
            print(f"Failed to delete {fullpath}: {e}")


    print(f'Ran deletedallimagesinimagefolder.\n{delcount} images were deleted.')

def main():
    deleteallimagesinimagefolder(imagefolderpath=imagesfolder)

if __name__=='__main__':
    main()
