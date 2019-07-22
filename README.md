# Steganography
Encrypting data into images

Given any data,<br/>
<br/>
Represent each letter using its ASCII value.(8 bits)<br/>
Group 3 pixels to represent a character. [ 1pixel -> RGB (3 values)]  Hence 3 pixels -> 9 values out of which 8 will be encoded<br/>
change the value to ODD number if corresponding bit is 1<br/>
change the value to EVEN number if corresponding bit is 0<br/>

Use the remaining bit (9th one) to inform the end of message.<br/>
If the 9th bit is high it indicates end of message<br/>
If the th bit is low it indicates that the complete message has not yet been decrypted.</br>


Run the EncoderUI.py file,<br/>
Choose an image, to encrypt data<br/>
enter the text in the Textfield of the Window.<br/>
Click on the encrypt button to encrypt the text into the chosen image file<br/>
The encrypted image will be saved as encrypted.png<br/>
<br/>
To decrypt the image to get back the data<br/>
Run the DecoderUI.py file, <br/>
choose the image encrypted.png and click on the decrypt button to decrypt the text.<br/>
