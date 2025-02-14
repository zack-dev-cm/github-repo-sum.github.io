# whoami

I’m a deep learning and computer vision enthusiast who loves building things that *just might* make life easier—or at least more interesting. If you spot me squinting at a screen, I’m probably wrangling neural networks or figuring out how to make an AI agent tap around an Android screen all by itself. Here’s a quick peek at my journey and some of the projects I’ve built along the way.

---

## in a Nutshell

- **Senior Deep Learning Engineer** with 5+ years of experience, focusing on everything from classification and segmentation to OCR and multi-modal transformer reasoning models.  
- **Upwork Top Rated Plus** contractor, recognized in the top 1% of AI developers, with 100% Job Success.  
- **Mentor & Teacher**: I’ve led corporate programs, taught undergraduates the fundamentals of computer vision, and discovered I really enjoy sharing knowledge.

---

## Toolbelt & Tech Playground

- **Frameworks/Libraries**: PyTorch, TensorFlow, Keras, FastAI, OpenAI APIs, CLIP, Vision-Language foundation models.  
- **Languages**: Primarily Python, with supporting roles from Dart (Flutter), Kotlin/Java, Swift, and C++.  
- **DevOps & Infra**: GCP, AWS, Docker, Kubernetes, Cloud Build, Cloud Run, and a dash of ML Ops for good measure.  
- **Mobile & Embedded**: TensoRT, TFLite, CoreML, ONNX, etc.

---

## Some Projects & Creations

### 1. Android Remote Control with VLM AI Agents
**“Hands-free” Android automation? Yes, please.**  
A custom Android app that captures screenshots and sends them to vision-language AI agents which figure out the next UI action—tap, swipe, or type.  
- **Real-Time**: Gets instructions from powerful server-based models.  
- **Use Cases**: Automated testing, daily phone tasks, or exploring novel ways to control a device.

