import streamlit as st
import base64

# TODO: In Line 35 put the audio of the text!!!


# Code from https://discuss.streamlit.io/t/how-to-play-an-audio-file-automatically-generated-using-text-to-speech-in
# -streamlit/33201/2
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


def render_pirate():
    st.sidebar.progress(45)

    st.sidebar.markdown(f""" <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p> <p style="line-height: 
    100%; font-size: 1.1vw;">Eisenhower First Try</p> <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower 
    Method</p> <p style="line-height: 100%; font-size: 1.1vw;">Eisenhower Applied</p> <p style="padding-left: 30px; 
    line-height:100%; font-size: 1.3vw;"><strong>Pirate Encounter</strong></p> """, unsafe_allow_html=True)

    col1, col2 = st.columns((1, 3), gap='large')
    with col1:
        st.markdown(f""" <p style="line-height:130%; font-size: 1.3vw; color: 
        white"><br><br><br><br><br><br><br></p>""", unsafe_allow_html=True)
        st.image("pictures/pirate.png")
        autoplay_audio("audio/Orinoco-Flow.mp3")  # TODO: Put here the audio of the text!!!
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.3vw; color: white">Arr, gather 'round, ye lads!<br>Sit tight 
            and listen close, for I've a tale to tell that'll curl yer toes and set the wind in yer sails. Once upon 
            a time, not so long ago, I sailed the vast and treacherous seas, seeking fortune and adventure at every 
            turn. But, fate had other plans for this old sea dog. A fierce storm, the likes of which I'd never seen, 
            swept me ship off course and dashed it upon the jagged rocks of this cursed isle. For years I've been 
            marooned here, a castaway left to fend for meself. But fear not, for I've learned a thing or two about 
            survival in these harsh and unforgiving lands. Ye see, survival ain't just about strength and skill; it's 
            about adaptin' to yer surroundings, makin' do with what ye have, and never losin' hope. Take heed, 
            young ones, for I'll share with ye the secrets of me survival. First and foremost, ye must master the art 
            of findin' water. Without ye will not survive the day. Next ye must learn to find shelter from the 
            elements. Build yerself a sturdy shelter, a haven from the wind and rain, and ye'll weather any storm 
            that comes yer way. And don´t forget ye also need food. The sea be teemin' with life, me hearties, 
            so cast yer lines and nets and reap the bounty that lies beneath the waves. And don't be afraid to forage 
            the land for fruits and berries, for nature provides for those who know where to look. But survival ain't 
            just about yer daily bread; it's about stayin' sharp in both mind and body. Keep yer wits about ye at all 
            times, for danger lurks in every shadow. Train yer body to endure the rigors of this harsh land, 
            for only the strong survive in the end. And finally, me lads, never lose sight of yer true goal. Ye may 
            be stranded on this island for now, but never give up hope of escapin' its clutches and returnin' to the 
            open sea. Keep in mind that time is essential for survival, use it wisely. Repair yer boat, gather yer 
            supplies, and when the time is right, set sail for freedom once more. So heed me words well, me hearties, 
            and ye'll find that even in the darkest of times, there be light to guide ye home. For as long as there 
            be breath in yer lungs and fire in yer hearts, ye'll never be truly lost at sea.<br>Now, enough of me 
            ramblin's! Let's raise a toast to adventure, to survival, and to the boundless spirit of the open sea! Yo 
            ho ho!</p>""",
            unsafe_allow_html=True
        )

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue"):
            st.session_state.place = "cornell_method"
            st.rerun()
