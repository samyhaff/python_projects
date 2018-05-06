import sys
import os
 
# Print iterations progress
class ProgressBar:
    iteration = 0
    total = 0
    prefix = ''
    suffix = ''
    decimals = 2
    barLength = 100
     
    usePercentage = True
     
    label = ''
     
    fillingChar = '='
    emptyChar = ' ' #-
    beginChar = '['
    endChar = ']'
     
    def __init__(self, iteration, total = 100, fillingChar = '=', emptyChar = ' ', beginChar = '[', endChar = ']', prefix = '', suffix = '', decimals = 2, barLength = 30, **kwargs):
        self.iteration = iteration
        self.total = total
        self.fillingChar = fillingChar
        self.emptyChar = emptyChar
        self.beginChar = beginChar
        self.endChar = endChar
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.barLength = barLength
        if kwargs.get("label") != None:
            self.label = kwargs.get("label")
 
        if kwargs.get("usePercentage") == False:
            self.usePercentage = False
        else:
            self.usePercentage = True
             
        self.updateProgress(iteration, self.label)
     
    def updateProgress(self, iteration, label):
 
        self.iteration = iteration
        self.label = label
        filledLength    = int(round(self.barLength * self.iteration / float(self.total)))
        percents        = round(100.00 * (iteration / float(self.total)), self.decimals)
        bar             = self.fillingChar * filledLength + self.emptyChar * (self.barLength - filledLength)
 
        sys.stdout.write("\r                                                                            ")
        if self.usePercentage:
            sys.stdout.write('\r%s %s%s%s %s%s %s' % (self.prefix, self.beginChar, bar, self.endChar, percents, '%', self.suffix)),
        else:
            sys.stdout.write('\r%s %s%s%s %s %s' % (self.prefix, self.beginChar, bar, self.endChar, label, self.suffix)),
        sys.stdout.flush()
        if self.iteration == self.total:
            sys.stdout.write('\n')
            sys.stdout.flush()
