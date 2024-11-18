from PIL import Image


def main():
    im1 = Image.open("im1.jpg")
    im2 = Image.open("im2.jpg")
    im3 = Image.open("im3.jpg")
    im4 = Image.open("im4.jpg")
    im5 = Image.open("im5.jpg")
    im6 = Image.open("im6.jpg")
    # im1.show()
    # im_px = im1.load()
    print("im1:")
    layer(im1)
    print("im2:")
    layer(im2)
    print("im3:")
    layer(im3)
    print("im4:")
    layer(im4)
    print("im5:")
    layer(im5)
    print("im6:")
    layer(im6)



def layer(im):
    fourThrd, zeroThrd, threeThrd, oneThrd, twoThrd, start4two, start4three = 0,0,0,0,0,0,0
    oneThrd = (int)(im.size[1]/3)
    twoThrd = (int)(im.size[1]*2/3)
    threeThrd = (int)(im.size[1])
    # size that all thirds should equal, achieved by adding/subtracting to where the bottom of the picture is held
    sizeForAll = oneThrd - zeroThrd
    # print("Size: ", sizeForAll)
    # print(zeroThrd, " ", oneThrd, " ", twoThrd, " ", threeThrd)
    # zeroThrd = addToVarTillReachNumber(oneThrd, zeroThrd, sizeForAll, True)
    # oneThrd = addToVarTillReachNumber(oneThrd, zeroThrd, sizeForAll)
    blueIm = im.crop((30, zeroThrd + 30, im.size[0] - 30, oneThrd + 30))
    redIm = im.crop((30, twoThrd + 30, im.size[0] - 30, threeThrd + 30))
    greenIm = im.crop((30, oneThrd + 30, im.size[0] - 30, twoThrd + 30))
    #image alignment process:

    middleofblueX = blueIm.size[0] / 2

    middleofblueY = blueIm.size[1] / 2
    twoThrd = addToVarTillReachNumber(twoThrd, oneThrd, sizeForAll, False)
    threeThrd = addToVarTillReachNumber(threeThrd, twoThrd, sizeForAll, False)
    blueOffsetX, blueOffsetY = align(greenIm, blueIm, greenIm.size[0]/2, greenIm.size[1]/2)
    redOffsetX, redOffsetY = align(greenIm, redIm, greenIm.size[0]/2, greenIm.size[1]/2)
    print("blue offset x: ", blueOffsetX, " blue offset y: ", blueOffsetY, " red offset x: ", redOffsetX, " red offset y: ", redOffsetY)
    blueIm = im.crop((30 + blueOffsetX, 30 + blueOffsetY, im.size[0] + blueOffsetX - 30, oneThrd + blueOffsetY + 30))
    redIm = im.crop((30 + redOffsetX, 30 + twoThrd + redOffsetY, im.size[0] + redOffsetX + -30, 30 + threeThrd + redOffsetY))
    # print("red: ", redIm.size, " green: ", greenIm.size, " blue: ", blueIm.size)
    # blueIm.show()
    # greenIm.show()
    # redIm.show()
    merged = Image.merge("RGB", (redIm, greenIm, blueIm))
    finalMerged = merged.crop((0, 0, merged.size[0], merged.size[1] - 50))
    finalMerged.show()

#middleX & Y are middle of the first (blue) image
def align(blueIm, compareToIm, middleX, middleY):
    scoreIndv = 0
    qx = int(blueIm.size[0]/4)
    qy = int(blueIm.size[1]/4)
    blueIm_px = blueIm.load()
    compareToIm_px = compareToIm.load()
    #total score for one offset
    scoreTotal = 0
    #the score of each offset as it is at its index
    offsetScores = []
    # return lowest scored offset combo
    lowestScore = 100000000000000000
    offsetIndex = 0
    #indexes to return
    lowestX = 0
    lowestY = 0
    for offsetX in range(-25,25):
        for offsetY in range(-25,25):
            scoreTotal = 0
            for i in range(-25, 25):
                for j in range(-25,25):
                    #score for individual pixel
                    xCompareto = middleX + i + offsetX
                    yCompareto = middleY + j + offsetY
                    xBlue = middleX + i
                    yBlue = middleY + j
                    # print(middleY)
                    # print(xCompareto, " y: ", yCompareto)
                    # if xBlue <= blueIm.size[0] and xCompareto <= blueIm.size[0] and yBlue <= blueIm.size[1] and yCompareto <= blueIm.size[1]:
                    scoreIndv = (blueIm_px[xBlue,yBlue] - compareToIm_px[xCompareto,yCompareto]) ** 2
                    scoreTotal += scoreIndv
                        #set the score for the index of the offset you are scoring
            # print(offsetX + 25, " dfsa: ", offsetY + 25)
            # print("score total: ", scoreTotal)
            if scoreTotal < lowestScore:
                lowestX = offsetX
                lowestY = offsetY
                lowestScore = scoreTotal
            # print("lowestX, ", lowestX, " lowestY, ", lowestY)
    if not lowestScore > 10000000000000000:
        return lowestX, lowestY
    else:
        return 0, 0




def addToVarTillReachNumber(bottom, top, number, firstSquare):
    number = abs(number)
    while not abs(bottom - top) == number:
        if abs(bottom - top) < number:
            if firstSquare:
                bottom -= 1
            else:
                bottom += 1
        if abs(bottom - top) > number:
            if firstSquare:
                bottom += 1
            else:
                bottom -= 1
        # print(abs(bottom-top))
    return bottom


main()
