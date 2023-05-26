import subprocess as sub 
import numpy as np 

array = np.array( [5,7,9,11,13,15,19,21,31,41,51,61,91,101,131] )
array = array.astype( str )
resistor_count = np.array([])
impediance = np.array([])

# 1. runs the 'file.py' python script to generate the desired netlist code 
# 2. the .cir file thus generated is further run by this script to generate an out.txt file 
# 3. out.txt is scraped for the desired current value, i 
# 4. this i value, alog with the lattice length and resistor count is stored in a .csv file for further analysis
with open( 'data.csv' , 'w' ) as data : 
    for index in array:
        data.writelines( [ index , ','] )
        result = sub.run( [ '/Users/ashmitbathla/Desktop/ltspice-nrtlist/inf-R-grid/file.py' , index ] )
        sub.call( 'ngspice< /Users/ashmitbathla/Desktop/ltspice-nrtlist/inf-R-grid/file.cir > out.txt' , shell = True )
        with open( 'rvalue.txt' , 'r') as f:
            data.writelines( [ f.read() , ','])
        with open( 'out.txt' , 'r') as f : 
            t = f.read().find('Vsource: Independent voltage source')
            f.seek(t)
            for i in range( 0 , 13 ):
                m = f.readline()
            data.writelines( [ str( round( -1/float( m[25:33] ) , 3 )) , '\n'])
array = array.astype( int )