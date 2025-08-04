# ✋🗣️ KheiroVox — From Hands to Voice

KheiroVox is an innovative hand gesture interpreter that recognizes sign language and converts it into spoken or textual output. It uses real-time computer vision and AI to bridge the communication gap between signers and non-signers.

---

## 📖 What Does "KheiroVox" Mean?

The name KheiroVox comes from:

- ✋ Kheiro (χειρ) — Greek for "hand"
- 🗣️ Vox — Latin for "voice"

Together, they form "Hand Voice" — a voice that speaks through hand gestures.

---

## 💡 Project Vision

Some speak through words. Others through silence.  
But hands speak louder when voices can’t.

KheiroVox empowers silent communication by:

- Detecting sign language gestures  
- Converting them into on-screen text  
- (Optional) Converting text into spoken audio

---

## ⚙️ How It Works

1. 🎥 Live Webcam Feed  
   Captures hand gestures in real-time using OpenCV.

2. 🖐️ Hand Landmark Detection  
   MediaPipe identifies 21 key hand points and tracks finger movement.

3. 🤖 Gesture Recognition  
   Uses finger positions to detect specific signs like Hello, Help, Yes, No.

4. 💬 Text Output  
   Recognized gestures are shown as subtitles on the screen.

5. 🔊 (Optional) Voice Output  
   Text can be spoken aloud using a text-to-speech engine like pyttsx3.

---

## 📦 Requirements

Install dependencies:

```bash
pip install opencv-python mediapipe
 Atlast:Press Q to quit the live feed.
