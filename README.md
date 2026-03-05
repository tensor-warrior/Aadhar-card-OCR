## Aadhaar OCR - Version 1.0

The Aadhaar OCR project is designed as a modular computer vision pipeline that automates the extraction of personal information from Aadhaar cards. The process is divided into four primary stages: **Card Blob Detection**, **Noise Reduction**, **Character Recognition**, and **Information Segmentation**. This architecture ensures that the raw image is progressively refined and parsed into structured data.

### Phase 1: Card Blob Detection

The initial stage focuses on isolating the card from its background. This is achieved using the Canny edge detection algorithm to identify the card’s boundaries, followed by a warp perspective transformation in OpenCV to crop and "flatten" the card into a top-down view. These operations are handled by the `card_extractor.py` script, which outputs a standardized file named `crop.jpg`. Because the subsequent pipeline relies on this specific file, it must remain in the root directory to avoid execution errors.

### Phase 2: Noise Reduction and Pre-processing

Once the card is isolated, the system filters out non-textual elements that could interfere with OCR accuracy. This includes the removal of the individual's photograph, QR codes, headers, footers, and decorative line segments. The effectiveness of this stage is highly sensitive to the lighting, orientation, and crop quality of the `crop.jpg` image generated in the previous step. While formal accuracy metrics are still being gathered, preliminary testing shows robust results when provided with high-quality input.

### Phase 3: Optical Character Recognition (OCR)

Text extraction is performed using **PyTesseract**, a Python wrapper for Google’s Tesseract-OCR engine. While Tesseract supports a vast array of Indic scripts—including Devanagari, Bengali, Gujarati, and Tamil—and their corresponding languages, this version is specifically optimized for English. English was chosen as the primary target because it is a universal field on almost all Aadhaar formats and currently yields the highest recognition accuracy within the Tesseract engine. This logic is encapsulated within the `text_parser.py` script.

### Phase 4: Information Segmentation

The final stage parses the raw text strings into specific data fields. Using the `text_parser.py` script, the system identifies and extracts the cardholder's **Name**, **Date of Birth**, **Gender**, and **UID (Aadhaar Number)**. The segmentation logic is designed to be compatible with both the latest Aadhaar card layouts and legacy formats, ensuring reliable data capture across different card versions.
