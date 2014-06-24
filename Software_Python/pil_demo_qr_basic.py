import Image
import ImageEnhance
import ImageOps

# More detail on PIL, please visit
# http://effbot.org/imagingbook/image.htm
# Allan K Liu

class panel:
    def __init__(self,width=172,height=72,color="L",bpp=2,scan="v",endian="msb"):
        width = width
        height = self.height
        color = self.color
        bpp = self.bpp
        scan = self.scan
        endian = self.endian

    def getRatio(self):
        ratio = float(self.width)/float(self.height)
        return ratio

def loadPanelParas():
    pass
    
def readRawImage():
    pass
    
def rotate(img):
    pass
def resize(img):
    pass
def move(img):
    pass
def crop(img):
    pass
def enhance(img):
    pass
def merge(img):
    pass
def codeGen(img):
    pass

   
def printscreen(img):
    iml = list(img.getdata())
    
    for i in range(len(iml)):
        val = iml[i]
        print "%02X"%val,
    print
    
def printscreen(img,x,y):
    iml = list(img.getdata())
    
    for i in range(y):
        for j in range(x):
            print "%02X"%(ol[j+i*x]),
        print
'''
    main loop: 
        read panel params, 
        read raw image for dimension, histogram(dynamic range), 
        enhance(contract), rotate, resize, crop, merge
        save it as *.bin file, with codegen in different coding style (c.*.asm)
'''    
def main():
    
    bin = []
    
    im = Image.open("merged-172x72-rotate.png")
    
    panel = panel.Panel(172,72,"L",2,"v","msb")
    
    #print im.format, im.size, im.mode
    # Save it as a temp BMP file
    # and invoke system default image viewer to show it 
    #im.show()

    (x,y) = im.size
    ratio2 = float(x)/float(y)
    ratio3 = float(y)/float(x)
    #print ratio2
    #print ratio3

    
    dither =im.convert(mode='P', dither=Image.FLOYDSTEINBERG)
    #dither.show()
    
    di = dither.convert('L')
    bw = ImageOps.mirror(di)
    #bw.show()
    (b,p) = bw.getextrema()
    print "B&W image ranges : %02X - %02X"%(b,p)
    
    bw.point(lambda i: (0xFF-i)&0xC0).show()
    
    #enh = ImageEnhance.Contrast(bpp2)
    #enh.enhance(2).show()
    
    (x,y)=bw.size
    ol =  list(bw.getdata())
    #print "x=%d,y=%d,len=%d"%(x,y,len(ol))
    
    print ">> co-ordinate"
    for i in range(y):
        for j in range(x):
            print "%02X%02x"%(i,j),
        print ""
     
    print ">> value"
    for i in range(y):
        for k in range(x):
            print "%02X"%(ol[k+i*72]),
        print ""
    '''    
    '''
    print ">> array"
    for i in range(len(ol)):
        #print "%02X"%(ol[i]>>5),
        print "%02X"%(ol[i]),
    
    for i in range(len(ol)/4):
        val0= ol[i*4]&0xC0
        val1= (ol[i*4+1]&0xC0)>>2
        val2= (ol[i*4+2]&0xC0)>>4
        val3= (ol[i*4+3]&0xC0)>>6
        val = val0+val1+val2+val3
        #print "%02X=%02X:%02X:%02X:%02X(%02X:%02X:%02X:%02X)"%(val,val0,val1,val2,val3,ol[i],ol[i+1],ol[i+2],ol[i+3])
        bin.append(val)
        
    #print "len=%d"%(len(bin))
    
    '''
    for i in range(len(bin)):
        print "%02X"%(bin[i]),
    '''
    
    #for i in range(len(bin)):
    for i in range(172):
        for j in range(18):
            #print "0x%02X:(%02X,%02X,%02X),"%(bin[j+i*18],i,j,j+i*18),
            print "0x%02X,"%(bin[j+i*18]),
        print
    
        
    
if __name__=='__main__' :main()
