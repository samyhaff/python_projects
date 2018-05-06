import objc

class ETMouse():    
    def setMousePosition(self, x, y):
        bndl = objc.loadBundle('CoreGraphics', globals(), 
                '/System/Library/Frameworks/ApplicationServices.framework')
        objc.loadBundleFunctions(bndl, globals(), 
                [('CGWarpMouseCursorPosition', 'v{CGPoint=ff}')])
        CGWarpMouseCursorPosition((x, y))

if __name__ == "__main__":
    et = ETMouse()
    et.setMousePosition(200, 200)
