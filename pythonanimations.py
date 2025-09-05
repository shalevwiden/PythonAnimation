import os
import webbrowser
import time
import subprocess

from matplotlib import pyplot as plt

from deleteimages_inimagesfolder import deleteallimagesinimagefolder


# do this tmr

# set the amount of colors for the amount of arguments too
# do this for the stock visualizations script too
# make line, bar, and pie charts too. 
colors = ['gold', 'skyblue', 'lightcoral', 'mediumseagreen']


def animateinsafari(folderpath,delaysecs):

    listofitems=os.listdir(folderpath)
    listofitems=[item for item in listofitems if ".ds" not in item.lower()]
    # sort them to open properly. They must be named "chart(num)" for this to work
    # they are named that later on.
    listofitems=sorted(listofitems,key=lambda x:int(os.path.splitext(x)[0].replace('chart','')))

    lengthofanimation=delaysecs*len(listofitems)
    for image in listofitems:
        # find a better way to show than webbrowser.open although that could also work.
        # need to use the file extension: file://
        fullpath=f'file://{folderpath}/{image}'        
        print(fullpath)

        # thats wierd it was opening preview
        subprocess.run(["open", "-a", "Safari", fullpath])
        time.sleep(delaysecs)
        # close preview 5 seconds after the animation 
    time.sleep(5)
    print(f'The animation concluded and lasted {lengthofanimation}')

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



# animateinsafari(graphspath)

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

# print(getsymmetricaldata_andcolors(11))

def getcolors():
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
    return colors

def get_similar_colors(colorhex,steps):
    '''
    This returns 20 of a color, but starting very dark and getting slightly ligther. 
    The more steps there are, the more subtle the color change. 
    '''
    colorhex = colorhex.lstrip("#")

    # Convert to RGB (0–255)
    r, g, b = tuple(int(colorhex[i:i+2], 16) for i in (0, 2, 4))

    colorlist = []
    for i in range(steps):
        # Factor goes from 1.0 (original) up to 0.0 (white)
        factor = 1 - (i / steps)
        new_r = int(r + (255 - r) * (1 - factor))
        new_g = int(g + (255 - g) * (1 - factor))
        new_b = int(b + (255 - b) * (1 - factor))

        colorlist.append(f"#{new_r:02X}{new_g:02X}{new_b:02X}")

    return colorlist

def get_alternating_colors(base_color, steps=12, delta=20):
    """
    Generate colors cycling every 3:
    - lighter version of base
    - darker version of base
    - the base color itself
    """
    base_color = base_color.lstrip("#")
    r, g, b = tuple(int(base_color[i:i+2], 16) for i in (0, 2, 4))

    color_list = []
    for i in range(steps):
        mode = i % 3  # 0=lighter, 1=darker, 2=base

        if mode == 0:  # lighter
            new_r = min(255, r + delta * (i // 3))
            new_g = min(255, g + delta * (i // 3))
            new_b = min(255, b + delta * (i // 3))

        elif mode == 1:  # darker
            new_r = max(0, r - delta * (i // 3))
            new_g = max(0, g - delta * (i // 3))
            new_b = max(0, b - delta * (i // 3))

        else:  # base
            new_r, new_g, new_b = r, g, b

        color_list.append(f"#{new_r:02X}{new_g:02X}{new_b:02X}")

    return color_list

def get_data(num):
    datasizes=[]
    for i in range(1,num+1):
        datasizes.append(1/(num))
    return datasizes

def getfibbonacidata(num):
    '''
    I can do this actually with a loop or with recursive
    '''
    pass




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

    Rotate val will affect how many degrees each chart changes from one to the next
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

        
        chartfile=f'chart{chart}.png'
        savepath=os.path.join(imagesfolder,chartfile)
        plt.savefig(savepath)
        subprocess.run(["xattr", "-c", savepath])


        # make it rounded for formatting
        figx*=(1+scaleval)
        figx=round(figx,2)
        figy*=(1+scaleval)
        figy=round(figy,2)
        
        testing=True
        if testing:
            print(f'Saved {imagesfolder}/chart{chart}.png\nWith figx{figx} and figy{figy}\n\
                  and startangle of {degreeslist[chart]}\n')
            
    subprocess.run([
        "xattr",
        "-cr",
        "/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images"
    ])

def makesamecolorcharts(chartdata, chartcolors,chartcount,pie_initialdegrees,sectors,pie_rotateval=10, scaleval=1,legend=True):
    """
    This makes and saves the images to a folder specified in the function, images folder.
    The function could be changed to take the folder as argument. 
    """

    styles=['fivethirtyeight','ggplot']
    plt.style.use(styles[1])
    imagesfolder='/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images'

    # this is the data in EACH pie chart. 
    degreeslist=mapdegrees(initialdegrees=pie_initialdegrees,rotateval=pie_rotateval,count=chartcount)

    sorteddegrees=True
    if sorteddegrees:
        degreeslist=sorted(degreeslist)
    print(f'len:{len(degreeslist)}')
    figx, figy=9,6
    # chart is the chartindex
    fullstring='Thanks for watching                      '
    fullstring += ''.join([' text ' if i % 2 == 0 else 'animationssss' for i in range(chartcount-len(fullstring))])
    title=""
    for chart in range(chartcount):
        
        plt.close()
        plt.figure(figsize=(figx,figy))
        
        if chart>50:
            chartcolors=get_similar_colors("#045656",steps=sectors)
        newangle= -(int(degreeslist[chart]))
        plt.pie(chartdata,colors=chartcolors,startangle=newangle)
        plt.title(title)
        


        breaknum=len(fullstring)
        if breaknum>chart+1:
            title+=fullstring[chart]
        else:
            title=fullstring[1:]


        

        plt.axis('equal')

        if legend:
            plt.legend(loc='lower right',bbox_to_anchor=(1.1, -0.1))

        chartfile=f'chart{chart}.png'
        savepath=os.path.join(imagesfolder,chartfile)
        plt.savefig(savepath)


        # make it rounded for formatting
        figx*=scaleval
        figx=round(figx,2)
        figy*=scaleval
        figy=round(figy,2)
        
        testing=True
        if testing:
            print(f'Saved {imagesfolder}/chart{chart}.png\nWith figx{figx} and figy{figy}\n\
                  and startangle of {degreeslist[chart]}\n')
        
    subprocess.run([
        "xattr",
        "-cr",
        "/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images"
    ])




imagesfolder='/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images'


def makebarchart():
    pass


def makecharts():

    print('Making Dynamic Pie Charts now:')

    # the data is whats important for determining the colors
    sectors=4
    datalist=get_data(sectors)
    colors=get_similar_colors("#0A0A17",steps=sectors)
    # colors=get_alternating_colors("#3D3B9A",steps=sectors)

    # colors=sorted(colors,reverse=True)
    deleteallimagesinimagefolder(imagefolderpath=imagesfolder)

    makesamecolorcharts(chartdata=datalist,chartcolors=colors,pie_initialdegrees=180,chartcount=100,sectors=sectors)
    # makedynamicpiecharts(chartdata=datalist,chartcolors=getcolors(),chartcount=40,pie_initialdegrees=0,pie_rotateval=30)
    #


    print(os.getcwd())
    time.sleep(2)

makecharts()

def run():
    

    animateinsafari(imagesfolder,delaysecs=.1)
    # print(f'Animate in chrome\n {animateinchrome(folderpath='/Users/shalevwiden/Downloads/Coding_Files/Python/BeautifulSoup_Library/python_animation/images',delaysecs=.1)}')

# run()