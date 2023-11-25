#pip install pyqrcode
#(importing dependencies/modules/packages , we can import 'pyqrcode *' as well)
import pyqrcode 
#(from parent u are opening child code(method))
from pyqrcode import QRCode    
  
# String which represent the QR code 
s = "https://www.youtube.com/channel/UCBz4yaxNxfiz1XYh-07UfWQ"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
#Scalable Vector Graphics
url.svg("myyoutube.svg", scale = 8) 
