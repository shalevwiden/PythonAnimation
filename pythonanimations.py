import os
import webbrowser
import time
import subprocess

from matplotlib import pyplot as plt

# do this tmr

# set the amount of colors for the amount of arguments too
# do this for the stock visualizations script too
# make line, bar, and pie charts too. 
colors = ['gold', 'skyblue', 'lightcoral', 'mediumseagreen']


def animateinpreview(folderpath,delaysecs):

    listofitems=os.listdir(folderpath)
    # sort them. They must be named "chart(num)" for this to work
    # they are named that later on.
    listofitems=sorted(listofitems,key=lambda x:int(os.path.splitext(x)[0].replace('chart','')))

    lengthofanimation=delaysecs*len(listofitems)
    for image in listofitems:
        # find a better way to show than webbrowser.open although that could also work.
        # need to use the file extension: file://
        fullpath=f'file://{folderpath}/{image}'        
        print(fullpath)

        # thats wierd it was opening preview
        webbrowser.open_new_tab(fullpath)
        time.sleep(delaysecs)
        # close preview 5 seconds after the animation 
    time.sleep(5)
    print(f'The animation concluded and lasted {lengthofanimation}')
    subprocess.run(['osascript', '-e','quit app "Preview"'])

def animateinchrome(folderpath,delaysecs):

    listofitems=os.listdir(folderpath)
    # sort them. They must be named "chart(num)" for this to work
    listofitems=sorted(listofitems,key=lambda x:int(os.path.splitext(x)[0].replace('chart','')))
    lengthofanimation=delaysecs*len(listofitems)
    print(f'List of the images is:\n{listofitems}')
    for image in listofitems:
        # find a better way to show than webbrowser.open although that could also work.
        # need to use the file extension: file://
        fullpath=f'file://{folderpath}/{image}'        
        print(fullpath)

        subprocess.run(['open', '-a', 'Google Chrome', fullpath])
        time.sleep(delaysecs)
        # close preview 5 seconds after the animation 
    time.sleep(5)
    print(f'The animation concluded and lasted {lengthofanimation} seconds')



# animateinpreview(graphspath)

def getsymmetricaldata_andcolors(num):
    datasizes=[]
    colors=[
    "#0B1F4B",  # Dark navy blue
    "#123D6B",  # Deep blue
    "#1A5C8C",  # Strong blue
    "#2A7CA6",  # Medium blue
    "#3A9DC0",  # Sky blue with teal
    "#4AC0D9",  # Light cyan
    "#68D3C8",  # Soft turquoise
    "#8CDCB0",  # Pale seafoam
    "#B0E49B",  # Muted minty green
    "#D3DD87",  # Pale yellow-green
    "#EFC373",  # Soft warm tan-orange
]
    for i in range(num):
        datasizes.append(1/(num))
    return datasizes,colors
print(getsymmetricaldata_andcolors(11))

def getdynamicdata_andcolors(num):
    datasizes=[]
    colors=[
    "#0B1F4B",  # Dark navy blue
    "#123D6B",  # Deep blue
    "#1A5C8C",  # Strong blue
    "#2A7CA6",  # Medium blue
    "#3A9DC0",  # Sky blue with teal
    "#4AC0D9",  # Light cyan
    "#68D3C8",  # Soft turquoise
    "#8CDCB0",  # Pale seafoam
    "#B0E49B",  # Muted minty green
    "#D3DD87",  # Pale yellow-green
    "#EFC373",  # Soft warm tan-orange
]
    for i in range(1,num+1):
        datasizes.append(1/(i))
    return datasizes,colors
    # make data where one datapoint has 1/2, the next 1/3, etc

def getfibbonacidata(num):
    pass

print(getdynamicdata_andcolors(11))



def mapdegrees(initialdegrees, rotateval,count):
    '''
    returns degreeslist
    '''
    currentdegrees=initialdegrees
    totalrotations=0
    degreeslist=[]
    for i in range(count):
        if i>=1:
            # this works to do it by loop
            currentdegrees+=rotateval
            # print(f'currentdegrees"{currentdegrees}rotateval={rotateval}')

            
            rotationiteration=currentdegrees//360
            currentdegrees-=(360*rotationiteration)

            # track total rotations around the circle

            if currentdegrees==initialdegrees:
                totalrotations+=1
            degreeslist.append(currentdegrees)
            # add equation to control the changing of the rotateval
        # elif initialdegrees!=0:
        else:
            rotationiteration=currentdegrees//360
            degreeslist.append(currentdegrees)
    return degreeslist
            


def makedynamicpiecharts(chartdata, chartcolors,chartcount,pie_initialdegrees,pie_rotateval=20, scaleval=.01,legend=False):
    """
    This makes and saves the images to a folder specified in the function, images folder.
    The function could be changed to take the folder as argument. 
    """
    styles=['fivethirtyeight','ggplot']
    plt.style.use(styles[1])
    imagesfolder='/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images'

    # this is the data in EACH pie chart. 
    degreeslist=mapdegrees(initialdegrees=pie_initialdegrees,rotateval=pie_rotateval,count=chartcount)
    print(f'len:{len(degreeslist)}')
    figx, figy=9,6
    # chart is the chartindex
    for chart in range(chartcount):
        
        plt.figure(figsize=(figx,figy))

        plt.pie(chartdata,colors=chartcolors,startangle=degreeslist[chart])
        plt.title("Pie Animation")
        plt.axis('equal')

        if legend:
            plt.legend(loc='lower right',bbox_to_anchor=(1.1, -0.1))

        plt.savefig(f'{imagesfolder}/chart{chart}.png')

        # make it rounded for formatting
        figx*=(1+scaleval)
        figx=round(figx,2)
        figy*=(1+scaleval)
        figy=round(figy,2)
        
        testing=True
        if testing:
            print(f'Saved {imagesfolder}/chart{chart}.png\nWith figx{figx} and figy{figy}\n\
                  and startangle of {degreeslist[chart]}\n')
    





imagesfolder='/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images'


def makebarchart():
    pass


def main():

    print('Making Dynamic Pie Charts now:')

    datalist, colorlist=getdynamicdata_andcolors(11)
    makedynamicpiecharts(chartdata=datalist,chartcolors=colorlist,chartcount=40,pie_initialdegrees=0,pie_rotateval=30)
    # animateinpreview(imagesfolder,delaysecs=.5)

    print(f'Animate in chrome\n {animateinchrome(folderpath='/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images',delaysecs=.1)}')

    print(os.getcwd())
# if __name__=='__main__':
#     main()

