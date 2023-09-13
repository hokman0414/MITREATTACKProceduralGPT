# MITREATT&CKProceduralGPT (Proof Of Concept)
The main aim of this project is to address the existing challenges in Cyber Threat Intelligence (CTI), particularly in the rapid and precise generation of Tactics, Techniques, and Procedures (TTP) based on Mitre's ATT&CK framework. Currently, CTI analysts spend a disproportionate amount of time dissecting and interpreting Mitre T-codes manually, resulting in delays that could be costly to organizational security.

# Objectives:
- Automate the extraction of procedural level TTPs from various reports, thereby saving CTI analysts' time.
- Offer Red teams and offensive security personnel a tool that could help them emulate various threat actors.
- Provide procedural-level TTPs as examples for Threat Hunting and Threat Detection rule creation.
- Produce quicker analysis for better-defined intelligence products.

# Concept Design:
![image](https://github.com/hokman0414/MitreProceduralGPT/assets/106271123/acbe8e8c-71e6-4a62-909d-b2b4afc68119)


# Goal:
This DOES NOT fully automate CTI analyst task of dissection BUT does ASSIST in the manual dissection process (pinpoint where attack is shown which speeds up the identification process). CTI analyst/engineers should still verify the claims of these quickly per all Intelligence Products + Product validation processes(aka peer and Final review). 

# Enabling Detection Rule Creation:
Uncomment the codes at the bottom within main.py and specify the detection rule.
![image](https://github.com/hokman0414/MITREATTACKProceduralGPT/assets/106271123/cd88200b-3d85-4d6f-9237-915332d770b9)


# Usage: 
Please make sure to install all requirements before running.
```
pip install -r requirements.txt
```
Add API keys (Input ChatGPT API key in Backend.py and Scraper API Key input in LinkScrapeData.py)
https://www.scraperapi.com/ - ScraperAPI
https://platform.openai.com/account/api-keys - GPT KEY

Run Streamlit app
```
streamlit run main.py
```
Video Usage: https://youtu.be/ZKeZSmAKOy4

# Final Note:
This project still requires editing of the prompts and possible finetuning to help improve the accuracy. I will continue to make future updates on this project.
