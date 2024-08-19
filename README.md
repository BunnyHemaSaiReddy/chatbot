# chatbot
# Streamlit Text-to-Text Application Documentation
# Overview
This application leverages multiple APIs and libraries to create an interactive tool that allows users to input prompts via text or speech, generate AI-driven content, translate the output into different languages, and access related resources like YouTube videos and web links. The app also includes features for generating and playing back audio versions of the generated text.

# Features
## Input Methods:

Text Input: Users can manually enter text prompts.
Speech Input: Users can speak their prompts, which are then converted to text using Google's Speech Recognition.

## AI Content Generation:

Utilizes Google's Generative AI (gemini-pro model) to generate content based on the provided prompts.
Language Translation:

Translates the AI-generated content into a selected language using the bunny_lang library.
## WhatsApp Integration:

Provides an option to send the generated content directly via WhatsApp using the pywhatkit library.
## Video and Web Content Retrieval:

Fetches relevant YouTube videos related to the input prompt.
Retrieves web links that provide additional information on the input topic using Google's search API.
## Text-to-Speech Conversion:

Converts the generated content into speech using the gtts library and plays the audio.
## User Interaction:

Interactive buttons and input fields guide users through generating, translating, and using the content.
A spinner is displayed while content is being generated to improve user experience.
## Usage Flow
Select Input Type: Choose between Text📄 (text input) or Speak🎤 (speech input).

Input Prompt: Enter text or speak your prompt depending on the selected input method.

Select Language: Choose the language for the output from a dropdown list.

Generate Content: Click the "Generate" button to create content based on the input.

## View and Use Output:

The generated text is displayed, with options to:
View related YouTube videos.
Access additional web resources.
Play the generated content as audio.
Send the content via WhatsApp.
Retry Option: A "New attempt" button allows users to clear inputs and start over.

## API and Library Details
Google Generative AI (gemini-pro): Powers the content generation based on user prompts.
SpeechRecognition: Captures and converts spoken language into text.
Google Text-to-Speech (gtts): Converts text to speech, allowing playback of generated content.
PyWhatKit: Facilitates sending WhatsApp messages and searching YouTube.
Bunny_lang: Handles language translation.
Google Search API: Retrieves relevant web links based on the generated content.
## Error Handling
The app includes error handling mechanisms to manage issues like speech recognition errors, translation issues, and Google API errors. Alerts and warnings are displayed to guide the user when an error occurs.
## Customization
Users can easily modify the app to change the AI model, add more languages, or integrate with additional APIs based on their needs.
