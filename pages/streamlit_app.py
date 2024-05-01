import streamlit as st
st.title("The Ultimate Football Quiz")
st.header("Will you beat it?")
st.radio ("Select Your Level",["EASY -(Is that all you can do?)","Medium-(Well I guess its alright)", "HARD -(No Way you beat this)"])
st.button("START!")
st.image("https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/06/01/22/Liverpool-trophy.jpg")
col1, col2, col3 = st.columns(3)
with col1:
   st.image("https://tse4.mm.bing.net/th/id/OIP.y1wPfoNdn-XMSeVwWT0PyAHaEK?rs=1&pid=ImgDetMain")
with col3:
   st.image("https://everyevery.ng/wp-content/uploads/2019/11/everyevry.ng-UEFA-Champions-League-Round-16-Stage.jpg")
