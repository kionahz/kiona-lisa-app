import streamlit as st


def render_pirate():
    st.sidebar.progress(10)  # Todo anpassen

    st.sidebar.markdown(f"""
            <p style="line-height: 100%; font-size: 1.1vw;">Introduction</p>
            <p style="padding-left: 30px; line-height:100%; font-size: 1.2vw;"><strong>Backpack</strong></p>
        """, unsafe_allow_html=True)  # todo anpassen

    col1, col2 = st.columns((1, 3), gap='large')
    with col1:
        st.image("../pictures/pirate.png")
    with col2:
        st.markdown(
            f""" <p style="line-height:130%; font-size: 1.5vw; color: white">Arr, gather 'round, ye lads! Sit tight 
            and listen close, for I've a tale to tell that'll curl yer toes and set the wind in yer sails. Once upon 
            a time, not so long ago, I sailed the vast and treacherous seas, seeking fortune and adventure at every 
            turn. But, fate had other plans for this old sea dog. A fierce storm, the likes of which I'd never 
            seen, swept me ship off course and dashed it upon the jagged rocks of this cursed isle. For years I've 
            been marooned here, a castaway left to fend for meself. But fear not, for I've learned a thing or two 
            about survival in these harsh and unforgiving lands. Ye see, survival ain't just about strength and 
            skill; it's about adaptin' to yer surroundings, makin' do with what ye have, and never losin' hope. Take 
            heed, young ones, for I'll share with ye the secrets of me survival. First and foremost, ye must master 
            the art of findin' water. Without ye will not survive the day. Next ye must learn to find shelter from 
            the elements. Build yerself a sturdy shelter, a haven from the wind and rain, and ye'll weather any storm 
            that comes yer way. And don´t forget ye also need food. The sea be teemin' with life, me hearties, 
            so cast yer lines and nets and reap the bounty that lies beneath the waves. And don't be afraid to forage 
            the land for fruits and berries, for nature provides for those who know where to look. But survival ain't 
            just about yer daily bread; it's about stayin' sharp in both mind and body. Keep yer wits about ye at all 
            times, for danger lurks in every shadow. Train yer body to endure the rigors of this harsh land, 
            for only the strong survive in the end. And finally, me lads, never lose sight of yer true goal. Ye may 
            be stranded on this island for now, but never give up hope of escapin' its clutches and returnin' to the 
            open sea. Repair yer boat, gather yer supplies, and when the time is right, set sail for freedom once 
            more. So heed me words well, me hearties, and ye'll find that even in the darkest of times, 
            there be light to guide ye home. For as long as there be breath in yer lungs and fire in yer hearts, 
            ye'll never be truly lost at sea. Now, enough of me ramblin's! Let's raise a toast to adventure, 
            to survival, and to the boundless spirit of the open sea! Yo ho ho!</p>""",
            unsafe_allow_html=True
        )

    cola, colb = st.columns((8, 1))
    with colb:
        if st.button("Continue"):
            st.session_state.place = "cornell_method"
            st.rerun()
