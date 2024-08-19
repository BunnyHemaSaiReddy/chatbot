import streamlit as st
import time
import io
import google.generativeai as genai
import speech_recognition as sr
import gtts
import googlesearch
import bunny_lang
import pywhatkit.playonyt as playonyt
import asyncio

                   
def speak():
    rec=sr.Recognizer()
    with sr.Microphone() as mic:
        sound=rec.listen(mic)
        text_rec=rec.recognize_google(sound)
        return text_rec
    
def text_to_text():
    if 'out' not in st.session_state:
      st.session_state['out']=[]
    if 'History' not in st.session_state:
      st.session_state['History']=[]
    with st.sidebar:
        st.header(":rainbow[History] **🤖**")
        for i,j in enumerate(st.session_state['History']):
            @st.dialog(j)
            def display_hist(i):
                st.success(st.session_state['out'][i])
            if st.button(j):
                display_hist(i)
    api='AIzaSyCBHTmgKXbiputUhfU9PlFUufQYVGqsMHs'
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-pro') 
    st.markdown('## :red[Input type:]')
    chat_c=st.radio("",("Text📄","Speak🎤"))
    dict_lang=bunny_lang.lang()
    choice_trans=st.selectbox("Select the language for output:",["DEFAULT-English"]+list(dict_lang.keys()))
    to='en'
    input_text=""
    if choice_trans!="DEFAULT-English":
        to=dict_lang[choice_trans]
    if chat_c=="Text📄":
        st.session_state[input_text]=""
        input_text=st.text_area('**🤖**',key="input_text",placeholder='Enter the prompt.....',disabled=False)
        
    elif chat_c=='Speak🎤':
        st.markdown("### :violet[Speak now:] 🗣️ ")
        input_text=st.text_area('**🤖**',value=speak(),disabled=False)
    if st.button("Generate:") and input_text:
        for i in range(1):
            if st.button("cancel"):
                break
            async def genmsg():
                return model.generate_content(input_text)
            async def spin():
                with st.spinner("Generating..."):
                    await asyncio.sleep(2)
            async def main():
                result, _ = await asyncio.gather(genmsg(), spin())
                return result
            result = asyncio.run(main())
            st.session_state['History'].append(input_text)
            if result:
                for i in result:
                    output=i.text
                output=bunny_lang.trans(output,to)
                i__='''f 0 and st.button("Send whatshapp") :
                    ph_no=st.text_input(label="Enter the Phone number:",placeholder=0000000000)
                    if len(ph_no)==10:
                        pywhatkit.whats.sendwhatmsg_instantly("+91"+ph_no,output)'''
                def generate():
                    for i in output:
                        yield i
                        time.sleep(0.02)
                st.write_stream(generate)
                st.session_state['out'].append(output)     
                st.header("Relevant video")
                __='''def get_video_url(query):
                    try:
                        link = pywhatkit.playonyt(query, open_video=False)
                        return link
                    except Exception as e:
                        return 
                try:
                    video_links = [get_video_url(input_text) for query in '123']
                    col1, col2, col3 = st.columns(len(video_links))
                    with col1:
                        if video_links[0]:
                            st.video(video_links[0], width=300, height=300)
                    with col2:
                        if video_links[1]:
                            st.video(video_links[1], width=300, height=300)
                    with col3:
                        if video_links[2]:
                            st.video(video_links[2], width=300, height=300)
                except Exception:
                  pass'''
                link=playonyt(input_text,open_video=False)
                st.video(link)
                st.write(link)
                try:
                    st.markdown("### :red[Links that provide extra content for your text :]")
                    query=input_text
                    g_s=googlesearch.search(query,num_results=5)
                    for j in g_s:
                        st.write(j)
                except Exception as e:
                    j=str(e)[45:]
                    st.warning(j)
                try:
                    sound_text=gtts.gTTS(output,lang=to)
                    audio_buffer = io.BytesIO()
                    sound_text.write_to_fp(audio_buffer)
                    audio_buffer.seek(0)                    
                    st.audio(audio_buffer,format="audio/mp3")
                except Exception:
                    pass
                if st.button("New attempt"):
                    st.session_state[input_text]=""
                    st.rerun()

text_to_text() 
