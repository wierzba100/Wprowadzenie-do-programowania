import serial
import time

# internal
com=None
def open():
    global com
#    com = serial.Serial('COM3',115200,timeout=1)  # Windows
    com = serial.Serial('/dev/ttyUSB0',115200,timeout=1)  # Linux
    time.sleep(0.5)
    com.flushInput()

def _write_command_read_answer(cmd):
   global com
   com.write(cmd.encode('UTF-8')+b'\r\n')
   com.flushOutput()
   com.readline()
   r=com.readline()
   com.read(3)
   return r.decode('UTF-8').strip()

def _write_command(cmd):
   global com
   com.write(cmd.encode('UTF-8')+b'\r\n')
   com.flushOutput()
   com.readline()
   com.read(3) #len(cmd)+2+3+1)

# API
   
def set_port(state):
    _write_command('set('+str(state)+')')   
    
def get_port():
    return int(_write_command_read_answer('get()'))
   
def led(state):
   _write_command('led('+str(state)+')')

def  but():
   return int(_write_command_read_answer('but()')) #.strip('\''),16)

def  det():
   return int(_write_command_read_answer('det()'))

def  pot():
   return int(_write_command_read_answer('pot()'))

def close():
    com.close()

