#!/usr/bin/env python
from samplebase import SampleBase



class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            for x in range(0, 11):
                offset_canvas.SetPixel(x, 0, 255, 0, 255)
                offset_canvas.SetPixel(0, x, 255, 0, 255)
               
            for x in range(0, 12):
                
                offset_canvas.SetPixel(x, 11, 255, 0, 255)
                offset_canvas.SetPixel(11, x, 255, 0, 255)
        
            offset_canvas.SetPixel(int(input("row")), int(input("col")), 255, 0, 0)
            


            
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
            


# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()