**Demo Link**: [View MP4  in Google Drive](https://drive.google.com/file/d/13UQTdBVsZwPclMOca6Nmaywk4BiRydbi/view?usp=sharing)
![Android Remote Control with VLM AI Agents](samples/android_become_human-ezgif.com-speed.gif "Android Remote Control with VLM AI Agents")



---

### 2. Control VLM-LLM Agent Silently With Your Breath
Start or stop the neural network with your breath. “Start listening” might be 2–3 short exhalations, while a smooth exhalation says “stop.” It’s all about recognizing **breathing** patterns, not your voice. After calibration (reading text aloud vs. silently), it learns to detect words from the sounds of breathing or sniffles alone.

**Demo Link**: [View GIF in Google Drive](https://drive.google.com/file/d/1H43aT5n8NWlOuTIWsJinssKRh1n3tiOM/view?usp=sharing)  
![Breathing Control Demo](samples/mlbreath.gif "Breathing Control")

---

### 3. Create, Chat & AR experience with AI-character. Text2Room
**Image & Video Generation • Inpainting • TryOn • Reasoning & More**  
Spin up an AI “character,” style them, dress, chat with them in Telegram or even place in your living room! Perfect for marketing campaigns, creative collaborations, or just having fun with next-gen generative AI.

[**Live Demo (Colab-based)**](https://adfeed-1095464065298.us-central1.run.app/)  
**Video Link**: [View MP4 with sound in Google Drive](https://drive.google.com/file/d/1kvg4gjCNFPmrI3URPsM3eIyQ_vqSk1Ow/view?usp=sharing)

![Create, Chat & AR experience with AI-character](samples/adfeed_her.gif "Create & Chat: AI Fashion Models, Ad Campaigns, or Pokémon Buddies")


---

### 4. Label and Inpaint Anything in a Room Interior
Label objects in a photo, then seamlessly inpaint them—complete with realistic shadows and lighting for interior makeovers.

**Inpainting Demos (Google Drive):**  
- [Segmentation](https://drive.google.com/file/d/1XqQgbmBgTlRRdR-K3X4PHlSzrmiMUJgY/view?usp=sharing)  
- [Inpaint #1](https://drive.google.com/file/d/1dCkeI7Mi87cg2kOgY5UCLG-DiHkt358L/view?usp=sharing)  
- [Inpaint #2](https://drive.google.com/file/d/1xRmS8AXMJcmk-S0mth8yUQpltyfPkOSI/view?usp=sharing)  
- [Inpaint #3](https://drive.google.com/file/d/18kD2cm0uYmzudvOqVFmtJ8ZCkEbqqIHc/view?usp=sharing)

<img src="samples/interior/marble_floor_w_reflections.png" width="480">
<img src="samples/interior/download (81).png" width="480">

| Original                                      | Another Example                                 |
|----------------------------------------------|-------------------------------------------------|
| <img src="samples/interior/1.png" width="200"> | <img src="samples/interior/2sample.png" width="200"> |

---

### 5. Smart Drive for Smart City: Predict Optimal Speed to the Nearest Traffic Light or Jam
Find an optimal speed to the nearest traffic light.  
For example, you’re driving and you never know whether you should speed up a bit or slow down. The program predicts the ideal speed from your start to end point, calculating the optimal speed for each traffic light on the way. It can also predict the ideal speed to nearest traffic jams along the way.

<img src="samples/smart_drive/smart_drive3.png" width="640" />

---


 ---

### 6. Estimate Golf Ball Trajectory
Analyze your golf swing or build sports analytics solutions—this AI estimates the ball trajectory and more.

![Estimate Golf Ball Trajectory](samples/golf/1.png "Estimate Golf Ball Trajectory")


---

### 7. Pixel-Wise Segmentation of Spare Parts for 3D Printing
Precisely identify which parts need 3D printing or rework.

- [Segmentation #1](https://drive.google.com/file/d/1bAyEPYLbiETD0vKStnpB1VvzK1wKdKRv/view?usp=sharing)  
- [Segmentation #2](https://drive.google.com/file/d/1xVEonSJ7jvnYSnQ6ztvFZy-Llf_dxSrP/view?usp=sharing)

Local files:

| Example 1                                     | Example 2                                     |
|----------------------------------------------|-----------------------------------------------|
| <img src="samples/key_segm/download (61).png" width="200"> | <img src="samples/key_segm/download (62).png" width="200"> |

---

### 8. Food Recognition App
**When you want your phone to know what’s for dinner**  
AI app that identifies food items (packaged or fresh) and performs OCR on labels.  
- **Nutritional Info**: Extract brand names, nutrient data, and portion sizes.  
- **Works in Real-Time**: Over 90% accuracy, optimized for CPU/GPU inference.  
- **Cross-Platform**: iOS & Android.

**Demo Link**: [View GIF in Google Drive](https://drive.google.com/file/d/1RRRVYH0DLILZX84v5x0boj68VfMqnWWf/view?usp=sharing)



---

### 9. Python Library: AutoToloka
**Speedy dataset prep & crowdsourcing**  
A Python library to help set up and validate datasets, using interactive segmentation and multi-modal networks under the hood.  
- **Reduces Labeling Costs**: Automates a chunk of manual labeling.  
- **Scalable**: Integrates easily with pipeline tools, containerized deployments, and major clouds.

[**AutoToloka on PyPI**](https://pypi.org/project/autotoloka/)

---

### 10. Python Library: shiftlab-ocr
A library for handwriting text segmentation and character recognition.

[**shiftlab-ocr on PyPI**](https://pypi.org/project/shiftlab-ocr/)

---

### 11. Face Antispoofing & Multi-Modal Vision-Language Models
Because cameras can be tricked sometimes, I experiment with CLIP and other multi-modal setups to detect spoofing in face authentication systems, bridging text-image embeddings with advanced, specialized neural networks.

[**YouTube Presentation**](https://www.youtube.com/watch?v=jJnyj0OH0lk&t=285s&ab_channel=TolokaAI)

---

### 12. GitHub Repo Summarizer (Chrome Extension)
**Speed-read your repositories**  
Uses your locally stored GitHub personal access token to fetch and summarize code structure—**no servers** involved.  
- **No Third-Party Sharing**: Token stays on your device.  
- **Auto Summaries**: Quickly see how a repo is organized, from directories to major code files.

[**GitHub Repo Summarizer**](https://chromewebstore.google.com/detail/github-repo-summarizer/ccikgbjalcbokaalidnfcjhhbhjoljfm)

---

### 13. ChatGPT Scrollbar (Chrome Extension)
**Tired of scrolling forever through ChatGPT’s conversation feed?**  
I was too! So I built a nifty extension that adds a navigable scrollbar with clickable dashes for quick jumps. Simple but oh-so-handy.  
- **Local-Only Storage**: No external pings or data collection.  
- **Auto-Hide**: Keeps your screen tidy when you don’t need it.

**Demo Link**: [View GIF in Google Drive](https://drive.google.com/file/d/1fhf6l85wv-uYGc_jqDdoEXHvDMYBLyH4/view?usp=sharing)  
![ChatGPT Scrollbar Demo](samples/scroller.gif "ChatGPT Scrollbar")

[**ChatGPT Scrollbar on Chrome Web Store**](https://chromewebstore.google.com/detail/chatgpt-scrollbar/jnoonpeekddinkiecaonhocaflcgbhap?pli=1)

---

## More Highlights

- **Top 1%** on Upwork for AI/ML tasks.  
- **Mentored** teams at corporate events, universities, and School of AI chapters.  
- **Hackathon Finalist**: Digital Transformation, PicsArt AI.

[**See more on LinkedIn**](https://www.linkedin.com/in/zakhar-pashkin-a524a6163/)

---

## Let’s Build Something

If you’re looking for:
- **Custom AI solutions** (computer vision, NLP, or multi-modal)  
- **Mobile & embedded model optimization**  
- **ML Ops** for GCP/AWS or on-prem solutions  

Then let’s talk!

**Email**: [kaisenaiko@gmail.com](mailto:kaisenaiko@gmail.com)  
**GitHub**: [github.com/zack-dev-cm](https://github.com/zack-dev-cm)  
**GitHub**: [github.com/ZackPashkin](https://github.com/ZackPashkin)

Thanks for stopping by. Let’s see where AI can take us next!
