                 ****************AADHAR CARD OCR - Version 1.0****************

QUICK NOTE: First execute "card extractor.py" and then "text parser.py"

        DESCRIPTION:
    The project is based on the following pipeline

  Card Blob  --->  Noise reduction  --->  Character  --->  Information
  Detection        and elimination        Recognition      Segmentation

      STEP 1: Card Blob Detection
This step is accomplished through edge detection of the boundaries of the card followed by blob
cropping. We are using the Canny edge detector for edge detection. To crop out the aadhar blob
we are using warp perspective.

All these functionalities are incorporated in the script "card extractor.py" so you are required
to run that first. This script will generate an image named "crop.jpg" which contains the cropped
out image of the aadhar card blob. Do not move or rename that image to another location or the
program will crash.
--------------------------------------------------------------------------------------------------

      STEP 2: Noise reduction and elimination
Here we try to remove useless elements like photograph of person, QR code, headers and footers,
line segments, etc. The accuracy of this step depends upon how much bright is the image and how
better is it cropped and oriented and, thus, depends upon the quality of image "crop.jpg" obtained
by executing "card extractor.py". Therefore, accuracy of the previous step will have a good effect
on the accuracy of this step. The accuracy cannot be theoretically calculated so experimentation is
the only way to determine it.
--------------------------------------------------------------------------------------------------

      STEP 3: Character Recognition
Character recognition is accomplished via the wrapper class for tesseract-ocr which is pytesseract.

Following are the scripts for which tesseract-ocr can be trained:
1.  Arabic script
2.  Bengali script
3.  Devanagari script
4.  Gujarati script
5.  Gurmukhi script
6.  Kannada script
7.  Malayalam script
8.  Oriya script
9.  Sinhala script
10. Tamil script
11. Telugu script

Following are the languages for which  tesseract-ocr can be trained:
1.  Math/equation detection module
2.  Arabic
3.  Assamese
4.  Bengali
5.  Persian
6.  Gujarati
7.  Hindi
8.  Kannada
9.  Malayalam
10. Marathi
11. Oriya
12. Panjabi/Punjabi
13. Sanskrit
14. Sinhala/Sinhalese
15. Sindhi
16. Tamil
17. Telugu
18. Urdu

Though tesseract-ocr can be trained for the above mentioned scripts and languages, currenly it's trained 
for English because:
1. It's present on almost all aadhar cards.
2. Tesseract gives much greater accuracy for English compared to other languages and scripts.

Again, the accuracy of this step depends upon how much noise free is the card blob.
This step is implemented in the script "text parser.py".
-----------------------------------------------------------------------------------------------------

STEP 4: Information Segmentation
From the data obtained in the previous step, in this step useful information like name, date of birth,
gender and uid are extracted. The segmentation works fine for new Aadhar card formats and is expected
to work fine for older formats too. This step is again implemented in the script "text parser.py".
