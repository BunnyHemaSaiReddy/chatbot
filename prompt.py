import streamlit as st
import time
import io
import google.generativeai as genai
import speech_recognition as sr
import gtts
import googlesearch
import bunny_lang
import asyncio
from pytube import Search
                   
def speak():
    rec=sr.Recognizer()
    with sr.Microphone() as mic:
        sound=rec.listen(mic)
        text_rec=rec.recognize_google(sound)
        return text_rec

def fetch_youtube_links(query, num_results=3):
    search = Search(query)
    results = search.results
    video_links = [result.watch_url for result in results[:num_results]]    
    return video_links
   
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
                #chat_c="Text📄"
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
        try:
          input_text=st.text_area('**🤖**',value=speak(),disabled=False)
        except Exception:
            st.warning("After 3 seconds ,you can try Again.Speak loud..🗣️🗣️")
            time.sleep(3)
            st.rerun()
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
            if result:
                for i in result:
                    output=i.text
                output=bunny_lang.trans(output,to)
                __='''if 0 and st.button("Send whatshapp") :
                    ph_no=st.text_input(label="Enter the Phone number:",placeholder=0000000000)
                    if len(ph_no)==10:
                        pywhatkit.whats.sendwhatmsg_instantly("+91"+ph_no,output)'''
                def generate():
                    for i in output:
                        yield i
                        time.sleep(0.02)
                if input_text not in st.session_state['History']:
                    st.session_state['History'].append(input_text)
                    st.session_state['out'].append(output)
                st.write_stream(generate)
                links = fetch_youtube_links(input_text)
                st.header("Relevant video link")
                # for link in links:
                #     st.write(link)
                columns = st.columns(len(links))
                for i, link in enumerate(links):
                    with columns[i]:
                        st.video(link)
                        st.write(link)
                # st.video(pywhatkit.playonyt(input_text,open_video=False))
                # st.write(pywhatkit.playonyt(input_text,open_video=False))
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
