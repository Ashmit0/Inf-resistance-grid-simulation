#!/Users/ashmitbathla/opt/anaconda3/bin/python3
# this file generates the required ltspice netlist code for a user provided grid length
import sys 
import numpy as np 

length = int( sys.argv[1] ) # resistances along the length as input 
width = length - 1 

if length < 2 or length % 2 == 0 : 
    print( " long side nodes must be odd and >= 3 ")
    sys.exit( 1 )

# ground node lattice point
gnd_x = int( ( length + 1 )/2 ) 
gnd_y = int( ( width )/2 )
# voltage input node lattice point
v_x = int( ( length + 1 )/2 - 2 )
v_y = int( ( width )/2  -1 )
node_id = 1 ; # 0 is preserved for gnd! 

array = np.arange( length * width ) 
array = array.reshape( width , length )       

v_id = array[ v_y][ v_x ]
gnd_id = array[ gnd_y ][ gnd_x ]

# print( array ) 
# print( v_x , v_y , gnd_x , gnd_y )
# print(  v_id , gnd_id )

array = array.astype( str )
v_id = str( v_id )
gnd_id = str( gnd_id )

# The desired code is printed out to a .cir file
ini_stdout = sys.stdout 
with open( 'file.cir' , 'w') as f :
    sys.stdout = f 
    print("\n\n * Resistance latticle with node lenght " , length , '\n\n') 
    print("*Sources")
    print("vin" , v_id , gnd_id , 1 , '\n')
    print('*Resistance') 
    resistor_id = 1 
    for y in range( 0 , width ): 
        for x in range( 0 , length  ): 
            # Add a horizontal resistor
            if x <= length - 2:
                print( 'r' + str(resistor_id) , array[ y , x ] , array[ y , x + 1 ] , '1' )
                resistor_id += 1
            # Add a vertical resistor
            if y <= width - 2 : 
                print( 'r' + str(resistor_id) , array[y ,x ] , array[ y + 1 , x ] , '1' )
                resistor_id += 1
    print('\n *Directive')
    print('.op ; for DC analysis')
    print('.END') 
    sys.stdout = ini_stdout 

# resistance count value is stored for future refreance
with open( 'rvalue.txt' , 'w') as f :
    sys.stdout = f  
    print( resistor_id -1 )
    sys.stdout = ini_stdout      